"""
kndoz.py — K-Vecinos más Cercanos (K-Nearest Neighbors) inspirado en sklearn.

API expuesta al lenguaje TREZ:
  KNdoz.crear(k, metrica)           → crea clasificador KNN
  KNdoz.entrenar(knn, X, y)         → memoriza el dataset
  KNdoz.predecir(knn, X)            → predice clases
  KNdoz.predecir_proba(knn, X)      → probabilidades por clase (votación)
  KNdoz.puntaje(knn, X, y)          → exactitud
  KNdoz.set_k(knn, nuevo_k)         → cambia el número de vecinos
  KNdoz.get_k(knn)                  → retorna k actual
  KNdoz.vecinos(knn, X, n)          → retorna los n vecinos más cercanos de cada muestra
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.mathdoz.core_mathdoz import sqrt_doz
from errors import TrezRuntimeError


# ──────────────────────────────────────────────────────────────────────────────
# Distancias
# ──────────────────────────────────────────────────────────────────────────────

def _dist_euclidea(a, b):
    if len(a) != len(b):
        raise TrezRuntimeError("KNdoz: vectores de distinta longitud.")
    return sqrt_doz(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))

def _dist_manhattan(a, b):
    if len(a) != len(b):
        raise TrezRuntimeError("KNdoz: vectores de distinta longitud.")
    return sum(abs(ai - bi) for ai, bi in zip(a, b))

def _distancia(a, b, metrica):
    if metrica == 'euclidea':
        return _dist_euclidea(a, b)
    elif metrica == 'manhattan':
        return _dist_manhattan(a, b)
    else:
        raise TrezRuntimeError(f"KNdoz: métrica '{metrica}' desconocida. Use 'euclidea' o 'manhattan'.")


# ──────────────────────────────────────────────────────────────────────────────
# Clase interna
# ──────────────────────────────────────────────────────────────────────────────

class _KNNClassifier:
    def __init__(self, k, metrica):
        self.k = k
        self.metrica = metrica
        self.X_train = None
        self.y_train = None
        self.classes_ = None
        self._fitted = False

    def fit(self, X, y):
        if not X or not y:
            raise TrezRuntimeError("KNdoz.entrenar: X e y no pueden estar vacíos.")
        if len(X) != len(y):
            raise TrezRuntimeError("KNdoz.entrenar: X e y deben tener el mismo número de muestras.")
        self.X_train = [row if isinstance(row, list) else [row] for row in X]
        self.y_train = list(y)
        self.classes_ = sorted(set(y), key=lambda v: (str(type(v)), v))
        self._fitted = True

    def _get_k_neighbors(self, x):
        """Retorna lista de (distancia, etiqueta) de los k vecinos más cercanos."""
        xv = x if isinstance(x, list) else [x]
        dists = [(idx, _distancia(xv, xt, self.metrica), self.y_train[idx])
                 for idx, xt in enumerate(self.X_train)]
        dists.sort(key=lambda t: t[1])
        return dists[:self.k]

    def predict_one(self, x):
        neighbors = self._get_k_neighbors(x)
        # Votación por mayoría (ponderada por 1/dist si dist>0)
        votes = {}
        for _, dist, label in neighbors:
            peso = 1.0 / (dist + 1e-10)
            votes[label] = votes.get(label, 0.0) + peso
        return max(votes, key=lambda lbl: votes[lbl])

    def predict(self, X):
        if not self._fitted:
            raise TrezRuntimeError("KNdoz: modelo no entrenado. Llama KNdoz.entrenar primero.")
        return [self.predict_one(x) for x in X]

    def predict_proba(self, X):
        if not self._fitted:
            raise TrezRuntimeError("KNdoz: modelo no entrenado.")
        result = []
        for x in X:
            neighbors = self._get_k_neighbors(x)
            votes = {c: 0.0 for c in self.classes_}
            for _, dist, label in neighbors:
                votes[label] = votes.get(label, 0.0) + 1.0 / (dist + 1e-10)
            total = sum(votes.values())
            result.append([votes[c] / total for c in self.classes_])
        return result

    def score(self, X, y):
        preds = self.predict(X)
        return sum(1 for p, t in zip(preds, y) if p == t) / len(y) if y else 0.0

    def get_neighbors(self, X, n=None):
        if not self._fitted:
            raise TrezRuntimeError("KNdoz: modelo no entrenado.")
        n = n if n is not None else self.k
        result = []
        for x in X:
            xv = x if isinstance(x, list) else [x]
            dists = [(_distancia(xv, xt, self.metrica), self.y_train[idx])
                     for idx, xt in enumerate(self.X_train)]
            dists.sort(key=lambda t: t[0])
            result.append([[round(d, 6), lbl] for d, lbl in dists[:n]])
        return result


# ──────────────────────────────────────────────────────────────────────────────
# API funcional
# ──────────────────────────────────────────────────────────────────────────────

def crear(k=5, metrica='euclidea'):
    return _KNNClassifier(int(k), str(metrica))

def entrenar(knn, X, y):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.entrenar: primer argumento debe ser un KNNClassifier.")
    knn.fit(X, y)
    return knn

def predecir(knn, X):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.predecir: primer argumento debe ser un KNNClassifier.")
    return knn.predict(X)

def predecir_proba(knn, X):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.predecir_proba: primer argumento debe ser un KNNClassifier.")
    return knn.predict_proba(X)

def puntaje(knn, X, y):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.puntaje: primer argumento debe ser un KNNClassifier.")
    return knn.score(X, y)

def set_k(knn, nuevo_k):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.set_k: primer argumento debe ser un KNNClassifier.")
    knn.k = int(nuevo_k)
    return knn

def get_k(knn):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.get_k: primer argumento debe ser un KNNClassifier.")
    return knn.k

def vecinos(knn, X, n=None):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.vecinos: primer argumento debe ser un KNNClassifier.")
    return knn.get_neighbors(X, n)

def clases(knn):
    if not isinstance(knn, _KNNClassifier):
        raise TrezRuntimeError("KNdoz.clases: primer argumento debe ser un KNNClassifier.")
    return knn.classes_ or []
