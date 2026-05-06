# Algoritmo de Euclides en TREZ

## ¿Qué es el Algoritmo de Euclides?

El algoritmo de Euclides calcula el **Máximo Común Divisor (MCD)** de dos números enteros. Se basa en la propiedad:

```
mcd(a, 0) = a
mcd(a, b) = mcd(b, a % b)
```

Es decir, el MCD de `a` y `b` es el mismo que el MCD de `b` y el residuo de `a / b`. Se repite el proceso hasta que el residuo sea `0`.

**Ejemplo paso a paso** con `mcd(48, 18)`:

| Paso | a   | b   | a % b |
|------|-----|-----|-------|
| 1    | 48  | 18  | 12    |
| 2    | 18  | 12  | 6     |
| 3    | 12  | 6   | 0     |
| 4    | 6   | 0   | —     |

Resultado: **MCD = 6**

---

## Implementación Recursiva

La versión recursiva traduce directamente la definición matemática del algoritmo.

```trez
func mcd_recursivo(a, b) {
    if (b == 0) { return a; }
    return mcd_recursivo(b, a % b);
}
```

**Cómo funciona:**

- **Caso base:** si `b == 0`, retorna `a` (el MCD encontrado).
- **Caso recursivo:** llama a sí misma con `(b, a % b)`, reduciendo el problema en cada llamada.
- Usa el operador `%` (módulo) nativo de TREZ.

**Traza de `mcd_recursivo(48, 18)`:**

```
mcd_recursivo(48, 18)
  → mcd_recursivo(18, 12)
      → mcd_recursivo(12, 6)
          → mcd_recursivo(6, 0)
              → return 6
```

---

## Implementación Iterativa

La versión iterativa reemplaza la recursión con un ciclo `while`, evitando el uso de la pila de llamadas.

```trez
func mcd_iterativo(a, b) {
    while (b != 0) {
        let temp = b;
        let b = a % b;
        let a = temp;
    }
    return a;
}
```

**Cómo funciona:**

- En cada iteración del `while`, se actualizan `a` y `b` usando una variable temporal `temp`.
- El ciclo termina cuando `b` llega a `0`.
- En ese punto, `a` contiene el MCD.

**Traza de `mcd_iterativo(48, 18)`:**

| Iteración | a  | b  | temp |
|-----------|----|----|------|
| 1         | 48 | 18 | 18   |
| 2         | 18 | 12 | 12   |
| 3         | 12 | 6  | 6    |
| 4         | 6  | 0  | —    |

Resultado: **MCD = 6**

---

## Comparación entre versiones

| Aspecto           | Recursiva                        | Iterativa                        |
|-------------------|----------------------------------|----------------------------------|
| Legibilidad       | Muy cercana a la definición matemática | Más explícita en los pasos      |
| Uso de pila       | Usa la pila de llamadas          | No usa pila extra                |
| Caso base         | `if (b == 0) return a`           | Condición del `while (b != 0)`   |
| Riesgo de overflow| En entradas muy grandes          | Ninguno                          |
| Rendimiento       | Similar en la práctica           | Ligeramente más eficiente        |

---

## Aplicación: Mínimo Común Múltiplo (MCM)

Usando el MCD se puede calcular el MCM con la fórmula:

```
mcm(a, b) = (a × b) / mcd(a, b)
```

Implementado en TREZ:

```trez
func mcm(a, b) {
    return (a * b) / mcd_recursivo(a, b);
}
```

---

## Casos de prueba

Los tests cubren los siguientes escenarios:

| Entrada        | MCD esperado | Caso que cubre               |
|----------------|--------------|------------------------------|
| `(48, 18)`     | 6            | Caso típico                  |
| `(100, 75)`    | 25           | Múltiplo exacto              |
| `(17, 5)`      | 1            | Números coprimos             |
| `(0, 7)`       | 7            | Un argumento es cero         |
| `(7, 0)`       | 7            | Caso base directo            |
| `(12, 12)`     | 12           | Números iguales              |
| `(1071, 462)`  | 21           | Números grandes              |

---

## Archivo de prueba

El test completo se encuentra en:

```
tests/features/test_euclides.trez
```

Para ejecutarlo:

```bash
# Solo el test de Euclides
cd TREZ-master/src
python3 main.py ../tests/features/test_euclides.trez

# Suite completa
cd TREZ-master
python3 tests/run_tests.py
```
