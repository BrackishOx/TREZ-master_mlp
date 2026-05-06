"""
logregdoz.py — Regresión Logística inspirada en sklearn.LogisticRegression.

Soporta clasificación binaria y multiclase (One-vs-Rest).
Optimiza con Gradiente Descendente (SGD).

API expuesta al lenguaje TREZ:
  LogRegdoz.crear(lr, max_iter, tol, verbose)
  LogRegdoz.entrenar(modelo, X, y)
  LogRegdoz.predecir(modelo, X)
  LogRegdoz.predecir_proba(modelo, X)
  LogRegdoz.puntaje(modelo, X, y)
  LogRegdoz.set_lr(modelo, nueva_lr)
  LogRegdoz.get_lr(modelo)
  LogRegdoz.coeficientes(modelo)
  LogRegdoz.historial(modelo)
"""

import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.mathdoz.core_mathdoz import exp_doz, log_doz
from errors import TrezRuntimeError


# ──────────────────────────────────────────────────────────────────────────────
# Sigmoid
# ──────────────────────────────────────────────────────────────────────────────

def _sigmoid(z):
    if z >= 0:
        return 1.0 / (1.0 + exp_doz(-z))
    e = exp_doz(z)
    return e / (1.0 + e)

def _dot(w, x):
    return sum(wi * xi for wi, xi in zip(w, x))


# ──────────────────────────────────────────────────────────────────────────────
# Clasificador binario (base para OvR)
# ──────────────────────────────────────────────────────────────────────────────

class _BinaryLogReg:
    """Regresión logística binaria con SGD."""
    def __init__(self, lr, max_iter, tol):
        self.lr = lr
        self.max_iter = max_iter
        self.tol = tol
        self.w = None   # pesos
        self.b = 0.0    # bias
        self.loss_history = []

    def fit(self, X, y_bin):
        n_features = len(X[0])
        self.w = [0.0] * n_features
        self.b = 0.0
        n = len(X)
        self.loss_history = []

        for epoch in range(self.max_iter):
            # Shuffle
            indices = list(range(n))
            random.shuffle(indices)
            epoch_loss = 0.0

            for i in indices:
                xi = X[i]
                yi = y_bin[i]
                z = _dot(self.w, xi) + self.b
                pred = _sigmoid(z)
                error = pred - yi
                # Gradiente descend: w -= lr * error * x
                self.w = [wi - self.lr * error * xi[j] for j, wi in enumerate(self.w)]
                self.b -= self.lr * error
                # Loss: binary cross-entropy
                p = max(min(pred, 1 - 1e-10), 1e-10)
                if yi == 1:
                    epoch_loss -= log_doz(p)
                else:
                    epoch_loss -= log_doz(1.0 - p)

            avg_loss = epoch_loss / n
            self.loss_history.append(avg_loss)
            if avg_loss < self.tol:
                break

    def predict_proba_one(self, x):
        return _sigmoid(_dot(self.w, x) + self.b)


# ──────────────────────────────────────────────────────────────────────────────
# Clasificador multiclase One-vs-Rest
# ──────────────────────────────────────────────────────────────────────────────

