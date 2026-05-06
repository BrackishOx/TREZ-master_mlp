"""
mlpdoz.py — Perceptrón Multicapa (MLPClassifier) inspirado en scikit-learn.

API expuesta al lenguaje TREZ:
  MLPdoz.crear(capas_ocultas, lr, activacion, max_iter, batch_size, verbose)
  MLPdoz.entrenar(mlp, X, y)
  MLPdoz.predecir(mlp, X)
  MLPdoz.predecir_proba(mlp, X)
  MLPdoz.puntaje(mlp, X, y)         → exactitud (accuracy)
  MLPdoz.set_lr(mlp, nueva_lr)      → cambia la tasa de aprendizaje
  MLPdoz.get_lr(mlp)                → retorna la tasa de aprendizaje actual
  MLPdoz.matriz_confusion(y_real, y_pred)
  MLPdoz.reporte(y_real, y_pred, clases)
  MLPdoz.historial(mlp)             → lista de pérdidas por época
"""

import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.mathdoz.core_mathdoz import exp_doz, log_doz, sqrt_doz
from errors import TrezRuntimeError


# ──────────────────────────────────────────────────────────────────────────────
# Utilidades numéricas internas
# ──────────────────────────────────────────────────────────────────────────────

def _zeros(rows, cols):
    return [[0.0] * cols for _ in range(rows)]

def _scale(data, s):
    if not isinstance(data, list):
        return data * s
    return [_scale(x, s) for x in data]

def _add(a, b):
    if not isinstance(a, list):
        return a + b
    return [_add(ai, bi) for ai, bi in zip(a, b)]

def _sub(a, b):
    if not isinstance(a, list):
        return a - b
    return [_sub(ai, bi) for ai, bi in zip(a, b)]

def _matmul(a, b):
    """a: (m,n)  b: (n,p)  →  (m,p)"""
    m, n = len(a), len(a[0])
    if isinstance(b[0], list):
        p = len(b[0])
        return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
    else:
        return [sum(a[i][k] * b[k] for k in range(n)) for i in range(m)]

def _transpose(m):
    if not isinstance(m[0], list):
        return [[v] for v in m]
    rows, cols = len(m), len(m[0])
    return [[m[r][c] for r in range(rows)] for c in range(cols)]

def _add_bias(mat, bias_row):
    return [[mat[i][j] + bias_row[j] for j in range(len(mat[i]))] for i in range(len(mat))]

def _sum_cols(mat):
    cols = len(mat[0])
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(cols)]

def _clip(x, lo, hi):
    if not isinstance(x, list):
        return max(lo, min(hi, x))
    return [_clip(v, lo, hi) for v in x]


# ──────────────────────────────────────────────────────────────────────────────
# Funciones de activación
# ──────────────────────────────────────────────────────────────────────────────

def _relu(x):
    if not isinstance(x, list):
        return max(0.0, x)
    return [_relu(v) for v in x]

def _relu_mask(x):
    if not isinstance(x, list):
        return 1.0 if x > 0 else 0.0
    return [_relu_mask(v) for v in x]

def _sigmoid_scalar(x):
    if x >= 0:
        e = exp_doz(-x)
        return 1.0 / (1.0 + e)
    else:
        e = exp_doz(x)
        return e / (1.0 + e)

def _sigmoid(x):
    if not isinstance(x, list):
        return _sigmoid_scalar(x)
    return [_sigmoid(v) for v in x]

def _sigmoid_deriv(s):
    """s ya es sigmoid(x); deriv = s*(1-s)"""
    if not isinstance(s, list):
        return s * (1.0 - s)
    return [_sigmoid_deriv(v) for v in s]

def _tanh_scalar(x):
    ep = exp_doz(x)
    en = exp_doz(-x)
    d = ep + en
    if d == 0:
        return 0.0
    return (ep - en) / d

def _tanh(x):
    if not isinstance(x, list):
        return _tanh_scalar(x)
    return [_tanh(v) for v in x]

def _tanh_deriv(t):
    if not isinstance(t, list):
        return 1.0 - t * t
    return [_tanh_deriv(v) for v in t]

def _softmax_rows(x):
    out = []
    for row in x:
        mv = max(row)
        ev = [exp_doz(v - mv) for v in row]
        s = sum(ev)
        out.append([e / s for e in ev])
    return out

