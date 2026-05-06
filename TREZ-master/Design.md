# Arquitectura y Diseño de TREZ

**TREZ** — Lenguaje de Dominio Específico Funcional para Deep Learning
Universidad Sergio Arboleda

---

## 1. Visión General

TREZ es un DSL estrictamente funcional orientado a la definición, entrenamiento y evaluación de modelos de Deep Learning, construido desde cero sin dependencias externas para el cómputo numérico. Cada expresión es una función; no existen variables mutables ni bucles imperativos en el núcleo del lenguaje. El entrenamiento de una red neuronal se expresa como una cadena de transformaciones funcionales puras encadenadas con `|>`.

**Principio de diseño central:** En TREZ, `A |> f` equivale a `f(A)`. Un pipeline de inferencia completo es una composición declarativa de funciones sin efectos secundarios.

---

## 2. Arquitectura del Sistema

El compilador e intérprete de TREZ opera en dos niveles:

```
Script .trez
    │
    ▼
 [Lexer]  ← TrezLexer.g4  (ANTLR4)
    │
    ▼
 [Parser] ← TrezParser.g4 (ANTLR4, CFG Tipo 2)
    │
    ▼
   AST (Parse Tree)
    │
    ▼
 [Visitor] ← TrezVisitor (Python, patrón Visitor)
    │         Entorno: Environment (scopes encadenados)
    ▼
 [Stdlib nativa] ← mathdoz, tensordoz, metricsdoz, iodoz, structsdoz...
    │
    ▼
 Resultado
```

### 2.1 Front-end — Análisis Léxico y Sintáctico (ANTLR4)

- **Lexer (`TrezLexer.g4`):** Segmenta el flujo de caracteres en tokens: `ID`, `NUMBER`, `STRING`, keywords (`let`, `func`, `return`, `if`, `else`, `while`, `for`, `in`, `not`), operadores (`**`, `&&`, `||`, `|>`, `->`, `==`, `!=`, `<=`, `>=`), separadores y literales.
- **Parser (`TrezParser.g4`):** Aplica la gramática CFG Tipo 2 (Chomsky) para construir el Parse Tree. ANTLR4 genera automáticamente `TrezParser.py` y `TrezParserVisitor.py`.

### 2.2 Back-end — Motor de Evaluación (Python)

El `TrezVisitor` extiende `TrezParserVisitor` (generado por ANTLR4) e implementa un `visitX()` para cada regla de la gramática. El entorno de ejecución (`Environment`) es una cadena de scopes enlazados que implementa lookup funcional: cada bloque/función crea un nuevo scope hijo, y `let` actualiza el binding más cercano en la cadena via `update()`.

---

## 3. Decisiones de Diseño

### 3.1 Paradigma Funcional

- Bindings con `let`: inmutables en intención; `update()` sube la cadena de scopes para simular reasignación controlada dentro de loops.
- Funciones como closures (`TrezFunction`): capturan el `Environment` de definición, permiten recursión (self-reference inyectado en el call env).
- Lambdas anónimas (`\x -> expr`): funciones de primer orden pasables como argumentos y al operador `|>`.
- Sin side-effects en la stdlib: todas las funciones de `lib/` retornan nuevos valores, nunca mutan en lugar.

### 3.2 Patrón Visitor

Cada nodo del AST tiene un `visitNodo()` correspondiente en `TrezVisitor`. La evaluación es puramente recursiva: visitar un nodo dispara la visita de sus hijos, compone los resultados y retorna un valor inmutable. No hay tablas de símbolos globales mutables — el estado vive en el `Environment` encadenado.

### 3.3 Cero Librerías Externas (para cómputo)

| Necesidad | Implementación nativa |
|---|---|
| Constantes PI, E | Literales de 20 dígitos en `core_mathdoz.py` |
| `exp(x)` | Serie de Maclaurin (30 términos) |
| `log(x)` | Serie de Mercator + reducción de rango por E |
| `sin(x)`, `cos(x)` | Serie de Taylor (20 términos) + reducción de periodo |
| `sqrt(x)` | Método de Newton-Raphson (20 iteraciones) |
| `pow(base, exp)` | Producto iterativo (enteros) / `exp(n·log(base))` (floats) |
| Producto matricial | Triple bucle nativo en `tensor_mathdoz.py` |
| Transpose | Lista de comprensión 2D |
| ReLU, Sigmoid | Definiciones elementales sobre `exp_doz` |
| MSE, MSE_grad | Definiciones analíticas directas |
| Queue, Stack | Listas Python puras con semántica inmutable en `structsdoz.py` |
| Backprop | Grafo computacional con topological sort en `autograd.py` |

