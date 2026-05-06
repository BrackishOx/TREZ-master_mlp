class TrezError(Exception):
    """Base class for all TREZ language errors."""
    pass


class TrezSyntaxError(TrezError):
    """Raised during lexing/parsing. Includes line, column and offending token."""
    def __init__(self, line, column, msg):
        self.line = line
        self.column = column
        self.msg = msg
        super().__init__(f"[SyntaxError] Line {line}, Col {column}: {msg}")


class TrezRuntimeError(TrezError):
    """Base runtime error. Raised for semantic/evaluation failures."""
    def __init__(self, msg):
        self.msg = msg
        super().__init__(f"[RuntimeError] {msg}")


class UndefinedSymbolError(TrezRuntimeError):
    """Raised when an identifier is not found in any enclosing scope."""
    def __init__(self, name):
        self.symbol = name
        super().__init__(f"Símbolo no definido: '{name}'")


class ShapeMismatchError(TrezRuntimeError):
    """Raised when tensor dimensions are incompatible for an operation."""
    def __init__(self, op, shape_a, shape_b):
        super().__init__(
            f"Dimensiones incompatibles en '{op}': {shape_a} vs {shape_b}"
        )


class MathDomainError(TrezRuntimeError):
    """Raised for mathematically illegal operations (log(0), sqrt(-1), etc.)."""
    def __init__(self, func, value):
        super().__init__(
            f"Dominio inválido en '{func}': el argumento {value} no está permitido"
        )


class TypeMismatchError(TrezRuntimeError):
    """Raised when an operation receives arguments of the wrong type."""
    def __init__(self, op, expected, got):
        super().__init__(
            f"Tipo incorrecto en '{op}': se esperaba {expected}, se recibió {got}"
        )