def _apply_activation(pre, act_name):
    if act_name == 'relu':
        out = _relu(pre)
        mask = _relu_mask(pre)
        return out, mask
    elif act_name == 'sigmoid':
        out = _sigmoid(pre)
        return out, out   # guardamos la salida (usada en deriv)
    elif act_name == 'tanh':
        out = _tanh(pre)
        return out, out
    else:
        raise TrezRuntimeError(f"MLPdoz: activación '{act_name}' desconocida. Use 'relu', 'sigmoid' o 'tanh'.")

def _activation_grad(cache_val, grad_out, act_name):
    """Retorna grad de la activación aplicado a grad_out."""
    if act_name == 'relu':
        # cache_val es la máscara
        def _apply(m, g):
            if not isinstance(m, list):
                return m * g
            return [_apply(mi, gi) for mi, gi in zip(m, g)]
        return _apply(cache_val, grad_out)
    elif act_name == 'sigmoid':
        # cache_val es sigmoid(x)
        def _sig_g(s, g):
            if not isinstance(s, list):
                return s * (1 - s) * g
            return [_sig_g(si, gi) for si, gi in zip(s, g)]
        return _sig_g(cache_val, grad_out)
    elif act_name == 'tanh':
        def _tanh_g(t, g):
            if not isinstance(t, list):
                return (1 - t * t) * g
            return [_tanh_g(ti, gi) for ti, gi in zip(t, g)]
        return _tanh_g(cache_val, grad_out)


# ──────────────────────────────────────────────────────────────────────────────
# Inicialización de pesos (Xavier)
# ──────────────────────────────────────────────────────────────────────────────

def _init_layer(fan_in, fan_out):
    limit = sqrt_doz(6.0 / (fan_in + fan_out))
    W = [[random.uniform(-limit, limit) for _ in range(fan_out)] for _ in range(fan_in)]
    b = [0.0] * fan_out
    return {'W': W, 'b': b, 'fan_in': fan_in, 'fan_out': fan_out}


# ──────────────────────────────────────────────────────────────────────────────
# Forward & Backward
# ──────────────────────────────────────────────────────────────────────────────

def _forward(layers, X, act_name, n_classes):
    """
    Propagación hacia adelante.
    Retorna (logits, cache_list)
    cache_list[i] = {'pre': ..., 'act_cache': ..., 'out': ...}
    """
    current = X
    cache = []
    for i, layer in enumerate(layers):
        pre = _add_bias(_matmul(current, layer['W']), layer['b'])
        if i < len(layers) - 1:
            out, act_cache = _apply_activation(pre, act_name)
        else:
            out = pre      # última capa: sin activación (logits para cross-entropy)
            act_cache = None
        cache.append({'input': current, 'pre': pre, 'act_cache': act_cache, 'out': out})
        current = out
    return current, cache   # current = logits finales


def _backward(layers, cache, logits, y_int, act_name, batch_size):
    """
    Retroceso (backprop) completo.
    Retorna lista de {'grad_W', 'grad_b'} para cada capa.
    """
    n_classes = len(logits[0])

    # Gradiente de cross-entropy + softmax (combinado)
    softmax_out = _softmax_rows(logits)
    grad_out = [row[:] for row in softmax_out]
    for i, t in enumerate(y_int):
        grad_out[i][t] -= 1.0
    grad_out = _scale(grad_out, 1.0 / batch_size)

    grads = []
    for i in reversed(range(len(layers))):
        c = cache[i]
        x_in = c['input']

        if i < len(layers) - 1:
            # Aplicar gradiente de activación
            grad_pre = _activation_grad(c['act_cache'], grad_out, act_name)
        else:
            grad_pre = grad_out

        grad_W = _matmul(_transpose(x_in), grad_pre)
        grad_b = _sum_cols(grad_pre)

        # grad para la capa anterior
        grad_out = _matmul(grad_pre, _transpose(layers[i]['W']))

        grads.insert(0, {'grad_W': grad_W, 'grad_b': grad_b})

    return grads


# ──────────────────────────────────────────────────────────────────────────────
# Clase interna MLPClassifier
# ──────────────────────────────────────────────────────────────────────────────

