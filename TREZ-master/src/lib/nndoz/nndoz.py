import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import random
from lib.mathdoz.core_mathdoz import exp_doz, sqrt_doz
from errors import TrezRuntimeError


# ------------------------------------------------------------------
# Helpers internos
# ------------------------------------------------------------------

def _zeros(rows, cols):
    return [[0.0] * cols for _ in range(rows)]


def _matmul(a, b):
    """a: (m,n)  b: (n,p) → (m,p)."""
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


def _add_broadcast(mat, bias_row):
    """Suma bias_row (1 x cols) a cada fila de mat (batch x cols)."""
    return [[mat[i][j] + bias_row[0][j] for j in range(len(mat[i]))] for i in range(len(mat))]


def _scale(data, scalar):
    if not isinstance(data, list):
        return data * scalar
    return [_scale(x, scalar) for x in data]


def _add_elem(a, b):
    if not isinstance(a, list):
        return a + b
    return [_add_elem(ai, bi) for ai, bi in zip(a, b)]


def _sum_cols(mat):
    """Suma a lo largo de las filas → vector de longitud cols (para grad del bias)."""
    cols = len(mat[0])
    return [[sum(mat[i][j] for i in range(len(mat))) for j in range(cols)]]


# ------------------------------------------------------------------
# Capas
# ------------------------------------------------------------------

def linear_init(in_features, out_features):
    """
    Crea e inicializa una capa Linear con Xavier/Glorot.
    Retorna un dict: {type: 'linear', W: [[...]], b: [[...]], in: int, out: int}
    """
    limit = sqrt_doz(6.0 / (in_features + out_features))
    W = [[random.uniform(-limit, limit) for _ in range(out_features)]
         for _ in range(in_features)]
    b = [[random.uniform(-limit, limit) for _ in range(out_features)]]
    return {'type': 'linear', 'W': W, 'b': b, 'in': in_features, 'out': out_features}


def linear_forward(layer, x):
    """
    Forward de una capa linear.
    x:    (batch, in_features)
    layer: dict de linear_init
    Retorna (batch, out_features).
    """
    if not isinstance(x, list) or not isinstance(x[0], list):
        raise TrezRuntimeError("NNdoz.linear_forward: x debe ser lista de listas (batch x features).")
    out = _matmul(x, layer['W'])
    return _add_broadcast(out, layer['b'])


def linear_backward(layer, x, grad_out):
    """
    Backward de linear. Retorna dict con grad_W, grad_b, grad_x.
    grad_out: (batch, out_features)
    """
    grad_W = _matmul(_transpose(x), grad_out)           # (in, out)
    grad_b = _sum_cols(grad_out)                          # (1, out)
    grad_x = _matmul(grad_out, _transpose(layer['W']))   # (batch, in)
    return {'grad_W': grad_W, 'grad_b': grad_b, 'grad_x': grad_x}


def relu_forward(x):
    """ReLU elemento a elemento. Retorna (out, mask) para el backward."""
    def _relu(d):
        if not isinstance(d, list):
            return max(0.0, d)
        return [_relu(v) for v in d]

    def _mask(d):
        if not isinstance(d, list):
            return 1.0 if d > 0 else 0.0
        return [_mask(v) for v in d]

    out = _relu(x)
    mask = _mask(x)
    return out, mask


def relu_backward(mask, grad_out):
    """Backward de ReLU usando la máscara guardada en forward."""
    def _apply(m, g):
        if not isinstance(m, list):
            return m * g
        return [_apply(mi, gi) for mi, gi in zip(m, g)]
    return _apply(mask, grad_out)


def softmax_forward(x):
    """
    Softmax numericamente estable por fila.
    x: (batch, n_clases)
    Retorna (out, out) — guarda la salida para backward.
    Nota: el backward de softmax standalone es el jacobiano completo;
    en la práctica se combina con cross_entropy y se usa cross_entropy_grad.
    """
    if not isinstance(x, list) or not isinstance(x[0], list):
        raise TrezRuntimeError("NNdoz.softmax_forward: x debe ser (batch x clases).")
    out = []
    for row in x:
        max_val = max(row)
        exp_vals = [exp_doz(v - max_val) for v in row]
        s = sum(exp_vals)
        out.append([e / s for e in exp_vals])
    return out


def sequential_forward(layers, x):
    """
    Pasa x por una lista de capas en orden.
    Cada capa es un dict con 'type' y los parámetros correspondientes.
    Retorna (output, cache) donde cache es la lista de activaciones intermedias.
    """
    cache = [x]
    current = x
    for layer in layers:
        t = layer.get('type')
        if t == 'linear':
            current = linear_forward(layer, current)
        elif t == 'relu':
            current, layer['_mask'] = relu_forward(current)
        elif t == 'softmax':
            current = softmax_forward(current)
        else:
            raise TrezRuntimeError(f"NNdoz.sequential_forward: tipo de capa desconocido '{t}'.")
        cache.append(current)
    return current, cache


def get_params(layers):
    """Extrae lista plana de [W, b, W, b, ...] de todas las capas linear."""
    params = []
    for layer in layers:
        if layer.get('type') == 'linear':
            params.append(layer['W'])
            params.append(layer['b'])
    return params


def get_param_count(layers):
    """Número total de parámetros entrenables."""
    total = 0
    for layer in layers:
        if layer.get('type') == 'linear':
            W = layer['W']
            total += len(W) * len(W[0])
            total += len(layer['b'][0])
    return total
