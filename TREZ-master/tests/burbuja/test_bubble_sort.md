# Ejercicio: Ordenamiento Burbuja en TREZ

Implementación del **algoritmo de burbuja** (*Bubble Sort*) escrita íntegramente en el lenguaje **TREZ**, adaptada al paradigma funcional del lenguaje: sin mutación de estado, sin asignación por índice, usando únicamente funciones puras y recursión.

---

## 1. Planteamiento del problema

Dado una lista de números `[a₀, a₁, ..., aₙ₋₁]`, ordenarla de menor a mayor.

**Ejemplo:**
```
Entrada:  [5, 3, 8, 1, 9, 2]
Salida:   [1, 2, 3, 5, 8, 9]
```

---

## 2. Algoritmo de burbuja (versión imperativa)

En un lenguaje imperativo, el algoritmo compara pares adyacentes e intercambia si están en orden incorrecto, repitiendo `n-1` veces:

```
para p = 0 hasta n-2 hacer:       ← n-1 pases
    para i = 0 hasta n-2 hacer:
        si lista[i] > lista[i+1]:
            intercambiar lista[i] y lista[i+1]
```

Cada pase empuja el mayor elemento sin ordenar hacia el final. Complejidad: **O(n²)**.

---

## 3. El desafío en TREZ: paradigma funcional

TREZ es un DSL funcional. Esto tiene dos consecuencias directas para este algoritmo:

### 3.1 No existe asignación por índice

En Python o C se haría:
```python
lista[i], lista[i+1] = lista[i+1], lista[i]   # NO existe en TREZ
```

En TREZ **no hay `lista[i] = valor`**. Las listas son inmutables una vez creadas.

### 3.2 Los bucles `for` iteran sobre colecciones, no sobre rangos de índices

TREZ tiene `for item in lista` y `while`, pero el intercambio dentro de un bucle requeriría mutar la lista — lo que no es posible.

---

## 4. Solución funcional adoptada

En lugar de mutar la lista, cada "intercambio" **crea una lista nueva** con el elemento reemplazado. El algoritmo completo se expresa con tres funciones puras y recursión.

### 4.1 `set_idx` — reemplazar un elemento por posición

Reconstruye la lista completa, copiando todos los elementos excepto el de la posición `idx`, que se sustituye por `val`:

```trez
func set_idx(lst, idx, val) {
    func loop(rem, cur, acc) {
        if (len(rem) == 0) { return acc; }
        if (cur == idx) {
            return loop(tail(rem), cur + 1, append(acc, val));
        }
        return loop(tail(rem), cur + 1, append(acc, head(rem)));
    }
    return loop(lst, 0, []);
}
```

**Traza sobre `set_idx([3, 1, 2], 1, 99)`:**

```
loop([3,1,2], 0, [])
  cur=0 ≠ idx=1 → append([], 3)  → loop([1,2], 1, [3])
  cur=1 = idx=1 → append([3], 99) → loop([2],   2, [3,99])
  cur=2 ≠ idx=1 → append([3,99],2)→ loop([],   3, [3,99,2])
  len=0 → return [3, 99, 2]
```

Un intercambio (swap) entre posiciones `i` e `i+1` se hace con dos llamadas a `set_idx`:

```trez
let a    = lst[i];
let b    = lst[i + 1];
let lst2 = set_idx(lst, i, b);      // pone b en posición i
let lst3 = set_idx(lst2, i + 1, a); // pone a en posición i+1
```

### 4.2 `bubble_pass` — un pase completo

Recorre la lista comparando pares adyacentes. Si `lst[pos] > lst[pos+1]`, hace el swap y continúa desde la siguiente posición con la lista nueva. Si no, avanza sin cambiar nada:

```trez
func bubble_pass(lst, pos) {
    let lim = len(lst) - 1;
    if (pos >= lim) { return lst; }
    let a = lst[pos];
    let b = lst[pos + 1];
    if (a > b) {
        let lst2 = set_idx(lst, pos, b);
        let lst3 = set_idx(lst2, pos + 1, a);
        return bubble_pass(lst3, pos + 1);
    }
    return bubble_pass(lst, pos + 1);
}
```

**Traza de `bubble_pass([5, 3, 8, 1], 0)`:**