class _MLPClassifier:
    def __init__(self, hidden_layer_sizes, lr, activation, max_iter, batch_size, verbose):
        self.hidden_layer_sizes = hidden_layer_sizes   # lista de ints
        self.lr = lr
        self.activation = activation
        self.max_iter = max_iter
        self.batch_size = batch_size
        self.verbose = verbose
        self.layers = None         # lista de dicts {W, b}
        self.n_classes = None
        self.n_features = None
        self.classes_ = None       # lista de etiquetas únicas
        self.loss_history = []     # pérdida por época
        self._fitted = False

    def _build(self, n_features, n_classes):
        self.n_features = n_features
        self.n_classes = n_classes
        sizes = [n_features] + list(self.hidden_layer_sizes) + [n_classes]
        self.layers = [_init_layer(sizes[i], sizes[i+1]) for i in range(len(sizes)-1)]

    def fit(self, X, y):
        """Entrena el modelo. y puede ser lista de enteros o strings."""
        if not X or not y:
            raise TrezRuntimeError("MLPdoz.entrenar: X e y no pueden estar vacíos.")
        if len(X) != len(y):
            raise TrezRuntimeError("MLPdoz.entrenar: X e y deben tener el mismo número de muestras.")

        # Normalizar etiquetas a enteros
        unique_labels = sorted(set(y), key=lambda v: (str(type(v)), v))
        self.classes_ = unique_labels
        label_to_int = {lbl: i for i, lbl in enumerate(unique_labels)}
        y_int = [label_to_int[lbl] for lbl in y]

        n_features = len(X[0]) if isinstance(X[0], list) else 1
        n_classes = len(unique_labels)

        if not self._fitted:
            self._build(n_features, n_classes)
            self._fitted = True

        self.loss_history = []
        n = len(X)

        for epoch in range(self.max_iter):
            # Shuffle
            indices = list(range(n))
            random.shuffle(indices)
            epoch_loss = 0.0
            n_batches = 0

            for start in range(0, n, self.batch_size):
                batch_idx = indices[start:start + self.batch_size]
                bX = [X[i] if isinstance(X[i], list) else [X[i]] for i in batch_idx]
                by = [y_int[i] for i in batch_idx]
                bs = len(bX)

                logits, cache = _forward(self.layers, bX, self.activation, n_classes)

                # Cross-entropy loss
                loss = _cross_entropy_loss(logits, by)
                epoch_loss += loss
                n_batches += 1

                # Backprop
                grads = _backward(self.layers, cache, logits, by, self.activation, bs)

                # Actualizar pesos (SGD)
                for i, layer in enumerate(self.layers):
                    g = grads[i]
                    layer['W'] = _sub(layer['W'], _scale(g['grad_W'], self.lr))
                    layer['b'] = _sub(layer['b'], _scale(g['grad_b'], self.lr))

            avg_loss = epoch_loss / n_batches
            self.loss_history.append(avg_loss)

            if self.verbose and (epoch + 1) % 10 == 0:
                print(f"  Época {epoch+1}/{self.max_iter} — pérdida: {avg_loss:.6f}  lr: {self.lr}")

    def predict_proba(self, X):
        if not self._fitted:
            raise TrezRuntimeError("MLPdoz: el modelo no ha sido entrenado. Llama MLPdoz.entrenar primero.")
        Xm = [row if isinstance(row, list) else [row] for row in X]
        logits, _ = _forward(self.layers, Xm, self.activation, self.n_classes)
        return _softmax_rows(logits)

    def predict(self, X):
        proba = self.predict_proba(X)
        int_preds = [max(range(len(row)), key=lambda j: row[j]) for row in proba]
        return [self.classes_[i] for i in int_preds]

    def score(self, X, y):
        preds = self.predict(X)
        correct = sum(1 for p, t in zip(preds, y) if p == t)
        return correct / len(y) if y else 0.0


def _cross_entropy_loss(logits, targets):
    batch_size = len(logits)
    loss = 0.0
    for row, t in zip(logits, targets):
        mv = max(row)
        shifted = [v - mv for v in row]
        ev = [exp_doz(v) for v in shifted]
        s = sum(ev)
        loss -= (shifted[t] - log_doz(s))
    return loss / batch_size


# ──────────────────────────────────────────────────────────────────────────────
# Métricas de clasificación
# ──────────────────────────────────────────────────────────────────────────────

def confusion_matrix(y_real, y_pred):
    """
    Matriz de confusión.
    Retorna dict: {'clases': [...], 'matriz': [[...]]}
    """
    classes = sorted(set(y_real) | set(y_pred), key=lambda v: (str(type(v)), v))
    idx = {c: i for i, c in enumerate(classes)}
    n = len(classes)
    mat = [[0] * n for _ in range(n)]
    for r, p in zip(y_real, y_pred):
        mat[idx[r]][idx[p]] += 1
    return {'clases': classes, 'matriz': mat}

