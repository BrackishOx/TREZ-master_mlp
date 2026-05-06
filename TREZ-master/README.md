# TREZ Language

**TREZ** es un Lenguaje de Dominio Específico (DSL) funcional diseñado para la definición, entrenamiento y evaluación de modelos de Deep Learning, construido completamente desde cero — cero dependencias a NumPy, PyTorch o cualquier librería de álgebra lineal externa.

El lenguaje adopta un **paradigma estrictamente funcional** donde las transformaciones de datos se expresan mediante composición de funciones y el operador pipe `|>`. El sistema de compilación usa **ANTLR4** para análisis léxico/sintáctico y un intérprete **Python** que implementa el patrón **Visitor** sobre el AST generado.

---

## Caracteristicas Principales

- **Cero dependencias externas:** Motor matemático, tensores, funciones de activación, backpropagation y estructuras de datos implementados en Python puro.
- **Paradigma funcional:** Bindings inmutables (`let`), funciones puras, closures con recursión, lambdas anonimas (`\x -> expr`).
- **Patron Visitor:** `TrezVisitor` recorre el AST nodo a nodo. Cada construcción del lenguaje tiene su `visitX()` correspondiente.
- **Operador pipe `|>`:** Encadena transformaciones: `datos |> normalizar |> relu` equivale a `relu(normalizar(datos))`.
- **Namespaces:** La stdlib se invoca como `Tensordoz.dot(A, B)`, `Mathdoz.relu(x)`, `Metricsdoz.mse(Y, Yp)`.
- **Construido con ANTLR4:** Gramatica Tipo 2 (Libre de Contexto) compilada a Python.

---

## Requisitos

- Python >= 3.10
- antlr4-python3-runtime == 4.13.2  (`pip install antlr4-python3-runtime==4.13.2`)
- Java JRE/JDK (solo para regenerar el parser desde las gramáticas `.g4`)

---

## Uso

```bash
cd src
python3 main.py <archivo.trez>
```

---

## Sintaxis Rapida

```trez
// Variables (bindings inmutables)
let lr = 0.01;
let pesos = [0.5, 0.3, 0.1];
let matriz = [[1, 2], [3, 4]];

// Funciones con recursión
func factorial(n) {
    if (n <= 1) { return 1; }
    return n * factorial(n - 1);
}
mostrar(factorial(6));   // 720

// Lambda anónima
let doble = \x -> x * 2;

// Operador pipe
let resultado = [1, 2, 3] |> relu |> sigmoid;

// Namespace de módulo
let salida = Tensordoz.dot(W, X);
let error  = Metricsdoz.mse(Y_real, Y_pred);

// Desestructuración de tupla
let [W1, b1] = DLdoz.init_dense(4, 16);

// Condicionales encadenados
func clasificar(x) {
    if (x < 0)      { return "negativo"; }
    else if (x == 0){ return "cero"; }
    else            { return "positivo"; }
}

// Bucles
for i in range(10) { mostrar(i); }
while (cond) { ... }

// Estructuras de datos
let q = Queue();
let q = q.enqueue(42);

let s = Stack();
let s = s.push(10);

let d = {nombre: "TREZ", version: 2};
mostrar(d["nombre"]);
```

---

## Librería Estándar Nativa

Todos los módulos están implementados en Python puro — ninguna función llama a librería externa.

| Módulo | Funciones disponibles | Estado |
|---|---|---|
| `Mathdoz` / global | `relu`, `sigmoid`, `exp`, `log`, `sin`, `cos`, `tan`, `sqrt`, `pow`, `abs`, `factorial`; constantes `PI`, `E` | ✅ |
| `Tensordoz` | `dot`, `transpose` *(reshape, flatten, add, concat — E3)* | ✅ parcial |
| `Activationsdoz` | `relu`, `sigmoid` (elemento a elemento) | ✅ |
| `Metricsdoz` | `mse`, `mse_grad` *(cross_entropy, accuracy, rmse — E3)* | ✅ parcial |
| `IOdoz` | `leer`, `escribir` | ✅ |
| `Datadoz` | `from_lists`, `make_loader`, `get_batches`, `train_test_split`, `read_csv`, `read_xlsx`, `columna`, `fila`, `num_filas`, `num_columnas`, `columnas` | ✅ |
| `Plotdoz` | `learning_curve`, `histogram`, `bar_chart`, `scatter`, `line_chart` | ✅ |
| `Inspectdoz` | `spy`, `shape` | ✅ |
| `Structsdoz` | `Queue`, `Stack` | ✅ |
| `Optimdoz` | SGD, Adam | ✅ |

---

## Estructura del Proyecto

```
TREZ/
├── README.md
├── Design.md
├── src/
│   ├── main.py                  # Punto de entrada del intérprete
│   ├── visitor.py               # Patron Visitor — evaluación del AST
│   ├── math_utilsdoz.py         # Re-exporta la stdlib al visitor
│   ├── autograd.py              # Grafo computacional + backprop nativo
│   ├── errors.py                # TrezError, TrezSyntaxError, TrezRuntimeError
│   ├── error_listener.py        # TrezErrorListener para ANTLR4
│   ├── parser/
│   │   ├── TrezLexer.g4         # Gramática léxica
│   │   ├── TrezParser.g4        # Gramática sintáctica (CFG Tipo 2)
│   │   ├── TrezLexer.py         # Generado por ANTLR4
│   │   ├── TrezParser.py        # Generado por ANTLR4
│   │   └── TrezParserVisitor.py # Generado por ANTLR4
│   └── lib/
│       ├── mathdoz/             # core_mathdoz.py + tensor_mathdoz.py
│       ├── activationsdoz/      # relu, sigmoid
│       ├── lossesdoz/           # mse, mse_grad, cross_entropy
│       ├── optimdoz/            # sgd, adam, zeros_like
│       ├── nndoz/               # linear_init/forward/backward, relu, softmax
│       ├── datadoz/             # from_lists, loader, read_csv, read_xlsx, columna, fila
│       ├── plotdoz/             # learning_curve, histogram, bar_chart, scatter, line_chart
│       ├── iodoz/               # leer, escribir
│       ├── inspectdoz/          # spy, shape
│       └── structsdoz/          # Queue, Stack
└── tests/
    ├── features/
    │   ├── test_basic.trez
    │   ├── test_math.trez
    │   ├── test_dl.trez
    │   ├── test_backprop.trez
    │   ├── test_io.trez
    │   └── test_new_features.trez   # func, for, dict, Queue, Stack, lambda
    ├── runtime/
    │   └── test_runtime_error.trez
    └── syntax/
        └── test_syntax_error.trez
```

---

## Estado de Entregas

| Entrega | Objetivo | Estado |
|---|---|---|
| Entrega 1 | Aritmetica basica, arrays, variables, funciones nativas, errores | ✅ Completa |
| Entrega 2 | Pipe `\|>`, lambdas `\x ->`, namespaces `Modulo.func()`, `let [a,b] = expr`, `Inspectdoz`, funciones, closures, recursion, condicionales, bucles, dicts, Queue, Stack | ✅ Completa |
| **Entrega 3** | `Tensordoz` completo (reshape/flatten/add/concat), `Optimdoz` (SGD/Adam), `Metricsdoz` completo, `Datadoz.read_csv`, `Datadoz.read_xlsx`, `Plotdoz` completo | **✅ Completa** |
| Entrega 4 | MLP entrenable en TREZ + suite con dataset CSV real | Pendiente |
| Entrega Final | Autoencoder + `Plotdoz.learning_curve` + documentación completa | Pendiente |

---

Universidad Sergio Arboleda
