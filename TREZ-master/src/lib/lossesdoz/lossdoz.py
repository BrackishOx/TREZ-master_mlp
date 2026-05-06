import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.mathdoz.core_mathdoz import exp_doz, log_doz
from errors import TrezRuntimeError

def mse(y_true, y_pred):
    """Calcula el Error Cuadrático Medio entre dos tensores o listas de números."""
    if isinstance(y_true, list) and isinstance(y_pred, list):
        if len(y_true) != len(y_pred):
            raise TrezRuntimeError("Loss mse() mismatch: Las dimensiones de y_true e y_pred no coinciden.")
        return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)
    elif isinstance(y_true, (int, float)) and isinstance(y_pred, (int, float)):
        return (y_true - y_pred) ** 2
    else:
        raise TrezRuntimeError("Tipos no soportados para mse(). Se requieren números o listas planas.")

def mse_grad(y_true, y_pred):
    """Calcula el gradiente (derivada) del MSE con respecto a y_pred."""
    if isinstance(y_true, list) and isinstance(y_pred, list):
        if len(y_true) != len(y_pred):
            raise TrezRuntimeError("Loss mse_grad() mismatch: Las dimensiones de y_true e y_pred no coinciden.")
        n = len(y_true)
        # La derivada del MSE es 2 * (y_pred - y_true) / N
        return [2 * (p - t) / n for t, p in zip(y_true, y_pred)]
    elif isinstance(y_true, (int, float)) and isinstance(y_pred, (int, float)):
        return 2 * (y_pred - y_true)
    else:
        raise TrezRuntimeError("Tipos no soportados para mse_grad().")


def cross_entropy(logits, targets):
    """
    Entropía cruzada con softmax numericamente estable incorporado.
    logits:  lista de listas (batch x n_clases) — valores crudos de la red
    targets: lista de índices enteros (clase correcta por muestra)
    Retorna el loss promedio como escalar.
    """
    if not isinstance(logits, list) or not logits:
        raise TrezRuntimeError("cross_entropy: logits debe ser lista de listas no vacía.")
    if not isinstance(targets, list) or len(targets) != len(logits):
        raise TrezRuntimeError("cross_entropy: targets debe tener el mismo largo que logits.")

    batch_size = len(logits)
    loss_sum = 0.0
    for i, (row, t) in enumerate(zip(logits, targets)):
        if not isinstance(row, list):
            raise TrezRuntimeError(f"cross_entropy: logits[{i}] debe ser lista de números.")
        if not isinstance(t, int) or t < 0 or t >= len(row):
            raise TrezRuntimeError(f"cross_entropy: target {t} fuera de rango para {len(row)} clases.")
        max_val = max(row)
        shifted = [x - max_val for x in row]
        exp_vals = [exp_doz(x) for x in shifted]
        sum_exp = sum(exp_vals)
        log_softmax_t = shifted[t] - log_doz(sum_exp)
        loss_sum -= log_softmax_t

    return loss_sum / batch_size


def cross_entropy_grad(logits, targets):
    """
    Gradiente de cross_entropy respecto a logits.
    Retorna lista de listas con misma forma que logits.
    grad[i][j] = softmax(logits[i])[j] - 1{j == targets[i]}
    """
    if not isinstance(logits, list) or not logits:
        raise TrezRuntimeError("cross_entropy_grad: logits debe ser lista de listas no vacía.")
    if not isinstance(targets, list) or len(targets) != len(logits):
        raise TrezRuntimeError("cross_entropy_grad: targets debe tener el mismo largo que logits.")

    batch_size = len(logits)
    grads = []
    for i, (row, t) in enumerate(zip(logits, targets)):
        max_val = max(row)
        shifted = [x - max_val for x in row]
        exp_vals = [exp_doz(x) for x in shifted]
        sum_exp = sum(exp_vals)
        softmax = [e / sum_exp for e in exp_vals]
        softmax[t] -= 1.0
        grads.append([g / batch_size for g in softmax])
    return grads
