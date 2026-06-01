"""
menu.py — Menú de navegación y guía para el proyecto TREZ
Ejecutar: python3 menu.py  (desde la raíz del proyecto)
"""

import os
import sys
import subprocess

# ── Colores ANSI ─────────────────────────────────────────────────────────────
R  = "\033[0m"        # reset
B  = "\033[1m"        # bold
CY = "\033[96m"       # cyan
GR = "\033[92m"       # green
YE = "\033[93m"       # yellow
RE = "\033[91m"       # red
BL = "\033[94m"       # blue
MA = "\033[95m"       # magenta
DIM = "\033[2m"       # dim

# ── Rutas relativas al menú ───────────────────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(BASE, "src")

FILES = {
    "lexer"   : os.path.join(SRC, "parser", "TrezLexer.g4"),
    "parser"  : os.path.join(SRC, "parser", "TrezParser.g4"),
    "visitor" : os.path.join(SRC, "visitor.py"),
    "errors"  : os.path.join(SRC, "errors.py"),
    "main"    : os.path.join(SRC, "main.py"),
    "lib"     : os.path.join(SRC, "lib"),
    "tests"   : os.path.join(BASE, "tests", "features"),
}

# ── Utilidades ────────────────────────────────────────────────────────────────

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input(f"\n{DIM}  Presiona Enter para continuar...{R}")

def titulo(texto, color=CY):
    ancho = 60
    print(f"\n{color}{B}{'═' * ancho}{R}")
    print(f"{color}{B}  {texto}{R}")
    print(f"{color}{B}{'═' * ancho}{R}\n")

def seccion(texto):
    print(f"\n{YE}{B}  ▸ {texto}{R}\n")

def codigo(texto):
    """Muestra un bloque de código con indentación y color."""
    lineas = texto.strip().split("\n")
    for l in lineas:
        print(f"    {GR}{l}{R}")

def abrir_archivo(ruta, linea=None):
    """Intenta abrir el archivo en el editor del sistema o lo muestra en terminal."""
    if not os.path.exists(ruta):
        print(f"  {RE}Archivo no encontrado: {ruta}{R}")
        return

    editor = os.environ.get("EDITOR", "")
    if editor:
        cmd = [editor, ruta] if not linea else [editor, f"+{linea}", ruta]
        subprocess.run(cmd)
    else:
        # Si no hay editor configurado, imprime las líneas relevantes
        with open(ruta, encoding="utf-8") as f:
            lineas = f.readlines()
        inicio = max(0, (linea or 1) - 1)
        fin    = min(len(lineas), inicio + 30)
        print(f"\n  {DIM}{ruta}  (líneas {inicio+1}–{fin}){R}\n")
        for i, l in enumerate(lineas[inicio:fin], start=inicio + 1):
            marca = f"{YE}►{R}" if linea and i == linea else " "
            print(f"  {DIM}{i:4}{R} {marca} {GR}{l}{R}", end="")
        print()

def mostrar_archivo_directo(ruta, inicio, fin):
    """Muestra líneas específicas de un archivo."""
    if not os.path.exists(ruta):
        print(f"  {RE}No se encontró: {ruta}{R}")
        return
    with open(ruta, encoding="utf-8") as f:
        lineas = f.readlines()
    real_fin = min(fin, len(lineas))
    print(f"\n  {DIM}{os.path.relpath(ruta, BASE)}  (líneas {inicio}–{real_fin}){R}\n")
    for i, l in enumerate(lineas[inicio - 1:real_fin], start=inicio):
        print(f"  {DIM}{i:4}{R}  {GR}{l}{R}", end="")

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 1 — Estructura del proyecto
# ══════════════════════════════════════════════════════════════════════════════

