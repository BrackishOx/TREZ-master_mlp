"""
math_utilsdoz — Punto de entrada unificado de la stdlib matemática de TREZ.

Expone al visitor todas las funciones nativas sin dependencias externas:
  - Mathdoz   : álgebra, trascendentales, constantes (core_mathdoz)
  - Tensordoz : producto matricial y transposición (tensor_mathdoz)
  - Activaciones: relu, sigmoid (activationsdoz)
  - Metricsdoz: mse, mse_grad (lossesdoz)

Ninguna función de este módulo llama a numpy, scipy, math ni ninguna
librería externa. Todo el cómputo es Python puro.
"""

from lib.mathdoz.core_mathdoz import (
    PI_DOZ, E_DOZ,
    abs_doz, pow_doz, sqrt_doz, factorial_doz,
    exp_doz, log_doz,
    sin_doz, cos_doz, tan_doz,
)
from lib.mathdoz.tensor_mathdoz import dot, transpose
from lib.activationsdoz.activationsdoz import relu, sigmoid
from lib.lossesdoz.lossdoz import mse, mse_grad

# Constantes accesibles como variables en código TREZ: PI, E
constants = {
    "PI": PI_DOZ,
    "E":  E_DOZ,
}
