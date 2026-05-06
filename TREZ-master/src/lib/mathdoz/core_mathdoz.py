import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TrezRuntimeError, MathDomainError, TypeMismatchError

# === Constantes Matemáticas Nativas ===
PI_DOZ = 3.14159265358979323846
E_DOZ  = 2.71828182845904523536


# === Funciones Algebraicas ===

def abs_doz(x):
    """Valor absoluto. Aplica elemento a elemento sobre listas."""
    if isinstance(x, (int, float)):
        return x if x >= 0 else -x
    if isinstance(x, list):
        return [abs_doz(i) for i in x]
    raise TypeMismatchError("abs", "número o lista", type(x).__name__)


def pow_doz(base, exp):
    """
    Potencia real base^exp sin dependencias externas.
    - exp entero: producto iterativo (exacto).
    - exp flotante: e^(exp * ln(base)).
    """
    if isinstance(base, list):
        return [pow_doz(b, exp) for b in base]
    if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
        raise TypeMismatchError("pow", "números", f"{type(base).__name__}, {type(exp).__name__}")
    if isinstance(exp, int) or (isinstance(exp, float) and exp.is_integer()):
        exp = int(exp)
        if exp == 0:
            return 1.0
        if exp < 0:
            return 1.0 / pow_doz(base, -exp)
        res = 1.0
        for _ in range(exp):
            res *= base
        return res
    # Exponente flotante: base^exp = e^(exp·ln(base))
    if base <= 0:
        raise MathDomainError("pow", f"base={base} con exponente no entero")
    return exp_doz(exp * log_doz(base))


def factorial_doz(n):
    """n! iterativo. Acepta enteros o flotantes enteros (ej. 5.0)."""
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if not isinstance(n, int) or n < 0:
        raise MathDomainError("factorial", n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sqrt_doz(x):
    """
    Raíz cuadrada mediante el Método de Newton-Raphson.
    Converge en ~20 iteraciones para doble precisión.
    """
    if isinstance(x, list):
        return [sqrt_doz(i) for i in x]
    if not isinstance(x, (int, float)):
        raise TypeMismatchError("sqrt", "número", type(x).__name__)
    if x < 0:
        raise MathDomainError("sqrt", x)
    if x == 0:
        return 0.0
    guess = x / 2.0
    for _ in range(20):
        guess = 0.5 * (guess + x / guess)
    return guess


# === Funciones Trascendentales ===

def exp_doz(x, terms=30):
    """
    e^x mediante la Serie de Maclaurin: sum_{k=0}^{n} x^k / k!
    Para x < 0 usa la identidad e^x = 1 / e^(-x).
    """
    if isinstance(x, list):
        return [exp_doz(i) for i in x]
    if not isinstance(x, (int, float)):
        raise TypeMismatchError("exp", "número", type(x).__name__)
    if x < 0:
        return 1.0 / exp_doz(-x, terms)
    result = 1.0
    term = 1.0
    for i in range(1, terms):
        term *= x / i
        result += term
        if term < 1e-15:
            break
    return result


def log_doz(x, terms=50):
    """
    Logaritmo natural ln(x).
    Reduce el argumento al intervalo [1/e, e] sumando enteros de ln(e)=1,
    luego aplica la serie de Leibniz:
      ln(x) = 2 * sum_{n=0}^{inf} (1/(2n+1)) * ((x-1)/(x+1))^(2n+1)
    """
    if isinstance(x, list):
        return [log_doz(i) for i in x]
    if not isinstance(x, (int, float)):
        raise TypeMismatchError("log", "número", type(x).__name__)
    if x <= 0:
        raise MathDomainError("log", x)
    exponent = 0.0
    while x >= E_DOZ:
        x /= E_DOZ
        exponent += 1.0
    while x <= 1.0 / E_DOZ:
        x *= E_DOZ
        exponent -= 1.0
    y = (x - 1.0) / (x + 1.0)
    y2 = y * y
    result = 0.0
    term = y
    for n in range(1, terms * 2, 2):
        result += term / n
        term *= y2
    return 2.0 * result + exponent


def sin_doz(x, terms=20):
    """
    Seno en radianes mediante Serie de Taylor.
    Reduce x al intervalo [-π, π] antes de aplicar la serie.
    """
    if isinstance(x, list):
        return [sin_doz(i) for i in x]
    if not isinstance(x, (int, float)):
        raise TypeMismatchError("sin", "número", type(x).__name__)
    x = x % (2 * PI_DOZ)
    if x > PI_DOZ:
        x -= 2 * PI_DOZ
    result = 0.0
    sign = 1
    for n in range(terms):
        result += sign * pow_doz(x, 2 * n + 1) / factorial_doz(2 * n + 1)
        sign *= -1
    return result


def cos_doz(x, terms=20):
    """
    Coseno en radianes mediante Serie de Taylor.
    Reduce x al intervalo [-π, π] antes de aplicar la serie.
    """
    if isinstance(x, list):
        return [cos_doz(i) for i in x]
    if not isinstance(x, (int, float)):
        raise TypeMismatchError("cos", "número", type(x).__name__)
    x = x % (2 * PI_DOZ)
    if x > PI_DOZ:
        x -= 2 * PI_DOZ
    result = 0.0
    sign = 1
    for n in range(terms):
        result += sign * pow_doz(x, 2 * n) / factorial_doz(2 * n)
        sign *= -1
    return result


def tan_doz(x):
    """Tangente: sin(x) / cos(x). Lanza error en asintotas ±π/2."""
    if isinstance(x, list):
        return [tan_doz(i) for i in x]
    cosine = cos_doz(x)
    if abs_doz(cosine) < 1e-10:
        raise MathDomainError("tan", f"{x} (asíntota)")
    return sin_doz(x) / cosine