def menu_estructura():
    limpiar()
    titulo("ESTRUCTURA DEL PROYECTO TREZ")
    print(f"""
  {BL}TREZ/{R}
  ├── {B}src/{R}
  │   ├── {CY}main.py{R}           →  Punto de entrada.  Ejecuta archivos .trez
  │   ├── {CY}visitor.py{R}        →  Intérprete.  Evalúa cada nodo del AST
  │   ├── {CY}errors.py{R}         →  Tipos de error del lenguaje
  │   ├── {CY}error_listener.py{R} →  Captura errores de ANTLR4
  │   ├── {CY}autograd.py{R}       →  Diferenciación automática
  │   ├── {CY}math_utilsdoz.py{R}  →  Utilidades matemáticas
  │   ├── {CY}parser/{R}
  │   │   ├── {YE}TrezLexer.g4{R}  →  Gramática: tokens (palabras del lenguaje)
  │   │   └── {YE}TrezParser.g4{R} →  Gramática: reglas sintácticas
  │   └── {CY}lib/{R}              →  Librerías nativas (.py y .trez)
  │       ├── mathdoz/   datadoz/   mlpdoz/   kndoz/
  │       ├── logregdoz/ nndoz/     optimdoz/ plotdoz/
  │       └── structsdoz/ treedoz/ ...
  └── {CY}tests/{R}
      └── features/      →  Ejemplos y casos de prueba (.trez + .expected)
""")
    seccion("¿Cómo se ejecuta un archivo TREZ?")
    codigo("python3 src/main.py mi_programa.trez")
    seccion("Flujo interno:")
    print(f"  {DIM}archivo.trez  →  Lexer  →  Parser  →  AST  →  visitor.py  →  resultado{R}\n")
    pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 2 — Gramática
# ══════════════════════════════════════════════════════════════════════════════

def menu_gramatica():
    while True:
        limpiar()
        titulo("GRAMÁTICA DEL LENGUAJE TREZ", YE)
        print(f"  {DIM}Los archivos .g4 definen qué código TREZ es válido.{R}\n")
        print(f"  {B}1.{R}  Tokens — {YE}TrezLexer.g4{R}  (palabras clave, símbolos, literales)")
        print(f"  {B}2.{R}  Reglas sintácticas — {YE}TrezParser.g4{R}  (cómo se combinan los tokens)")
        print(f"  {B}3.{R}  Ver tokens disponibles (keywords y operadores)")
        print(f"  {B}4.{R}  Ver todas las reglas del parser")
        print(f"  {B}5.{R}  Ver regla específica (func_def, if_stmt, for_stmt…)")
        print(f"\n  {B}0.{R}  Volver")
        op = input(f"\n  {CY}Opción:{R} ").strip()

        if op == "1":
            limpiar(); titulo("TrezLexer.g4 — Tokens", YE)
            mostrar_archivo_directo(FILES["lexer"], 1, 60)
            pausar()
        elif op == "2":
            limpiar(); titulo("TrezParser.g4 — Reglas", YE)
            mostrar_archivo_directo(FILES["parser"], 1, 70)
            pausar()
        elif op == "3":
            limpiar(); titulo("Tokens disponibles en TREZ", YE)
            seccion("Palabras reservadas")
            codigo("let  func  return  if  else  while  for  in  true  false  not")
            seccion("Operadores")
            codigo("|>   **   &&   ||   ==   !=   <=   >=   <   >   %   +   -   *   /")
            seccion("Delimitadores")
            codigo("( )   { }   [ ]   ,   ;   =   .   :   \\   ->")
            seccion("Literales")
            codigo('NUMBER  →  42  |  3.14\nSTRING  →  "hola"\nID      →  mi_variable  |  _privado')
            pausar()
        elif op == "4":
            limpiar(); titulo("Reglas del Parser", YE)
            reglas = [
                ("statement",   "Cualquier sentencia del lenguaje"),
                ("let_stmt",    "let x = valor;"),
                ("func_def",    "func nombre(params) { ... }"),
                ("return_stmt", "return valor;"),
                ("if_stmt",     "if (cond) { } else { }"),
                ("while_stmt",  "while (cond) { }"),
                ("for_stmt",    "for x in lista { }"),
                ("rhs",         "Lado derecho: lambda o expresión"),
                ("expr",        "Expresiones con operadores"),
                ("atom",        "Valores atómicos: número, string, ID, llamada"),
                ("array",       "[ elem1, elem2, ... ]"),
                ("dict",        "{ clave: valor, ... }"),
            ]
            for nombre, desc in reglas:
                print(f"  {CY}{nombre:<16}{R}  {desc}")
            pausar()
        elif op == "5":
            limpiar(); titulo("Buscar regla en el Parser", YE)
            regla = input(f"  {CY}Nombre de la regla (ej: func_def):{R} ").strip()
            if regla:
                with open(FILES["parser"], encoding="utf-8") as f:
                    lineas = f.readlines()
                encontrado = False
                for i, l in enumerate(lineas, 1):
                    if regla in l:
                        mostrar_archivo_directo(FILES["parser"], max(1, i - 1), i + 8)
                        encontrado = True
                        break
                if not encontrado:
                    print(f"  {RE}Regla '{regla}' no encontrada en el parser.{R}")
            pausar()
        elif op == "0":
            break

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 3 — Visitor (intérprete)
# ══════════════════════════════════════════════════════════════════════════════