class _LogisticRegression:
    def __init__(self, lr, max_iter, tol, verbose):
        self.lr = lr
        self.max_iter = max_iter
        self.tol = tol
        self.verbose = verbose
        self.classes_ = None
        self.classifiers_ = {}   # clase → _BinaryLogReg
        self.loss_history = []
        self._fitted = False

    def fit(self, X, y):
        if not X or not y:
            raise TrezRuntimeError("LogRegdoz.entrenar: X e y no pueden estar vacíos.")
        if len(X) != len(y):
            raise TrezRuntimeError("LogRegdoz.entrenar: X e y deben tener el mismo largo.")

        Xm = [row if isinstance(row, list) else [row] for row in X]
        self.classes_ = sorted(set(y), key=lambda v: (str(type(v)), v))

        if len(self.classes_) == 2:
            # Binario directo
            c = self.classes_[1]
            y_bin = [1 if yi == c else 0 for yi in y]
            clf = _BinaryLogReg(self.lr, self.max_iter, self.tol)
            clf.fit(Xm, y_bin)
            self.classifiers_[c] = clf
            self.loss_history = clf.loss_history
        else:
            # One-vs-Rest
            all_losses = []
            for c in self.classes_:
                y_bin = [1 if yi == c else 0 for yi in y]
                clf = _BinaryLogReg(self.lr, self.max_iter, self.tol)
                clf.fit(Xm, y_bin)
                self.classifiers_[c] = clf
                all_losses.append(clf.loss_history)
            # Promedio de pérdidas por época
            n_epochs = min(len(l) for l in all_losses)
            self.loss_history = [
                sum(all_losses[j][i] for j in range(len(self.classes_))) / len(self.classes_)
                for i in range(n_epochs)
            ]

        if self.verbose:
            for i, loss in enumerate(self.loss_history[-10:], 1):
                print(f"  LogReg — última época {len(self.loss_history)-10+i}: pérdida={loss:.6f}  lr={self.lr}")

        self._fitted = True

    def predict_proba(self, X):
        if not self._fitted:
            raise TrezRuntimeError("LogRegdoz: modelo no entrenado.")
        Xm = [row if isinstance(row, list) else [row] for row in X]

        if len(self.classes_) == 2:
            c1 = self.classes_[1]
            clf = self.classifiers_[c1]
            result = []
            for x in Xm:
                p1 = clf.predict_proba_one(x)
                result.append([1 - p1, p1])
            return result
        else:
            # OvR: normalizar scores
            result = []
            for x in Xm:
                scores = [self.classifiers_[c].predict_proba_one(x) for c in self.classes_]
                total = sum(scores)
                if total == 0:
                    total = 1.0
                result.append([s / total for s in scores])
            return result

    def predict(self, X):
        proba = self.predict_proba(X)
        return [self.classes_[max(range(len(row)), key=lambda j: row[j])] for row in proba]

    def score(self, X, y):
        preds = self.predict(X)
        return sum(1 for p, t in zip(preds, y) if p == t) / len(y) if y else 0.0


# ──────────────────────────────────────────────────────────────────────────────
# API funcional
# ──────────────────────────────────────────────────────────────────────────────

def crear(lr=0.1, max_iter=200, tol=1e-4, verbose=False):
    return _LogisticRegression(float(lr), int(max_iter), float(tol), bool(verbose))

def entrenar(modelo, X, y):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.entrenar: primer argumento debe ser un LogisticRegression.")
    modelo.fit(X, y)
    return modelo

def predecir(modelo, X):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.predecir: primer argumento debe ser un LogisticRegression.")
    return modelo.predict(X)

def predecir_proba(modelo, X):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.predecir_proba: primer argumento debe ser un LogisticRegression.")
    return modelo.predict_proba(X)

def puntaje(modelo, X, y):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.puntaje: primer argumento debe ser un LogisticRegression.")
    return modelo.score(X, y)

def set_lr(modelo, nueva_lr):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.set_lr: primer argumento debe ser un LogisticRegression.")
    modelo.lr = float(nueva_lr)
    for clf in modelo.classifiers_.values():
        clf.lr = float(nueva_lr)
    return modelo

def get_lr(modelo):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.get_lr: primer argumento debe ser un LogisticRegression.")
    return modelo.lr

def coeficientes(modelo):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.coeficientes: primer argumento debe ser un LogisticRegression.")
    if not modelo._fitted:
        raise TrezRuntimeError("LogRegdoz.coeficientes: modelo no entrenado.")
    result = {}
    for c, clf in modelo.classifiers_.items():
        result[str(c)] = {'pesos': clf.w, 'bias': clf.b}
    return result

def historial(modelo):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.historial: primer argumento debe ser un LogisticRegression.")
    return modelo.loss_history

def clases(modelo):
    if not isinstance(modelo, _LogisticRegression):
        raise TrezRuntimeError("LogRegdoz.clases: primer argumento debe ser un LogisticRegression.")
    return modelo.classes_ or []
