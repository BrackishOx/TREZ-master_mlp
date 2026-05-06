import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.mathdoz.core_mathdoz import sqrt_doz
from errors import TrezRuntimeError


def _zeros_like(data):
    if not isinstance(data, list):
        return 0.0
    return [_zeros_like(x) for x in data]


def _scale(data, scalar):
    if not isinstance(data, list):
        return data * scalar
    return [_scale(x, scalar) for x in data]


def _add_elem(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        return a + b
    if not isinstance(a, list):
        a = [a] * len(b)
    if not isinstance(b, list):
        b = [b] * len(a)
    return [_add_elem(ai, bi) for ai, bi in zip(a, b)]


def _sub_elem(a, b):
    if not isinstance(a, list):
        return a - b
    return [_sub_elem(ai, bi) for ai, bi in zip(a, b)]


def _square(data):
    if not isinstance(data, list):
        return data * data
    return [_square(x) for x in data]


def _sqrt_elem(data):
    if not isinstance(data, list):
        return sqrt_doz(data)
    return [_sqrt_elem(x) for x in data]


def _div_elem(a, b):
    if not isinstance(a, list):
        if b == 0:
            raise TrezRuntimeError("Optimdoz: división por cero en actualización Adam.")
        return a / b
    return [_div_elem(ai, bi) for ai, bi in zip(a, b)]


# ---------------------------------------------------------------------------
# SGD con momentum opcional
# ---------------------------------------------------------------------------

class _SGDState:
    def __init__(self, params, lr, momentum):
        self.params = params        # lista de listas (pesos)
        self.lr = lr
        self.momentum = momentum
        self.velocities = [_zeros_like(p) for p in params]
        self.step_count = 0

    def step(self, grads):
        if len(grads) != len(self.params):
            raise TrezRuntimeError("Optimdoz.sgd_step: número de gradientes != número de parámetros.")
        updated = []
        for i, (p, g) in enumerate(zip(self.params, grads)):
            if self.momentum > 0:
                self.velocities[i] = _add_elem(
                    _scale(self.velocities[i], self.momentum), g
                )
                update = self.velocities[i]
            else:
                update = g
            updated.append(_sub_elem(p, _scale(update, self.lr)))
        self.params = updated
        self.step_count += 1
        return self.params


class _AdamState:
    def __init__(self, params, lr, beta1, beta2, eps):
        self.params = params
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.m = [_zeros_like(p) for p in params]
        self.v = [_zeros_like(p) for p in params]
        self.t = 0

    def step(self, grads):
        if len(grads) != len(self.params):
            raise TrezRuntimeError("Optimdoz.adam_step: número de gradientes != número de parámetros.")
        self.t += 1
        updated = []
        for i, (p, g) in enumerate(zip(self.params, grads)):
            self.m[i] = _add_elem(_scale(self.m[i], self.beta1), _scale(g, 1 - self.beta1))
            self.v[i] = _add_elem(_scale(self.v[i], self.beta2), _scale(_square(g), 1 - self.beta2))
            m_hat = _scale(self.m[i], 1.0 / (1 - self.beta1 ** self.t))
            v_hat = _scale(self.v[i], 1.0 / (1 - self.beta2 ** self.t))
            denom = _add_elem(_sqrt_elem(v_hat), self.eps)
            update = _div_elem(_scale(m_hat, self.lr), denom)
            updated.append(_sub_elem(p, update))
        self.params = updated
        return self.params


# ---------------------------------------------------------------------------
# API funcional expuesta al visitor de TREZ
# ---------------------------------------------------------------------------

def sgd(params, grads, lr=0.01, momentum=0.0):
    """
    Un paso de SGD sin estado (stateless).
    params:   lista de tensores (listas de números)
    grads:    lista de gradientes con misma forma que params
    lr:       tasa de aprendizaje
    momentum: 0.0 = SGD puro
    Retorna la lista de parámetros actualizados.
    """
    if not isinstance(params, list) or not isinstance(grads, list):
        raise TrezRuntimeError("Optimdoz.sgd: params y grads deben ser listas.")
    updated = []
    for p, g in zip(params, grads):
        updated.append(_sub_elem(p, _scale(g, lr)))
    return updated


def adam(params, grads, m, v, t, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Un paso de Adam sin estado (stateless) — compatible con el estilo funcional de TREZ.
    params: lista de tensores actuales
    grads:  lista de gradientes
    m:      estimador de primer momento (misma forma que params)
    v:      estimador de segundo momento (misma forma que params)
    t:      paso actual (entero, empieza en 1)
    Retorna [params_new, m_new, v_new].
    """
    if not isinstance(params, list) or not isinstance(grads, list):
        raise TrezRuntimeError("Optimdoz.adam: params y grads deben ser listas.")
    m_new, v_new, params_new = [], [], []
    for p, g, mi, vi in zip(params, grads, m, v):
        mi_new = _add_elem(_scale(mi, beta1), _scale(g, 1 - beta1))
        vi_new = _add_elem(_scale(vi, beta2), _scale(_square(g), 1 - beta2))
        m_hat = _scale(mi_new, 1.0 / (1 - beta1 ** t))
        v_hat = _scale(vi_new, 1.0 / (1 - beta2 ** t))
        denom = _add_elem(_sqrt_elem(v_hat), eps)
        p_new = _sub_elem(p, _div_elem(_scale(m_hat, lr), denom))
        params_new.append(p_new)
        m_new.append(mi_new)
        v_new.append(vi_new)
    return [params_new, m_new, v_new]


def zeros_like(data):
    """Crea una estructura de ceros con la misma forma que data."""
    return _zeros_like(data)