def classification_report(y_real, y_pred, classes=None):
    """
    Reporte de clasificación: precisión, recall, F1 por clase.
    Retorna dict {'clases': [...], 'precision': [...], 'recall': [...], 'f1': [...], 'soporte': [...], 'exactitud': float}
    """
    if classes is None:
        classes = sorted(set(y_real) | set(y_pred), key=lambda v: (str(type(v)), v))

    precision_list, recall_list, f1_list, support_list = [], [], [], []

    for c in classes:
        tp = sum(1 for r, p in zip(y_real, y_pred) if r == c and p == c)
        fp = sum(1 for r, p in zip(y_real, y_pred) if r != c and p == c)
        fn = sum(1 for r, p in zip(y_real, y_pred) if r == c and p != c)
        support = tp + fn
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec  = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1   = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        precision_list.append(round(prec, 4))
        recall_list.append(round(rec, 4))
        f1_list.append(round(f1, 4))
        support_list.append(support)

    accuracy = sum(1 for r, p in zip(y_real, y_pred) if r == p) / len(y_real) if y_real else 0.0

    return {
        'clases': classes,
        'precision': precision_list,
        'recall': recall_list,
        'f1': f1_list,
        'soporte': support_list,
        'exactitud': round(accuracy, 4),
    }


# ──────────────────────────────────────────────────────────────────────────────
# API funcional expuesta al visitor de TREZ
# ──────────────────────────────────────────────────────────────────────────────

def crear(hidden_layer_sizes=None, lr=0.001, activation='relu',
          max_iter=200, batch_size=32, verbose=False):
    """
    Crea un nuevo MLPClassifier.
    hidden_layer_sizes: lista de enteros, p.ej. [100] o [64, 32]
    lr:                 tasa de aprendizaje (float)
    activation:         'relu' | 'sigmoid' | 'tanh'
    max_iter:           número de épocas
    batch_size:         tamaño del mini-batch
    verbose:            mostrar progreso
    """
    if hidden_layer_sizes is None:
        hidden_layer_sizes = [100]
    if not isinstance(hidden_layer_sizes, list):
        hidden_layer_sizes = [int(hidden_layer_sizes)]
    hidden_layer_sizes = [int(h) for h in hidden_layer_sizes]
    return _MLPClassifier(hidden_layer_sizes, float(lr), activation,
                          int(max_iter), int(batch_size), bool(verbose))


def entrenar(mlp, X, y):
    """Entrena el modelo con X (features) e y (etiquetas)."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.entrenar: primer argumento debe ser un MLPClassifier creado con MLPdoz.crear.")
    mlp.fit(X, y)
    return mlp


def predecir(mlp, X):
    """Retorna lista de etiquetas predichas para X."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.predecir: primer argumento debe ser un MLPClassifier.")
    return mlp.predict(X)


def predecir_proba(mlp, X):
    """Retorna lista de probabilidades por clase para cada muestra de X."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.predecir_proba: primer argumento debe ser un MLPClassifier.")
    return mlp.predict_proba(X)


def puntaje(mlp, X, y):
    """Retorna la exactitud (accuracy) del modelo en X, y."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.puntaje: primer argumento debe ser un MLPClassifier.")
    return mlp.score(X, y)


def set_lr(mlp, nueva_lr):
    """Cambia la tasa de aprendizaje del modelo."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.set_lr: primer argumento debe ser un MLPClassifier.")
    mlp.lr = float(nueva_lr)
    return mlp


def get_lr(mlp):
    """Retorna la tasa de aprendizaje actual del modelo."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.get_lr: primer argumento debe ser un MLPClassifier.")
    return mlp.lr


def historial(mlp):
    """Retorna la lista de pérdidas por época del último entrenamiento."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.historial: primer argumento debe ser un MLPClassifier.")
    return mlp.loss_history


def clases(mlp):
    """Retorna las clases conocidas por el modelo."""
    if not isinstance(mlp, _MLPClassifier):
        raise TrezRuntimeError("MLPdoz.clases: primer argumento debe ser un MLPClassifier.")
    return mlp.classes_ or []


def matriz_confusion(y_real, y_pred):
    """Calcula la matriz de confusión entre etiquetas reales y predichas."""
    return confusion_matrix(y_real, y_pred)


def reporte(y_real, y_pred, clases_param=None):
    """Calcula precisión, recall y F1 por clase."""
    return classification_report(y_real, y_pred, clases_param)
