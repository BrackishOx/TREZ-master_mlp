import sys
import os
import math

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from lib.mathdoz.core_mathdoz import (
    PI_DOZ, E_DOZ, abs_doz, pow_doz, sqrt_doz, 
    exp_doz, log_doz, sin_doz, cos_doz, tan_doz, factorial_doz
)
from lib.mathdoz.tensor_mathdoz import dot, transpose

def check(name, calculated, expected, is_matrix=False):
    """Verifica explícitamente y muestra los valores calculados vs los esperados."""
    TOLERANCE = 1e-5
    
    if is_matrix:
        passed = (calculated == expected)
    else:
        passed = abs(calculated - expected) < TOLERANCE

    if passed:
        print(f"✅ {name:.<30} OK (Obtenido: {calculated:.4f} | Esperado: {expected:.4f})" if not is_matrix else f"✅ {name:.<30} OK (Coinciden exactamente)")
    else:
        print(f"❌ ERROR EN {name}!")
        print(f"   -> CALCULADO POR TREZ: {calculated}")
        print(f"   -> ORIGINAL ESPERADO:  {expected}")
        sys.exit(1)

def test_core_math():
    print("\n--- TEST: Verificando Algoritmos Matemáticos ('core_mathdoz') ---")
    
    # 1. Constantes
    check("Constante PI", PI_DOZ, math.pi)
    check("Constante E", E_DOZ, math.e)

    # 2. Funciones Algebraicas
    check("Valor Absoluto (-42.5)", abs_doz(-42.5), 42.5)
    check("Potencia pow(2, 8)", pow_doz(2, 8), 256.0)
    check("Factorial (5!)", factorial_doz(5), 120)
    
    # Pruebas Numéricas (Newton-Raphson)
    check("Raíz sqrt(16)", sqrt_doz(16), 4.0)
    check("Raíz sqrt(2)", sqrt_doz(2), math.sqrt(2))

    # 3. Trascendentales (Maclaurin y Mercator)
    check("Exponencial exp(5)", exp_doz(5), math.exp(5))
    check("Logaritmo Nat. log(10)", log_doz(10), math.log(10))

    # Trigonometría (Series de Taylor)
    check("Seno sin(PI/2)", sin_doz(PI_DOZ / 2), 1.0)
    check("Seno sin(PI)", sin_doz(PI_DOZ), 0.0)
    check("Coseno cos(PI)", cos_doz(PI_DOZ), -1.0)
    check("Tangente tan(PI/4)", tan_doz(PI_DOZ / 4), 1.0)

def test_tensor_math():
    print("\n--- TEST: Verificando Tensores ('tensor_mathdoz') ---")
    
    vec1, vec2 = [1, 2, 3], [4, 5, 6]
    check("Producto Punto Vectores", dot(vec1, vec2), 32) # 1*4 + 2*5 + 3*6 = 32

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 0], [1, 2]]
    expected_mat = [[4, 4], [10, 8]]
    check("Multiplicación Matrices", dot(mat1, mat2), expected_mat, is_matrix=True)

    m = [[1, 2, 3], [4, 5, 6]]
    expected_t = [[1, 4], [2, 5], [3, 6]]
    check("Transposición Matrices", transpose(m), expected_t, is_matrix=True)

if __name__ == "__main__":
    test_core_math()
    test_tensor_math()
    print("\n🎉 ¡TODAS las pruebas matemáticas pasaron con exactitud nivel C/Python!\n")