VISITORS = [
    ("visitFunc_def",      381,  "Define funciones con func → crea TrezFunction y la guarda en el scope"),
    ("visitLambdaDef",     350,  "Lambdas anónimas: \\x -> x + 1"),
    ("visitFuncCallExpr",  694,  "Llama una función: evalúa args y delega a _apply"),
    ("visitLet_stmt",      359,  "Asignación: let x = valor;"),
    ("visitIf_stmt",       397,  "Condicional: if / else"),
    ("visitWhile_stmt",    407,  "Bucle while"),
    ("visitFor_stmt",      412,  "Bucle for … in lista"),
    ("visitPipeOp",        444,  "Operador pipe: valor |> funcion"),
    ("visitReturn_stmt",   388,  "Return: lanza ReturnSignal para salir del bloque"),
    ("visitMethodCallExpr",605,  "Llamada de método: obj.metodo(args)"),
    ("visitAddSubExpr",    548,  "Suma y resta"),
    ("visitMulDivExpr",    562,  "Multiplicación, división, módulo"),
    ("visitCompareExpr",   539,  "Comparaciones: <  >  <=  >="),
    ("visitIndexExpr",     589,  "Indexación: lista[i]  |  dict['clave']"),
]

def menu_visitor():
    while True:
        limpiar()
        titulo("VISITOR.PY — INTÉRPRETE", MA)
        print(f"  {DIM}visitor.py evalúa cada nodo del árbol sintáctico (AST).{R}")
        print(f"  {DIM}Cada método visit* corresponde a una regla del parser.{R}\n")
        for i, (nombre, linea, desc) in enumerate(VISITORS, 1):
            print(f"  {B}{i:2}.{R}  {MA}{nombre}{R}  {DIM}(línea {linea}){R}")
            print(f"        {desc}\n")
        print(f"  {B} 0.{R}  Volver")
        op = input(f"\n  {CY}Ver código de opción:{R} ").strip()
        if op == "0":
            break
        if op.isdigit() and 1 <= int(op) <= len(VISITORS):
            nombre, linea, _ = VISITORS[int(op) - 1]
            limpiar()
            titulo(f"visitor.py → {nombre}", MA)
            mostrar_archivo_directo(FILES["visitor"], linea, linea + 20)
            pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 4 — Cómo añadir nueva funcionalidad
# ══════════════════════════════════════════════════════════════════════════════

