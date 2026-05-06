import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.mathdoz.core_mathdoz import sqrt_doz
from errors import TrezRuntimeError


def _zeros_like(data):
    if not isinstance(data, list):
        return 0.0
    return [_zeros_like(x) for x in data]


def _add_elem(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        return a + b
    if not isinstance(a, list):
        a = [a] * len(b)
    if not isinstance(b, list):
        b = [b] * len(a)
    return [_add_elem(ai, bi) for ai, bi in zip(a, b)]


def _mul_elem(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        return a * b
    if not isinstance(a, list):
        a = [a] * len(b)
    if not isinstance(b, list):
        b = [b] * len(a)
    return [_mul_elem(ai, bi) for ai, bi in zip(a, b)]


def _scale(data, scalar):
    if not isinstance(data, list):
        return data * scalar
    return [_scale(x, scalar) for x in data]


def _sum_all(data):
    if not isinstance(data, list):
        return data
    return sum(_sum_all(x) for x in data)


def _transpose(m):
    if not isinstance(m[0], list):
        return [[v] for v in m]
    rows, cols = len(m), len(m[0])
    return [[m[r][c] for r in range(rows)] for c in range(cols)]


def _matmul(a, b):
    """a: (m,n)  b: (n,p)  →  (m,p). Ambos deben ser listas de listas."""
    m, n = len(a), len(a[0])
    b_cols = len(b[0]) if isinstance(b[0], list) else 1
    if isinstance(b[0], list):
        p = b_cols
        return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
    else:
        return [sum(a[i][k] * b[k] for k in range(n)) for i in range(m)]


class Tensor:
    """
    Tensor con soporte para autograd sobre escalares y matrices (listas anidadas).
    data puede ser un número, una lista 1D o una lista de listas 2D.
    """

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = None          # None hasta que backward() lo inicialice
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Tensor(data={self.data}, grad={self.grad})"

    # ------------------------------------------------------------------
    # Forma
    # ------------------------------------------------------------------

    @property
    def shape(self):
        def _s(d):
            if not isinstance(d, list):
                return ()
            return (len(d),) + _s(d[0])
        return _s(self.data)

    # ------------------------------------------------------------------
    # Operaciones aritméticas escalares y vectoriales
    # ------------------------------------------------------------------

    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(_add_elem(self.data, other.data), (self, other), '+')

        def _backward():
            _accum(self, out.grad)
            _accum(other, out.grad)
        out._backward = _backward
        return out

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(_add_elem(self.data, _scale(other.data, -1.0)), (self, other), '-')

        def _backward():
            _accum(self, out.grad)
            _accum(other, _scale(out.grad, -1.0))
        out._backward = _backward
        return out

    def __rsub__(self, other):
        return Tensor(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(_mul_elem(self.data, other.data), (self, other), '*')

        def _backward():
            _accum(self, _mul_elem(other.data, out.grad))
            _accum(other, _mul_elem(self.data, out.grad))
        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * Tensor(-1.0)

    def __truediv__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        return self * (other ** -1.0)

    def __pow__(self, power):
        power = float(power)

        def _pow_data(d, p):
            if not isinstance(d, list):
                return d ** p
            return [_pow_data(x, p) for x in d]

        out = Tensor(_pow_data(self.data, power), (self,), f'**{power}')

        def _backward():
            def _pow_grad(d, g, p):
                if not isinstance(d, list):
                    return p * (d ** (p - 1)) * g
                return [_pow_grad(di, gi, p) for di, gi in zip(d, g)]
            _accum(self, _pow_grad(self.data, out.grad, power))
        out._backward = _backward
        return out

    # ------------------------------------------------------------------
    # Álgebra lineal
    # ------------------------------------------------------------------

    def matmul(self, other):
        """Multiplicación matricial (m,n) @ (n,p) → (m,p) con backward."""
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(_matmul(self.data, other.data), (self, other), 'matmul')

        def _backward():
            # grad_self  = out.grad @ other.T
            # grad_other = self.T  @ out.grad
            g = out.grad if isinstance(out.grad, list) else [[out.grad]]
            _accum(self, _matmul(g, _transpose(other.data)))
            _accum(other, _matmul(_transpose(self.data), g))
        out._backward = _backward
        return out

    def T(self):
        """Transposición 2D con backward."""
        out = Tensor(_transpose(self.data), (self,), 'T')

        def _backward():
            _accum(self, _transpose(out.grad))
        out._backward = _backward
        return out

    # ------------------------------------------------------------------
    # Activaciones
    # ------------------------------------------------------------------

    def relu(self):
        def _relu(d):
            if not isinstance(d, list):
                return max(0.0, d)
            return [_relu(x) for x in d]

        out = Tensor(_relu(self.data), (self,), 'relu')

        def _backward():
            def _relu_grad(d, g):
                if not isinstance(d, list):
                    return g if d > 0 else 0.0
                return [_relu_grad(di, gi) for di, gi in zip(d, g)]
            _accum(self, _relu_grad(self.data, out.grad))
        out._backward = _backward
        return out

    # ------------------------------------------------------------------
    # Backward pass
    # ------------------------------------------------------------------

    def backward(self):
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)

        build_topo(self)
        # Gradiente inicial: 1 para escalar, matriz de unos para tensor
        self.grad = _ones_like(self.data)
        for node in reversed(topo):
            node._backward()

    def zero_grad(self):
        self.grad = None
        for child in self._prev:
            child.zero_grad()


# ------------------------------------------------------------------
# Helpers de acumulación de gradientes
# ------------------------------------------------------------------

def _ones_like(data):
    if not isinstance(data, list):
        return 1.0
    return [_ones_like(x) for x in data]


def _accum(tensor, grad_val):
    """Acumula grad_val en tensor.grad (suma si ya existe)."""
    if tensor.grad is None:
        tensor.grad = grad_val
    else:
        tensor.grad = _add_elem(tensor.grad, grad_val)