La única dependencia externa real es `antlr4-python3-runtime` — el motor del parser/lexer, estructural e inevitable.

### 3.4 Operador Pipe `|>`

`A |> f` evalúa `f(A)`. `A |> f |> g` evalúa `g(f(A))`. Tiene la menor precedencia de todos los operadores, garantizando que `a + b |> f` se evalúa como `f(a + b)`.

Con lambdas: `datos |> \x -> Tensordoz.dot(W, x) |> Mathdoz.relu` es un forward pass de una capa.

### 3.5 Namespaces de Módulo

La stdlib se invoca como `Modulo.funcion(args)` para hacer explícito el origen de cada operación y evitar colisiones de nombres. El visitor resuelve `Tensordoz.dot(A, B)` despachando a `tensor_mathdoz.dot(A, B)`.

---

## 4. Gramática (CFG Tipo 2 — ANTLR4)

### 4.1 Estado Actual — Entregas 1 y 2 (Completas)

```antlr
// TrezLexer.g4
LET: 'let';  FUNC: 'func';  RETURN: 'return';
IF: 'if';    ELSE: 'else';  WHILE: 'while';
FOR: 'for';  IN: 'in';      NOT: 'not';
POW: '**';   AND: '&&';     OR: '||';
PIPE: '|>';  ARROW: '->';   BACKSLASH: '\\';
EQEQ: '==';  NEQ: '!=';    LE: '<=';  GE: '>=';
DOT: '.';    COLON: ':';   MOD: '%';
// ... NUMBER, STRING, ID, WS, LINE_COMMENT

// TrezParser.g4
program    : statement+ EOF;
statement  : let_stmt | bind_tuple | func_def | return_stmt
           | expr_stmt | if_stmt | while_stmt | for_stmt | block;

let_stmt   : LET ID EQ expr SEMI;
bind_tuple : LET LBRACK ID (COMMA ID)* RBRACK EQ expr SEMI;
func_def   : FUNC ID LPAREN param_list? RPAREN block;
return_stmt: RETURN expr SEMI;
for_stmt   : FOR ID IN expr block;
if_stmt    : IF LPAREN expr RPAREN block (ELSE (if_stmt | block))?;

expr (menor a mayor precedencia):
    lambdaDef   : BACKSLASH ID ARROW expr
    pipeOp      : expr PIPE expr
    orExpr      : expr OR expr
    andExpr     : expr AND expr
    notExpr     : NOT expr
    eqExpr      : expr (EQEQ | NEQ) expr
    compareExpr : expr (LT | LE | GT | GE) expr
    mulDivExpr  : expr (MUL | DIV | MOD) expr
    addSubExpr  : expr (PLUS | MINUS) expr
    powExpr     : expr POW expr
    unaryMinus  : MINUS expr
    indexExpr   : expr LBRACK expr RBRACK
    moduleCall  : ID DOT ID LPAREN args? RPAREN
    methodCall  : expr DOT ID LPAREN args? RPAREN
    funcCall    : ID LPAREN args? RPAREN
    // ... literals, arrays, dicts
```

### 4.2 Precedencia de Operadores (mayor prioridad abajo)

| Nivel | Operador | Asociatividad |
|---|---|---|
| 1 (menor) | `\x ->` lambda | derecha |
| 2 | `\|>` pipe | izquierda |
| 3 | `\|\|` | izquierda |
| 4 | `&&` | izquierda |
| 5 | `not` | prefijo |
| 6 | `==`, `!=` | izquierda |
| 7 | `<`, `<=`, `>`, `>=` | izquierda |
| 8 | `+`, `-` | izquierda |
| 9 | `*`, `/`, `%` | izquierda |
| 10 | `**` | derecha |
| 11 | `-` unario | prefijo |
| 12 (mayor) | `[]`, `.método()` | izquierda |

---

## 5. Librería Estándar Nativa

### 5.1 Mathdoz / core_mathdoz.py

Constantes: `PI`, `E`.
Funciones: `abs`, `pow`, `factorial`, `sqrt` (Newton-Raphson), `exp` (Maclaurin), `log` (Mercator), `sin`, `cos`, `tan` (Taylor).

