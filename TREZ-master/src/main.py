import sys
import os
sys.path.append(os.path.dirname(__file__))

from antlr4 import *
from parser.TrezLexer import TrezLexer
from parser.TrezParser import TrezParser
from visitor import TrezVisitor
from error_listener import TrezErrorListener
from errors import (
    TrezRuntimeError,
    UndefinedSymbolError,
    ShapeMismatchError,
    MathDomainError,
    TypeMismatchError,
)


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <archivo.trez>")
        sys.exit(1)

    input_stream = FileStream(sys.argv[1], encoding='utf-8')

    lexer  = TrezLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TrezParser(stream)

    error_listener = TrezErrorListener()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.has_errors:
        error_listener.print_errors()
        sys.exit(1)

    visitor = TrezVisitor()
    try:
        visitor.visit(tree)
    except UndefinedSymbolError as e:
        print(f"\n[UndefinedSymbolError] {e.msg}\n", file=sys.stderr)
        sys.exit(1)
    except ShapeMismatchError as e:
        print(f"\n[ShapeMismatchError] {e.msg}\n", file=sys.stderr)
        sys.exit(1)
    except MathDomainError as e:
        print(f"\n[MathDomainError] {e.msg}\n", file=sys.stderr)
        sys.exit(1)
    except TypeMismatchError as e:
        print(f"\n[TypeMismatchError] {e.msg}\n", file=sys.stderr)
        sys.exit(1)
    except TrezRuntimeError as e:
        print(f"\n[RuntimeError] {e.msg}\n", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
