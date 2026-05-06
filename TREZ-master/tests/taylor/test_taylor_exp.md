# Ejercicio: Polinomio de Taylor para e^x

Implementación del **polinomio de Taylor** que aproxima la función exponencial `e^x`, escrita íntegramente en el lenguaje **TREZ**, sin dependencias externas y validada contra la implementación nativa `exp(x)`.

---

## 1. Planteamiento matemático

La serie de Taylor (centrada en 0, también llamada serie de Maclaurin) para la función exponencial es:

```
e^x = Σ_{n=0}^{∞}  x^n / n!
    = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
```

Truncando la serie en `N` términos obtenemos el **polinomio de Taylor de grado N-1**:

```
e^x ≈ T_N(x) = Σ_{n=0}^{N-1}  x^n / n!
```

El error de aproximación decrece con cada término adicional, tendiendo a cero conforme `N → ∞`.

---

## 2. Algoritmo

```
Entrada: x (real), N (entero positivo)
Salida:  T_N(x) ≈ e^x

suma ← 0
para n = 0 hasta N-1 hacer:
    suma ← suma + x^n / n!
fin
retornar suma
```

---

## 3. Implementación en TREZ

Archivo: [test_taylor_exp.trez](test_taylor_exp.trez)

### 3.1. Función reutilizable

```trez
func taylor_exp(x, N) {
    let suma = 0.0;
    for n in range(N) {
        let suma = suma + (pow(x, n) / factorial(n));
    }
    return suma;
}
```

### 3.2. Ejemplos de uso

```trez
let aprox_1 = taylor_exp(1, 10);    // ≈ 2.7182815...
let aprox_2 = taylor_exp(2, 15);    // ≈ 7.3890560...
let aprox_0 = taylor_exp(0, 5);     // = 1.0 exacto
let aprox_neg = taylor_exp(-1, 12); // ≈ 0.3678794...
```

---

## 4. Características del lenguaje TREZ utilizadas

| Característica | Dónde aparece | Función |
|---|---|---|
| **`func ... return`** | `func taylor_exp(x, N) { ... return suma; }` | Definición de función reutilizable con parámetros |
| **`for ... in range`** | `for n in range(N)` | Bucle iterativo sobre rango entero nativo |
| **`let` con re-asignación** | `let suma = suma + ...` | Acumulador con scope chain ascendente |
| **Operadores aritméticos** | `+`, `*`, `/`, paréntesis | Composición de la fórmula `x^n / n!` |
| **Funciones globales** | `pow`, `factorial`, `exp`, `abs`, `mostrar` | Stdlib matemática y de I/O |
| **Constante predefinida** | `E` | Valor de referencia para validar `taylor_exp(1, ...)` |
| **Namespace** | `Mathdoz.exp(3)` | Llamada con prefijo de módulo |
| **Arrays heterogéneos** | `[k, aprox, err]` | Mezcla `int` + `float` para reportes |

---

## 5. Funciones nativas invocadas

| Función | Implementación interna |
|---|---|
| `pow(x, n)` | Multiplicación iterativa para `n` entero; `e^(n·ln(x))` para `n` real (Newton + Maclaurin) |
| `factorial(n)` | Bucle iterativo `1·2·...·n` con validación de entero positivo |
| `exp(x)` | Serie de Maclaurin con 30 términos (referencia para validar) |
| `abs(x)` | Valor absoluto con vectorización implícita sobre listas |

Todas implementadas en Python puro dentro de [src/lib/mathdoz/core_mathdoz.py](../../src/lib/mathdoz/core_mathdoz.py), **sin importar `math` ni NumPy**.

---

## 6. Resultados experimentales

### 6.1. Casos individuales

| x | N | Taylor | `exp(x)` nativo | Error absoluto |
|---|---|---|---|---|
| 1 | 10 | 2.7182815255731922 | 2.7182818284590455 | 3.03 × 10⁻⁷ |
| 2 | 15 | 7.3890560703259105 | 7.389056098930649 | 2.86 × 10⁻⁸ |
| 0 | 5 | 1.0 | 1.0 | 0 (exacto) |
| -1 | 12 | 0.367879439233606 | 0.3678794411714423 | 1.94 × 10⁻⁹ |
| 3 | 20 | 20.085536921517665 | 20.08553692318766 | 1.67 × 10⁻⁹ |

### 6.2. Convergencia para x = 1 (vs constante `E`)

```
N=1  →  1.0                     error ≈ 1.72
N=2  →  2.0                     error ≈ 0.718
N=3  →  2.5                     error ≈ 0.218
N=4  →  2.6666666666666665      error ≈ 0.052
N=5  →  2.708333333333333       error ≈ 9.9 × 10⁻³
N=6  →  2.7166666666666663      error ≈ 1.6 × 10⁻³
N=7  →  2.7180555555555554      error ≈ 2.3 × 10⁻⁴
N=8  →  2.7182539682539684      error ≈ 2.8 × 10⁻⁵
```

Cada término adicional reduce el error aproximadamente en un orden de magnitud — **convergencia super-lineal** característica del polinomio de Taylor.

---

## 7. Cómo ejecutar

Desde la raíz del proyecto:

```bash
source .venv/bin/activate
python src/main.py tests/features/test_taylor_exp.trez
```

Si aún no tienes el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install antlr4-python3-runtime
```

---

## 8. Análisis y discusión

### Por qué esta implementación es interesante para el lenguaje

1. **Demuestra recursión funcional sin recursión explícita**: el bucle `for + range` reemplaza una recursión que sería natural en otros lenguajes funcionales.
2. **Stress test del scope chain**: el patrón `let suma = suma + ...` dentro del `for` dentro de `func` exige que el `Environment` resuelva correctamente la variable en el scope adecuado (3 niveles: bloque del for → loop_env → call_env de la función).
3. **Composición pura**: `pow(x, n) / factorial(n)` es una expresión libre de efectos secundarios — encaja con el paradigma funcional de TREZ.
4. **Validación cruzada**: comparar `taylor_exp(1, N)` contra la constante predefinida `E` y contra `exp(1)` permite detectar errores tanto en la implementación del usuario como en la stdlib.

### Limitaciones observadas

- Para `|x|` grande la serie de Taylor centrada en 0 converge **lentamente** y pierde precisión por cancelación numérica de términos alternos. Por eso `Mathdoz.exp(x)` internamente reduce el rango antes de evaluar.
- `factorial(n)` crece como `n!`, así que para `N > 20` ya hay riesgo de overflow numérico de Python si se combina con `x^n` grande.
- El bucle `for + range(N)` recalcula `pow(x, n)` y `factorial(n)` desde cero en cada iteración; una versión optimizada actualizaría `term *= x/n` incrementalmente.

---

## 9. Posibles extensiones

- **Generalizar** a cualquier serie de Maclaurin (sin, cos, log, ...) recibiendo el coeficiente como lambda: `\n -> 1 / factorial(n)`.
- **Versión recursiva** usando `if/else` y llamada interna `taylor_exp(x, N-1) + ...`.
- **Optimización incremental** con un solo `let term` actualizado en cada iteración (`term * x / n`).
- **Pipeline funcional** usando el operador `|>` para componer transformaciones.
