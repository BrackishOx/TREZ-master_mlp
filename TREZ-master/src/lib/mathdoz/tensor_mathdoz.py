import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TrezRuntimeError, ShapeMismatchError, TypeMismatchError


def _shape(t):
    """Retorna la forma de un tensor como string '[fxc]' para mensajes de error."""
    if isinstance(t, list) and t and isinstance(t[0], list):
        return f"[{len(t)}x{len(t[0])}]"
    if isinstance(t, list):
        return f"[{len(t)}]"
    return "escalar"


def dot(a, b):
    """
    Producto punto / multiplicación matricial nativa.
      escalar × escalar  → escalar
      vector  · vector   → escalar  (producto punto)
      matriz  × matriz   → matriz   (multiplicación matricial)
      matriz  × vector   → vector
    """
    # Escalar × escalar
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeMismatchError("dot", "lista o número", type(a).__name__)

    if not a or not b:
        raise TrezRuntimeError("dot() no acepta tensores vacíos.")

    a_is_vec = isinstance(a[0], (int, float))
    b_is_vec = isinstance(b[0], (int, float))
    a_is_mat = isinstance(a[0], list)
    b_is_mat = isinstance(b[0], list)

    # Vector · vector → escalar
    if a_is_vec and b_is_vec:
        if len(a) != len(b):
            raise ShapeMismatchError("dot", _shape(a), _shape(b))
        result = 0.0
        for x, y in zip(a, b):
            result += x * y
        return result

    # Matriz × matriz → matriz
    if a_is_mat and b_is_mat:
        cols_a = len(a[0])
        rows_b = len(b)
        if cols_a != rows_b:
            raise ShapeMismatchError("dot", _shape(a), _shape(b))
        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                val = 0.0
                for k in range(rows_b):
                    val += a[i][k] * b[k][j]
                row.append(val)
            result.append(row)
        return result

    # Matriz × vector → vector
    if a_is_mat and b_is_vec:
        if len(a[0]) != len(b):
            raise ShapeMismatchError("dot", _shape(a), _shape(b))
        return [dot(row, b) for row in a]

    raise TypeMismatchError("dot", "vector o matriz", f"{_shape(a)} y {_shape(b)}")


def transpose(m):
    """Transpone una matriz 2D. Retorna una nueva matriz."""
    if not isinstance(m, list) or not m:
        raise TypeMismatchError("transpose", "matriz 2D", type(m).__name__)
    if not isinstance(m[0], list):
        raise TypeMismatchError("transpose", "matriz 2D (lista de listas)", "vector 1D")
    rows, cols = len(m), len(m[0])
    return [[m[r][c] for r in range(rows)] for c in range(cols)]
