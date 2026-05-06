from antlr4.error.ErrorListener import ErrorListener
from errors import TrezSyntaxError

class TrezErrorListener(ErrorListener):
    def __init__(self):
        super(TrezErrorListener, self).__init__()
        self.has_errors = False
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        error = TrezSyntaxError(line, column, msg)
        self.errors.append(error)

    def print_errors(self):
        print("\n❌ Se encontraron errores de sintaxis en el código TREZ:")
        for err in self.errors:
            print(f"  - Línea {err.line}, Columna {err.column}: {err.msg}")
        print()