GUIAS = {
    "1": {
        "titulo": "Nueva función nativa (built-in)",
        "pasos": [
            ("visitor.py", "visitFuncCallExpr", 694,
             'Agrega un if dentro del bloque de builtins:\n\n'
             '    if func_name == "mi_funcion":\n'
             '        # args[0], args[1]... son los argumentos\n'
             '        return resultado'),
            ("Tests", "tests/features/", None,
             'Crea tests/features/test_mi_funcion.trez y\n'
             'tests/features/test_mi_funcion.expected\n'
             'con los valores que debe producir.'),
        ],
        "ejemplo": (
            '// En mi_funcion.trez\n'
            'mostrar(cuadrado(5));   // debe imprimir 25\n\n'
            '// En visitor.py — visitFuncCallExpr\n'
            'if func_name == "cuadrado":\n'
            '    return args[0] ** 2'
        ),
    },
    "2": {
        "titulo": "Nueva sentencia del lenguaje",
        "pasos": [
            ("TrezLexer.g4", "src/parser/TrezLexer.g4", None,
             'Si necesitas una nueva palabra reservada, añádela al lexer:\n\n'
             "    REPEAT:  'repeat';"),
            ("TrezParser.g4", "src/parser/TrezParser.g4", None,
             'Agrega la regla sintáctica en statement y define la regla:\n\n'
             '    statement: ... | repeat_stmt | ...;\n'
             '    repeat_stmt: REPEAT LPAREN rhs RPAREN block;'),
            ("visitor.py", "Nuevo método visit", None,
             'Crea el método correspondiente en TrezVisitor:\n\n'
             '    def visitRepeat_stmt(self, ctx):\n'
             '        n = self.visit(ctx.rhs())\n'
             '        for _ in range(int(n)):\n'
             '            self.visit(ctx.block())\n'
             '        return None'),
            ("Regenerar", "src/parser/", None,
             'Regenera el parser con ANTLR4 (si tienes Java instalado):\n\n'
             '    cd src/parser\n'
             '    antlr4 TrezLexer.g4 TrezParser.g4 -Dlanguage=Python3'),
        ],
        "ejemplo": (
            '// En código TREZ — nueva sentencia repeat:\n'
            'repeat(3) {\n'
            '    mostrar("hola");\n'
            '}'
        ),
    },
    "3": {
        "titulo": "Nueva librería (doz)",
        "pasos": [
            ("src/lib/", "Crear carpeta", None,
             'Crea la carpeta y archivo:\n\n'
             '    src/lib/midoz/\n'
             '    src/lib/midoz/__init__.py\n'
             '    src/lib/midoz/midoz.py'),
            ("midoz.py", "Implementar funciones Python", None,
             'En midoz.py implementa las funciones:\n\n'
             '    def mi_operacion(x, y):\n'
             '        return x + y'),
            ("visitor.py", "Registrar en visitFuncCallExpr", 694,
             'Importa y registra la librería como builtin:\n\n'
             '    from lib.midoz.midoz import mi_operacion\n\n'
             '    # Dentro de visitFuncCallExpr:\n'
             '    if func_name == "mi_operacion":\n'
             '        return mi_operacion(args[0], args[1])'),
        ],
        "ejemplo": (
            '// En código TREZ — usando la nueva librería:\n'
            'let resultado = mi_operacion(10, 5);\n'
            'mostrar(resultado);   // 15'
        ),
    },
    "4": {
        "titulo": "Nuevo tipo de error",
        "pasos": [
            ("errors.py", "src/errors.py", None,
             'Define la nueva clase de error heredando de TrezError:\n\n'
             '    class MiError(TrezError):\n'
             '        def __init__(self, msg):\n'
             '            super().__init__(msg)'),
            ("visitor.py", "Lanzar el error", None,
             'Importa y lanza el error donde corresponda:\n\n'
             '    from errors import MiError\n\n'
             '    raise MiError("Descripción del error")'),
            ("main.py", "Capturar en main.py", None,
             'Agrega el except en main.py:\n\n'
             '    except MiError as e:\n'
             '        print(f"[MiError] {e.msg}", file=sys.stderr)\n'
             '        sys.exit(1)'),
        ],
        "ejemplo": (
            '// Cuando TREZ encuentre el error lanzará:\n'
            '[MiError] Descripción del error'
        ),
    },
}

def menu_agregar():
    while True:
        limpiar()
        titulo("GUÍA: AGREGAR NUEVA FUNCIONALIDAD", GR)
        print(f"  {B}1.{R}  Nueva función nativa (built-in)")
        print(f"  {B}2.{R}  Nueva sentencia del lenguaje  {DIM}(ej: repeat, switch){R}")
        print(f"  {B}3.{R}  Nueva librería  {DIM}(ej: estadisticadoz){R}")
        print(f"  {B}4.{R}  Nuevo tipo de error")
        print(f"\n  {B}0.{R}  Volver")
        op = input(f"\n  {CY}Opción:{R} ").strip()
        if op == "0":
            break
        guia = GUIAS.get(op)
        if not guia:
            continue

        limpiar()
        titulo(guia["titulo"], GR)
        for i, paso in enumerate(guia["pasos"], 1):
            archivo, ref, linea, instruccion = paso
            print(f"  {GR}{B}Paso {i} — {archivo}{R}")
            if linea:
                print(f"  {DIM}  → ver visitor.py línea {linea}{R}")
            for l in instruccion.split("\n"):
                if l.startswith("    "):
                    print(f"  {GR}  {l}{R}")
                else:
                    print(f"  {l}")
            print()

        seccion("Ejemplo de código TREZ")
        codigo(guia["ejemplo"])
        pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 5 — Ejemplos de código TREZ