### 5.2 Tensordoz / tensor_mathdoz.py

Implementado: `dot` (producto matricial, vectorial y escalar), `transpose`.
Entrega 3: `reshape`, `flatten`, `add` (con broadcasting), `concat`, `mul_scalar`.

### 5.3 Activationsdoz / activationsdoz.py

`relu(x)`, `sigmoid(x)` — elemento a elemento, con `exp_doz` propio.
Entrega 3: `softmax(x)`, `tanh(x)`.

### 5.4 Metricsdoz / lossesdoz/lossdoz.py

Implementado: `mse(Y, Yp)`, `mse_grad(Y, Yp)`.
Entrega 3: `cross_entropy`, `accuracy`, `rmse`, `r2_score`.

### 5.5 IOdoz / iodoz/iodoz.py

Implementado: `leer(ruta)`, `escribir(ruta, contenido)`.
Entrega 3: `read_csv(ruta)` → lista de listas numéricas (tensor).

### 5.6 Structsdoz / structsdoz/structsdoz.py

`TrezQueue` (FIFO) y `TrezStack` (LIFO) — listas Python puras, API inmutable (`enqueue`/`dequeue`, `push`/`pop` retornan nuevas instancias).

### 5.7 Inspectdoz (Entrega 2)

`spy(tensor)` — imprime el tensor y lo retorna sin modificarlo (no-op en pipelines).
`shape(tensor)` — imprime las dimensiones `[filas, cols, ...]` y retorna la lista de dimensiones.

### 5.8 Optimdoz (Entrega 3)

`sgd(W, grad, lr)` → `W - lr * grad`.
`adam(W, grad, m, v, t, lr)` → actualización con estimadores de primer y segundo momento.

### 5.9 Plotdoz (Entrega Final)

`learning_curve(epochs, loss_t, loss_v)` — curva de convergencia en texto ASCII.
`histogram(X, bins)`, `boxplot(X)`, `correlation_heatmap(X)`.

---

## 6. Sistema de Errores

```
TrezError (base)
├── TrezSyntaxError      — detectado por TrezErrorListener en ANTLR4
│                          incluye línea, columna y token inesperado
├── TrezRuntimeError     — detectado por TrezVisitor en evaluación
│                          cubre: variable no definida, dimensión incompatible,
│                          división por cero, índice fuera de rango, IO
├── UndefinedSymbolError — (Entrega 2) reemplaza el caso "variable no definida"
│                          con información del símbolo y el entorno actual
├── ShapeMismatchError   — (Entrega 3) para incompatibilidades dimensionales en dot/add
└── MathDomainError      — (Entrega 3) para log(0), sqrt(-1)
```

---

## 7. Hoja de Ruta

### Entrega 1 — Completa

- [x] Gramática ANTLR4: aritmética, arrays recursivos 1D/2D/3D, `let`, funciones nativas globales
- [x] Visitor: `TrezVisitor` + entorno, aritmética vectorial, jerarquía de errores
- [x] Stdlib: `Mathdoz` completo, `Tensordoz` (dot+transpose), `Metricsdoz` (mse+mse_grad), `IOdoz` (leer/escribir)
- [x] `autograd.py` adelantado: grafo computacional + backprop topológico

### Entrega 2 — Completa

- [x] Funciones con nombre (`func`/`return`), recursión, closures
- [x] Condicionales encadenados (`else if`), `for..in`, `not`, `while`
- [x] Diccionarios, acceso por índice `[]`, métodos `.metodo()`
- [x] `Queue` y `Stack` nativos (`structsdoz`)
- [x] `range()`, `len()`, `append()`, `head()`, `tail()`, `str()`, `num()`
- [x] Operador pipe `|>` (`visitPipeOp` en `visitor.py`)
- [x] Lambdas anónimas `\x -> expr` (`visitLambdaDef` + `TrezLambda`)
- [x] Namespaces `Modulo.func()` (`visitMethodCallExpr` + `_NAMESPACES`)
- [x] Desestructuración de tuplas `let [a, b] = expr` (`visitBind_tuple`)
- [x] `Inspectdoz`: `spy()`, `shape()`
- [x] `UndefinedSymbolError` diferenciado

### Entrega 3