```
pos=0: a=5, b=3, 5>3 → swap → [3,5,8,1], recurse pos=1
pos=1: a=5, b=8, 5>8 → no swap,           recurse pos=2
pos=2: a=8, b=1, 8>1 → swap → [3,5,1,8], recurse pos=3
pos=3: 3 >= lim=3 → return [3,5,1,8]
```

Resultado del pase: `[3, 5, 1, 8]` — el mayor (8) quedó al final.

### 4.3 `burbuja` — repetir n pases

Aplica `bubble_pass` exactamente `n-1` veces de forma recursiva:

```trez
func burbuja(lst, n) {
    if (n <= 0) { return lst; }
    return burbuja(bubble_pass(lst, 0), n - 1);
}

func ordenar(lst) {
    if (len(lst) <= 1) { return lst; }
    let n = len(lst) - 1;
    return burbuja(lst, n);
}
```

---

## 5. Limitación descubierta del lenguaje (bug documentado)

Durante el desarrollo se encontró un comportamiento importante de TREZ:

**Las expresiones compuestas no funcionan directamente dentro de condiciones `if`.**

```trez
// INCORRECTO — len(lst) - 1 en el if no evalúa bien:
if (pos >= len(lst) - 1) { return lst; }

// CORRECTO — extraer a let primero:
let lim = len(lst) - 1;
if (pos >= lim) { return lst; }
```

Lo mismo aplica para `lst[i]` usado directamente en comparaciones dentro de `if`. La solución siempre es extraer el valor a una variable `let` antes del condicional.

---

## 6. Código completo

```trez
func set_idx(lst, idx, val) {
    func loop(rem, cur, acc) {
        if (len(rem) == 0) { return acc; }
        if (cur == idx) {
            return loop(tail(rem), cur + 1, append(acc, val));
        }
        return loop(tail(rem), cur + 1, append(acc, head(rem)));
    }
    return loop(lst, 0, []);
}

func bubble_pass(lst, pos) {
    let lim = len(lst) - 1;
    if (pos >= lim) { return lst; }
    let a = lst[pos];
    let b = lst[pos + 1];
    if (a > b) {
        let lst2 = set_idx(lst, pos, b);
        let lst3 = set_idx(lst2, pos + 1, a);
        return bubble_pass(lst3, pos + 1);
    }
    return bubble_pass(lst, pos + 1);
}

func burbuja(lst, n) {
    if (n <= 0) { return lst; }
    return burbuja(bubble_pass(lst, 0), n - 1);
}

func ordenar(lst) {
    if (len(lst) <= 1) { return lst; }
    let n = len(lst) - 1;
    return burbuja(lst, n);
}
```

---

## 7. Casos de prueba y resultados

| Entrada | Salida esperada | Descripción |
|---------|----------------|-------------|
| `[5, 3, 8, 1, 9, 2, 7, 4, 6]` | `[1, 2, 3, 4, 5, 6, 7, 8, 9]` | Caso general |
| `[5, 4, 3, 2, 1]` | `[1, 2, 3, 4, 5]` | Lista invertida |
| `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | Ya ordenada |
| `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]` | `[1, 1, 2, 3, 3, 4, 5, 5, 6, 9]` | Con duplicados |
| `[0, -3, 7, -1, 4, -5]` | `[-5, -3, -1, 0, 4, 7]` | Negativos |
| `[42]` | `[42]` | Un elemento |
| `[10, 1]` | `[1, 10]` | Dos elementos |

Ejecutar con:
```bash
cd TREZ/src
python3 main.py ../tests/features/test_bubble_sort.trez
```

---

## 8. Comparación: imperativo vs funcional

| Aspecto | Imperativo (Python/C) | TREZ (funcional) |
|---------|----------------------|-----------------|
| Swap | `a[i], a[i+1] = a[i+1], a[i]` | Dos llamadas a `set_idx()` |
| Bucle interno | `for i in range(n-1)` | Recursión de `bubble_pass` |
| Bucle externo | `for p in range(n-1)` | Recursión de `burbuja` |
| Mutación | Sí (in-place) | No — lista nueva en cada swap |
| Complejidad temporal | O(n²) | O(n²) |
| Complejidad espacial | O(1) | O(n²) — nueva lista en cada paso |

La versión funcional es más costosa en memoria pero refleja el paradigma del lenguaje: **transformaciones puras sin efectos secundarios**.

---

Universidad Sergio Arboleda — Lenguajes de Programación