# ══════════════════════════════════════════════════════════════════════════════

EJEMPLOS = [
    ("Variables y aritmética", """
let x = 10;
let y = 3.14;
let suma = x + y;
mostrar(suma);          // 13.14
mostrar(x ** 2);        // 100  (potencia)
mostrar(10 % 3);        // 1    (módulo)"""),

    ("Función y llamada", """
func factorial(n) {
    if (n <= 1) { return 1; }
    return n * factorial(n - 1);
}
mostrar(factorial(5));  // 120"""),

    ("Lambda / función anónima", """
let doble = \\n -> n * 2;
mostrar(doble(7));      // 14

// Guardada en variable y usada como argumento
let nums = [1, 2, 3, 4];
let dobles = map(nums, \\x -> x * 2);
mostrar(dobles);        // [2, 4, 6, 8]"""),

    ("Pipe operator |>", """
let resultado = [1, 2, 3, 4, 5] |> sum;
mostrar(resultado);     // 15

// Encadenar operaciones:
let r = [3, 1, 4, 1, 5] |> sorted |> reversed;
mostrar(r);             // [5, 4, 3, 1, 1]"""),

    ("Condicionales", """
func signo(x) {
    if (x > 0)      { return "positivo"; }
    else if (x < 0) { return "negativo"; }
    else            { return "cero"; }
}
mostrar(signo(-7));     // negativo"""),

    ("Bucles while y for", """
// while
let i = 0;
while (i < 3) {
    mostrar(i);
    let i = i + 1;
}

// for … in lista
for x in [10, 20, 30] {
    mostrar(x);
}"""),

    ("Listas y diccionarios", """
let lista = [1, 2, 3];
mostrar(lista[0]);      // 1
mostrar(len(lista));    // 3

let persona = {"nombre": "Ana", "edad": 25};
mostrar(persona["nombre"]);   // Ana"""),

    ("Structs (tipos propios)", """
struct Punto { x, y }

let p = Punto { x: 3, y: 4 };
mostrar(p.x);           // 3

func distancia(p) {
    return (p.x ** 2 + p.y ** 2) ** 0.5;
}
mostrar(distancia(p));  // 5.0"""),
]

def menu_ejemplos():
    while True:
        limpiar()
        titulo("EJEMPLOS DE CÓDIGO TREZ", BL)
        for i, (nombre, _) in enumerate(EJEMPLOS, 1):
            print(f"  {B}{i}.{R}  {nombre}")
        print(f"\n  {B}0.{R}  Volver")
        op = input(f"\n  {CY}Opción:{R} ").strip()
        if op == "0":
            break
        if op.isdigit() and 1 <= int(op) <= len(EJEMPLOS):
            nombre, code = EJEMPLOS[int(op) - 1]
            limpiar()
            titulo(nombre, BL)
            codigo(code)
            pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 6 — Ejecutar un archivo .trez
# ══════════════════════════════════════════════════════════════════════════════

def menu_ejecutar():
    limpiar()
    titulo("EJECUTAR UN ARCHIVO .trez", RE)
    print(f"  Escribe la ruta del archivo .trez que quieres ejecutar.")
    print(f"  {DIM}Puedes usar los archivos de tests/features/ como ejemplo.{R}\n")

    # Listar archivos de ejemplo
    ejemplos = [f for f in os.listdir(FILES["tests"]) if f.endswith(".trez")]
    print(f"  {DIM}Ejemplos disponibles:{R}")
    for i, ej in enumerate(sorted(ejemplos), 1):
        print(f"    {i:2}. {ej}")

    print()
    ruta = input(f"  {CY}Ruta del archivo (Enter para cancelar):{R} ").strip()
    if not ruta:
        return

    # Si es número, usar el ejemplo correspondiente
    if ruta.isdigit():
        idx = int(ruta) - 1
        lista = sorted(ejemplos)
        if 0 <= idx < len(lista):
            ruta = os.path.join(FILES["tests"], lista[idx])
    elif not os.path.isabs(ruta):
        ruta = os.path.join(BASE, ruta)

    if not os.path.exists(ruta):
        print(f"\n  {RE}Archivo no encontrado: {ruta}{R}")
        pausar()
        return

    print(f"\n  {GR}Ejecutando:{R} {ruta}\n  {'─' * 50}")
    main_py = os.path.join(SRC, "main.py")
    resultado = subprocess.run(
        [sys.executable, main_py, ruta],
        capture_output=False,
        cwd=BASE,
    )
    print(f"  {'─' * 50}")
    if resultado.returncode != 0:
        print(f"  {RE}El programa terminó con errores (código {resultado.returncode}).{R}")
    else:
        print(f"  {GR}Programa ejecutado correctamente.{R}")
    pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  SECCIÓN 7 — Referencia rápida