- [ ] `Tensordoz`: `reshape`, `flatten`, `add` (broadcasting), `concat`, `mul_scalar`
- [ ] `Activationsdoz`: `softmax`, `tanh`, `sigmoid_deriv`, `relu_deriv`
- [ ] `Optimdoz`: `sgd`, `adam`
- [ ] `Metricsdoz`: `cross_entropy`, `accuracy`, `rmse`, `r2_score`
- [ ] `IOdoz.read_csv` → tensor
- [ ] `ShapeMismatchError`, `MathDomainError`

### Entrega 4

- [ ] MLP multicapa entrenable en TREZ (forward + backward + update en sintaxis nativa)
- [ ] Suite de pruebas con dataset CSV real (Iris o similar)

### Entrega Final

- [ ] Autoencoder (encoder + decoder encadenados con `|>`)
- [ ] `Plotdoz`: `learning_curve` en ASCII, histograma, boxplot
- [ ] Documentación completa + ejemplos ejecutables

---

## 8. Estructura del Proyecto

```
TREZ/
├── README.md
├── Design.md                        (este archivo)
├── src/
│   ├── main.py                      punto de entrada
│   ├── visitor.py                   TrezVisitor + Environment + TrezFunction
│   ├── math_utilsdoz.py             re-exporta stdlib al visitor
│   ├── autograd.py                  Tensor + backward topológico
│   ├── errors.py                    jerarquía de errores
│   ├── error_listener.py            TrezErrorListener
│   ├── parser/
│   │   ├── TrezLexer.g4
│   │   ├── TrezParser.g4
│   │   ├── TrezLexer.py             generado ANTLR4
│   │   ├── TrezParser.py            generado ANTLR4
│   │   └── TrezParserVisitor.py     generado ANTLR4
│   └── lib/
│       ├── mathdoz/
│       │   ├── core_mathdoz.py      PI, E, exp, log, sin, cos, tan, sqrt, pow, factorial
│       │   └── tensor_mathdoz.py    dot, transpose
│       ├── activationsdoz/
│       │   └── activationsdoz.py    relu, sigmoid
│       ├── lossesdoz/
│       │   └── lossdoz.py           mse, mse_grad
│       ├── iodoz/
│       │   └── iodoz.py             leer, escribir
│       ├── structsdoz/
│       │   └── structsdoz.py        TrezQueue, TrezStack
│       └── inspectdoz/
│           └── inspectdoz.py        spy, shape
└── tests/
    ├── features/
    │   ├── test_basic.trez
    │   ├── test_math.trez
    │   ├── test_dl.trez
    │   ├── test_backprop.trez
    │   ├── test_io.trez
    │   ├── test_e2_features.trez    pipe, lambdas, namespaces, dicts, structs
    │   ├── test_functions.trez
    │   ├── test_lists.trez
    │   ├── test_control_flow.trez
    │   ├── test_dicts.trez
    │   ├── test_structs.trez
    │   └── test_new_features.trez
    ├── runtime/
    │   ├── test_runtime_error.trez
    │   └── test_runtime_errors.trez
    ├── syntax/
    │   └── test_syntax_error.trez
    ├── run_tests.py
    ├── test_mathdoz_verification.py
    └── test_structs_verification.py
```

---

## 9. Semántica Operacional (reglas clave)

```
-- Binding
Γ ⊢ e ⇒ v
─────────────────────────────
Γ ⊢ let x = e  ⇒  Γ[x ↦ v]

-- Aplicación de función
Γ ⊢ f ⇒ TrezFunction(params, body, env_def)
Γ ⊢ args ⇒ [v1..vn]
env_call = env_def + {param_i ↦ vi} + {f ↦ f}  (self-ref para recursión)
env_call ⊢ body ⇒ v
─────────────────────────────────────────────────
Γ ⊢ f(args) ⇒ v

-- Pipe
Γ ⊢ e1 ⇒ v1
Γ ⊢ e2 ⇒ TrezFunction / builtin f
─────────────────────────────────
Γ ⊢ e1 |> e2  ⇒  f(v1)

-- Lambda
──────────────────────────────────────────
Γ ⊢ \x -> body  ⇒  TrezLambda(x, body, Γ)

-- For
Γ ⊢ iterable ⇒ [v1..vn]
∀ vi: Γ + {var ↦ vi} ⊢ block
─────────────────────────────
Γ ⊢ for var in iterable block  ⇒  ()
```
