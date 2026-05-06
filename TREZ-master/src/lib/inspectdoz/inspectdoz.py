"""
Inspectdoz — Depuración no invasiva para pipelines TREZ.

spy(tensor)   : imprime el valor y lo retorna sin modificarlo.
                Ideal para insertar en medio de un |> sin romper el flujo.

shape(tensor) : imprime e imprime las dimensiones del tensor como lista [d1, d2, ...].
                Retorna la lista de dimensiones para que pueda usarse en el pipeline.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TypeMismatchError


def _get_shape(tensor):
    """Calcula las dimensiones de un tensor anidado recursivamente."""
    if not isinstance(tensor, list):
        return []
    if not tensor:
        return [0]
    inner = _get_shape(tensor[0])
    return [len(tensor)] + inner


def spy(tensor):
    """
    Imprime el valor del tensor tal como es y lo retorna intacto.
    Uso: datos |> Inspectdoz.spy |> relu
    """
    print(f"[spy] {tensor}")
    return tensor


def shape(tensor):
    """
    Imprime e imprime las dimensiones del tensor.
    Retorna la lista de dimensiones para que pueda encadenarse.
    Uso: datos |> Inspectdoz.shape |> relu
    """
    if not isinstance(tensor, list):
        raise TypeMismatchError("Inspectdoz.shape", "lista/tensor", type(tensor).__name__)
    dims = _get_shape(tensor)
    print(f"[shape] {dims}")
    return dims