# ══════════════════════════════════════════════════════════════════════════════

def menu_referencia():
    limpiar()
    titulo("REFERENCIA RÁPIDA — TREZ", CY)

    seccion("Sintaxis básica")
    codigo("""\
let x = 42;                        // variable
func f(a, b) { return a + b; }    // función
let g = \\x -> x * 2;              // lambda
f(3, 4) |> mostrar;               // pipe""")

    seccion("Estructuras de control")
    codigo("""\
if (cond) { } else { }
while (cond) { }
for x in lista { }""")

    seccion("Tipos de datos")
    codigo("""\
Número:      42  |  3.14
String:      "hola"
Booleano:    true  |  false
Lista:       [1, 2, 3]
Diccionario: {"a": 1, "b": 2}""")

    seccion("Funciones nativas disponibles")
    codigo("""\
mostrar(x)          // imprime
leer(archivo)       // lee archivo
len(lista)          // longitud
map(lista, fn)      // aplica fn a cada elemento
filter(lista, fn)   // filtra con fn
reduce(lista, fn)   // reduce con fn
sum(lista)          // suma total
sorted(lista)       // ordena
reversed(lista)     // invierte
str(x) / num(x)    // conversión de tipos""")

    seccion("Archivos del proyecto")
    archivos = [
        ("src/parser/TrezLexer.g4",  "Tokens del lenguaje"),
        ("src/parser/TrezParser.g4", "Gramática sintáctica"),
        ("src/visitor.py",           "Intérprete (evaluador)"),
        ("src/errors.py",            "Definición de errores"),
        ("src/main.py",              "Punto de entrada CLI"),
        ("src/lib/",                 "Librerías nativas"),
        ("tests/features/",          "Ejemplos y pruebas"),
    ]
    for ruta, desc in archivos:
        print(f"  {CY}{ruta:<35}{R}  {desc}")

    pausar()

# ══════════════════════════════════════════════════════════════════════════════
#  MENÚ PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

OPCIONES = [
    ("Estructura del proyecto",          menu_estructura),
    ("Gramática (Lexer y Parser .g4)",   menu_gramatica),
    ("Visitor — cómo se evalúa el AST", menu_visitor),
    ("Añadir nueva funcionalidad",       menu_agregar),
    ("Ejemplos de código TREZ",          menu_ejemplos),
    ("Ejecutar un archivo .trez",        menu_ejecutar),
    ("Referencia rápida",               menu_referencia),
]

def main():
    while True:
        limpiar()
        print(f"""
{CY}{B}  ████████╗██████╗ ███████╗███████╗
  ╚══██╔══╝██╔══██╗██╔════╝╚════██║
     ██║   ██████╔╝█████╗      ██╔╝
     ██║   ██╔══██╗██╔══╝     ██╔╝
     ██║   ██║  ██║███████╗   ██║
     ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝{R}
{DIM}  Menú de navegación y guía del lenguaje TREZ{R}
""")
        for i, (nombre, _) in enumerate(OPCIONES, 1):
            print(f"  {B}{i}.{R}  {nombre}")
        print(f"\n  {B}0.{R}  Salir")
        print()

        op = input(f"  {CY}Selecciona una opción:{R} ").strip()

        if op == "0":
            limpiar()
            print(f"\n  {GR}¡Hasta luego!{R}\n")
            break
        if op.isdigit() and 1 <= int(op) <= len(OPCIONES):
            OPCIONES[int(op) - 1][1]()

if __name__ == "__main__":
    main()
