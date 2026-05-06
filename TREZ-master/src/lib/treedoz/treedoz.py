"""
treedoz.py — Árbol de Decisión inspirado en sklearn.DecisionTreeClassifier.

Usa el criterio Gini para splits binarios recursivos.

API expuesta al lenguaje TREZ:
  Treedoz.crear(max_prof, min_muestras, criterio)
  Treedoz.entrenar(arbol, X, y)
  Treedoz.predecir(arbol, X)
  Treedoz.predecir_proba(arbol, X)
  Treedoz.puntaje(arbol, X, y)
  Treedoz.profundidad(arbol)
  Treedoz.num_hojas(arbol)
  Treedoz.importancia(arbol)          → importancia relativa de cada feature
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TrezRuntimeError


# ──────────────────────────────────────────────────────────────────────────────
# Criterios de impureza
# ──────────────────────────────────────────────────────────────────────────────

def _gini(y):
    if not y:
        return 0.0
    n = len(y)
    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((c / n) ** 2 for c in counts.values())

def _entropy(y):
    if not y:
        return 0.0
    n = len(y)
    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    result = 0.0
    import math
    for c in counts.values():
        p = c / n
        if p > 0:
            result -= p * math.log2(p)
    return result

def _impureza(y, criterio):
    if criterio == 'gini':
        return _gini(y)
    elif criterio == 'entropy':
        return _entropy(y)
    else:
        raise TrezRuntimeError(f"Treedoz: criterio '{criterio}' desconocido. Use 'gini' o 'entropy'.")

def _majority_class(y):
    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    return max(counts, key=lambda lbl: counts[lbl])

def _class_proba(y, classes):
    n = len(y)
    counts = {c: 0 for c in classes}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    return [counts[c] / n for c in classes] if n > 0 else [1.0 / len(classes)] * len(classes)


# ──────────────────────────────────────────────────────────────────────────────
# Nodo del árbol
# ──────────────────────────────────────────────────────────────────────────────

class _Node:
    def __init__(self):
        self.is_leaf = False
        self.clase = None           # para hojas
        self.proba = None           # distribución en hoja
        self.feature_idx = None     # índice de feature para split
        self.threshold = None       # umbral del split
        self.left = None            # rama izquierda (<=)
        self.right = None           # rama derecha (>)
        self.impurity_decrease = 0.0  # para importancia de features


# ──────────────────────────────────────────────────────────────────────────────
# Construcción del árbol
# ──────────────────────────────────────────────────────────────────────────────

def _best_split(X, y, criterio, feature_importances):
    n_samples = len(X)
    n_features = len(X[0])
    best_gain = -1.0
    best_feat = None
    best_thresh = None
    base_impurity = _impureza(y, criterio)

    for feat in range(n_features):
        values = sorted(set(row[feat] for row in X))
        thresholds = [(values[i] + values[i+1]) / 2.0 for i in range(len(values) - 1)]

        for thresh in thresholds:
            left_y  = [y[i] for i in range(n_samples) if X[i][feat] <= thresh]
            right_y = [y[i] for i in range(n_samples) if X[i][feat] > thresh]
            if not left_y or not right_y:
                continue
            gain = base_impurity - (
                len(left_y)  / n_samples * _impureza(left_y, criterio) +
                len(right_y) / n_samples * _impureza(right_y, criterio)
            )
            if gain > best_gain:
                best_gain = gain
                best_feat = feat
                best_thresh = thresh

    return best_feat, best_thresh, best_gain


def _build_tree(X, y, classes, criterio, max_prof, min_muestras, depth, feature_importances):
    node = _Node()
    n = len(y)

    # Condiciones de parada
    if (n < min_muestras or
        _impureza(y, criterio) == 0.0 or
        (max_prof is not None and depth >= max_prof)):
        node.is_leaf = True
        node.clase = _majority_class(y)
        node.proba = _class_proba(y, classes)
        return node

    feat, thresh, gain = _best_split(X, y, criterio, feature_importances)
    if feat is None or gain <= 0:
        node.is_leaf = True
        node.clase = _majority_class(y)
        node.proba = _class_proba(y, classes)
        return node

    # Registrar importancia del feature
    feature_importances[feat] = feature_importances.get(feat, 0.0) + gain * n

    # Dividir
    left_idx  = [i for i in range(len(X)) if X[i][feat] <= thresh]
    right_idx = [i for i in range(len(X)) if X[i][feat] > thresh]
    X_left  = [X[i] for i in left_idx];  y_left  = [y[i] for i in left_idx]
    X_right = [X[i] for i in right_idx]; y_right = [y[i] for i in right_idx]

    node.feature_idx = feat
    node.threshold = thresh
    node.impurity_decrease = gain
    node.left  = _build_tree(X_left,  y_left,  classes, criterio, max_prof, min_muestras, depth+1, feature_importances)
    node.right = _build_tree(X_right, y_right, classes, criterio, max_prof, min_muestras, depth+1, feature_importances)
    return node


def _predict_one(node, x):
    if node.is_leaf:
        return node.clase, node.proba
    if x[node.feature_idx] <= node.threshold:
        return _predict_one(node.left, x)
    else:
        return _predict_one(node.right, x)


def _tree_depth(node):
    if node is None or node.is_leaf:
        return 0
    return 1 + max(_tree_depth(node.left), _tree_depth(node.right))

def _count_leaves(node):
    if node is None:
        return 0
    if node.is_leaf:
        return 1
    return _count_leaves(node.left) + _count_leaves(node.right)


# ──────────────────────────────────────────────────────────────────────────────
# Clase principal
# ──────────────────────────────────────────────────────────────────────────────

class _DecisionTree:
    def __init__(self, max_prof, min_muestras, criterio):
        self.max_prof = max_prof
        self.min_muestras = min_muestras
        self.criterio = criterio
        self.root = None
        self.classes_ = None
        self.feature_importances_ = {}
        self._fitted = False

    def fit(self, X, y):
        if not X or not y:
            raise TrezRuntimeError("Treedoz.entrenar: X e y no pueden estar vacíos.")
        Xm = [row if isinstance(row, list) else [row] for row in X]
        self.classes_ = sorted(set(y), key=lambda v: (str(type(v)), v))
        self.feature_importances_ = {}
        self.root = _build_tree(Xm, list(y), self.classes_, self.criterio,
                                self.max_prof, self.min_muestras, 0, self.feature_importances_)
        # Normalizar importancias
        total = sum(self.feature_importances_.values()) or 1.0
        self.feature_importances_ = {k: round(v / total, 4) for k, v in self.feature_importances_.items()}
        self._fitted = True

    def predict(self, X):
        if not self._fitted:
            raise TrezRuntimeError("Treedoz: modelo no entrenado.")
        Xm = [row if isinstance(row, list) else [row] for row in X]
        return [_predict_one(self.root, x)[0] for x in Xm]

    def predict_proba(self, X):
        if not self._fitted:
            raise TrezRuntimeError("Treedoz: modelo no entrenado.")
        Xm = [row if isinstance(row, list) else [row] for row in X]
        return [_predict_one(self.root, x)[1] for x in Xm]

    def score(self, X, y):
        preds = self.predict(X)
        return sum(1 for p, t in zip(preds, y) if p == t) / len(y) if y else 0.0


# ──────────────────────────────────────────────────────────────────────────────
# API funcional
# ──────────────────────────────────────────────────────────────────────────────

def crear(max_prof=None, min_muestras=2, criterio='gini'):
    max_p = int(max_prof) if max_prof is not None else None
    return _DecisionTree(max_p, int(min_muestras), str(criterio))

def entrenar(arbol, X, y):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.entrenar: primer argumento debe ser un DecisionTree.")
    arbol.fit(X, y)
    return arbol

def predecir(arbol, X):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.predecir: primer argumento debe ser un DecisionTree.")
    return arbol.predict(X)

def predecir_proba(arbol, X):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.predecir_proba: primer argumento debe ser un DecisionTree.")
    return arbol.predict_proba(X)

def puntaje(arbol, X, y):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.puntaje: primer argumento debe ser un DecisionTree.")
    return arbol.score(X, y)

def profundidad(arbol):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.profundidad: primer argumento debe ser un DecisionTree.")
    if not arbol._fitted:
        raise TrezRuntimeError("Treedoz.profundidad: modelo no entrenado.")
    return _tree_depth(arbol.root)

def num_hojas(arbol):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.num_hojas: primer argumento debe ser un DecisionTree.")
    if not arbol._fitted:
        raise TrezRuntimeError("Treedoz.num_hojas: modelo no entrenado.")
    return _count_leaves(arbol.root)

def importancia(arbol):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.importancia: primer argumento debe ser un DecisionTree.")
    if not arbol._fitted:
        raise TrezRuntimeError("Treedoz.importancia: modelo no entrenado.")
    return arbol.feature_importances_

def clases(arbol):
    if not isinstance(arbol, _DecisionTree):
        raise TrezRuntimeError("Treedoz.clases: primer argumento debe ser un DecisionTree.")
    return arbol.classes_ or []
