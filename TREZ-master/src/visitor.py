import sys
import os
sys.path.append(os.path.dirname(__file__))

from parser.TrezParser import TrezParser
from parser.TrezParserVisitor import TrezParserVisitor as AntlrTrezVisitor
import math_utilsdoz
from errors import TrezRuntimeError, UndefinedSymbolError
from lib.iodoz.iodoz import read_file_doz, write_file_doz
from lib.structsdoz.structsdoz import TrezQueue, TrezStack, make_queue, make_stack
from lib.inspectdoz.inspectdoz import spy as inspectdoz_spy, shape as inspectdoz_shape
from lib.optimdoz.optimdoz import sgd as optimdoz_sgd, adam as optimdoz_adam, zeros_like as optimdoz_zeros
from lib.lossesdoz.lossdoz import cross_entropy as lossdoz_ce, cross_entropy_grad as lossdoz_ce_grad
from lib.nndoz.nndoz import (
    linear_init as nndoz_linear_init,
    linear_forward as nndoz_linear_forward,
    linear_backward as nndoz_linear_backward,
    relu_forward as nndoz_relu_forward,
    relu_backward as nndoz_relu_backward,
    softmax_forward as nndoz_softmax,
    sequential_forward as nndoz_sequential,
    get_params as nndoz_params,
    get_param_count as nndoz_param_count,
)
from lib.datadoz.datadoz import (
    from_lists as datadoz_from_lists,
    make_loader as datadoz_loader,
    get_batches as datadoz_batches,
    train_test_split as datadoz_split,
    read_csv as datadoz_read_csv,
    read_xlsx as datadoz_read_xlsx,
    get_column as datadoz_col,
    get_row as datadoz_row,
    num_rows as datadoz_nrows,
    num_cols as datadoz_ncols,
    column_names as datadoz_col_names,
)
from lib.plotdoz.plotdoz import (
    learning_curve as plotdoz_learning_curve,
    histogram as plotdoz_histogram,
    bar_chart as plotdoz_bar,
    scatter as plotdoz_scatter,
    line_chart as plotdoz_line,
)
from lib.mlpdoz.mlpdoz import (
    crear as mlpdoz_crear,
    entrenar as mlpdoz_entrenar,
    predecir as mlpdoz_predecir,
    predecir_proba as mlpdoz_predecir_proba,
    puntaje as mlpdoz_puntaje,
    set_lr as mlpdoz_set_lr,
    get_lr as mlpdoz_get_lr,
    historial as mlpdoz_historial,
    clases as mlpdoz_clases,
    matriz_confusion as mlpdoz_confusion,
    reporte as mlpdoz_reporte,
)
from lib.kndoz.kndoz import (
    crear as kndoz_crear,
    entrenar as kndoz_entrenar,
    predecir as kndoz_predecir,
    predecir_proba as kndoz_predecir_proba,
    puntaje as kndoz_puntaje,
    set_k as kndoz_set_k,
    get_k as kndoz_get_k,
    vecinos as kndoz_vecinos,
    clases as kndoz_clases,
)
from lib.logregdoz.logregdoz import (
    crear as logregdoz_crear,
    entrenar as logregdoz_entrenar,
    predecir as logregdoz_predecir,
    predecir_proba as logregdoz_predecir_proba,
    puntaje as logregdoz_puntaje,
    set_lr as logregdoz_set_lr,
    get_lr as logregdoz_get_lr,
    coeficientes as logregdoz_coef,
    historial as logregdoz_historial,
    clases as logregdoz_clases,
)
from lib.treedoz.treedoz import (
    crear as treedoz_crear,
    entrenar as treedoz_entrenar,
    predecir as treedoz_predecir,
    predecir_proba as treedoz_predecir_proba,
    puntaje as treedoz_puntaje,
    profundidad as treedoz_profundidad,
    num_hojas as treedoz_hojas,
    importancia as treedoz_importancia,
    clases as treedoz_clases,
)


# ── Namespace registry — Modulo.funcion() dispatch ───────────────────────────

_NAMESPACES = {
    'Tensordoz': {
        'dot':       lambda args: math_utilsdoz.dot(args[0], args[1]),
        'transpose': lambda args: math_utilsdoz.transpose(args[0]),
    },
    'Mathdoz': {
        'relu':      lambda args: math_utilsdoz.relu(args[0]),
        'sigmoid':   lambda args: math_utilsdoz.sigmoid(args[0]),
        'exp':       lambda args: math_utilsdoz.exp_doz(args[0]),
        'log':       lambda args: math_utilsdoz.log_doz(args[0]),
        'sin':       lambda args: math_utilsdoz.sin_doz(args[0]),
        'cos':       lambda args: math_utilsdoz.cos_doz(args[0]),
        'tan':       lambda args: math_utilsdoz.tan_doz(args[0]),
        'sqrt':      lambda args: math_utilsdoz.sqrt_doz(args[0]),
        'abs':       lambda args: math_utilsdoz.abs_doz(args[0]),
        'pow':       lambda args: math_utilsdoz.pow_doz(args[0], args[1]),
        'factorial': lambda args: math_utilsdoz.factorial_doz(args[0]),
    },
    'IOdoz': {
        'leer':    lambda args: read_file_doz(args[0]),
        'escribir': lambda args: write_file_doz(args[0], args[1]),
    },
    'Inspectdoz': {
        'spy':   lambda args: inspectdoz_spy(args[0]),
        'shape': lambda args: inspectdoz_shape(args[0]),
    },
    'Optimdoz': {
        'sgd':        lambda args: optimdoz_sgd(args[0], args[1], *args[2:]),
        'adam':       lambda args: optimdoz_adam(args[0], args[1], args[2], args[3], int(args[4]), *args[5:]),
        'zeros_like': lambda args: optimdoz_zeros(args[0]),
    },
    'Metricsdoz': {
        'mse':              lambda args: math_utilsdoz.mse(args[0], args[1]),
        'mse_grad':         lambda args: math_utilsdoz.mse_grad(args[0], args[1]),
        'cross_entropy':    lambda args: lossdoz_ce(args[0], args[1]),
        'cross_entropy_grad': lambda args: lossdoz_ce_grad(args[0], args[1]),
    },
    'NNdoz': {
        'linear_init':     lambda args: nndoz_linear_init(int(args[0]), int(args[1])),
        'linear_forward':  lambda args: nndoz_linear_forward(args[0], args[1]),
        'linear_backward': lambda args: nndoz_linear_backward(args[0], args[1], args[2]),
        'relu_forward':    lambda args: list(nndoz_relu_forward(args[0])),
        'relu_backward':   lambda args: nndoz_relu_backward(args[0], args[1]),
        'softmax':         lambda args: nndoz_softmax(args[0]),
        'sequential':      lambda args: list(nndoz_sequential(args[0], args[1])),
        'get_params':      lambda args: nndoz_params(args[0]),
        'param_count':     lambda args: nndoz_param_count(args[0]),
    },
    'Datadoz': {
        'from_lists':        lambda args: datadoz_from_lists(args[0], args[1]),
        'make_loader':       lambda args: datadoz_loader(args[0], int(args[1]), bool(args[2]) if len(args) > 2 else False),
        'get_batches':       lambda args: datadoz_batches(args[0]),
        'train_test_split':  lambda args: datadoz_split(args[0], args[1], args[2] if len(args) > 2 else 0.2),
        'read_csv':          lambda args: datadoz_read_csv(args[0], args[1] if len(args) > 1 else ','),
        'read_xlsx':         lambda args: datadoz_read_xlsx(args[0]),
        'columna':           lambda args: datadoz_col(args[0], args[1]),
        'fila':              lambda args: datadoz_row(args[0], int(args[1])),
        'num_filas':         lambda args: datadoz_nrows(args[0]),
        'num_columnas':      lambda args: datadoz_ncols(args[0]),
        'columnas':          lambda args: datadoz_col_names(args[0]),
    },
    'Plotdoz': {
        'learning_curve': lambda args: plotdoz_learning_curve(args[0], args[1] if len(args) > 1 else None, *args[2:]),
        'histogram':      lambda args: plotdoz_histogram(args[0], *args[1:]),
        'bar_chart':      lambda args: plotdoz_bar(args[0], args[1], *args[2:]),
        'scatter':        lambda args: plotdoz_scatter(args[0], args[1], *args[2:]),
        'line_chart':     lambda args: plotdoz_line(args[0], args[1], *args[2:]),
    },
    'MLPdoz': {
        'crear':            lambda args: mlpdoz_crear(
                                args[0] if len(args) > 0 else [100],
                                float(args[1]) if len(args) > 1 else 0.001,
                                args[2] if len(args) > 2 else 'relu',
                                int(args[3]) if len(args) > 3 else 200,
                                int(args[4]) if len(args) > 4 else 32,
                                bool(args[5]) if len(args) > 5 else False,
                            ),
        'entrenar':         lambda args: mlpdoz_entrenar(args[0], args[1], args[2]),
        'predecir':         lambda args: mlpdoz_predecir(args[0], args[1]),
        'predecir_proba':   lambda args: mlpdoz_predecir_proba(args[0], args[1]),
        'puntaje':          lambda args: mlpdoz_puntaje(args[0], args[1], args[2]),
        'set_lr':           lambda args: mlpdoz_set_lr(args[0], float(args[1])),
        'get_lr':           lambda args: mlpdoz_get_lr(args[0]),
        'historial':        lambda args: mlpdoz_historial(args[0]),
        'clases':           lambda args: mlpdoz_clases(args[0]),
        'matriz_confusion': lambda args: mlpdoz_confusion(args[0], args[1]),
        'reporte':          lambda args: mlpdoz_reporte(args[0], args[1], args[2] if len(args) > 2 else None),
    },
    # ── KNdoz: K-Vecinos más Cercanos ────────────────────────────────────────
    'KNdoz': {
        'crear':           lambda args: kndoz_crear(
                               int(args[0]) if len(args) > 0 else 5,
                               args[1] if len(args) > 1 else 'euclidea',
                           ),
        'entrenar':        lambda args: kndoz_entrenar(args[0], args[1], args[2]),
        'predecir':        lambda args: kndoz_predecir(args[0], args[1]),
        'predecir_proba':  lambda args: kndoz_predecir_proba(args[0], args[1]),
        'puntaje':         lambda args: kndoz_puntaje(args[0], args[1], args[2]),
        'set_k':           lambda args: kndoz_set_k(args[0], int(args[1])),
        'get_k':           lambda args: kndoz_get_k(args[0]),
        'vecinos':         lambda args: kndoz_vecinos(args[0], args[1], int(args[2]) if len(args) > 2 else None),
        'clases':          lambda args: kndoz_clases(args[0]),
    },
    # ── LogRegdoz: Regresión Logística ───────────────────────────────────────
    'LogRegdoz': {
        'crear':           lambda args: logregdoz_crear(
                               float(args[0]) if len(args) > 0 else 0.1,
                               int(args[1]) if len(args) > 1 else 200,
                               float(args[2]) if len(args) > 2 else 1e-4,
                               bool(args[3]) if len(args) > 3 else False,
                           ),
        'entrenar':        lambda args: logregdoz_entrenar(args[0], args[1], args[2]),
        'predecir':        lambda args: logregdoz_predecir(args[0], args[1]),
        'predecir_proba':  lambda args: logregdoz_predecir_proba(args[0], args[1]),
        'puntaje':         lambda args: logregdoz_puntaje(args[0], args[1], args[2]),
        'set_lr':          lambda args: logregdoz_set_lr(args[0], float(args[1])),
        'get_lr':          lambda args: logregdoz_get_lr(args[0]),
        'coeficientes':    lambda args: logregdoz_coef(args[0]),
        'historial':       lambda args: logregdoz_historial(args[0]),
        'clases':          lambda args: logregdoz_clases(args[0]),
    },
    # ── Treedoz: Árbol de Decisión ───────────────────────────────────────────
    'Treedoz': {
        'crear':           lambda args: treedoz_crear(
                               int(args[0]) if len(args) > 0 else None,
                               int(args[1]) if len(args) > 1 else 2,
                               args[2] if len(args) > 2 else 'gini',
                           ),
        'entrenar':        lambda args: treedoz_entrenar(args[0], args[1], args[2]),
        'predecir':        lambda args: treedoz_predecir(args[0], args[1]),
        'predecir_proba':  lambda args: treedoz_predecir_proba(args[0], args[1]),
        'puntaje':         lambda args: treedoz_puntaje(args[0], args[1], args[2]),
        'profundidad':     lambda args: treedoz_profundidad(args[0]),
        'num_hojas':       lambda args: treedoz_hojas(args[0]),
        'importancia':     lambda args: treedoz_importancia(args[0]),
        'clases':          lambda args: treedoz_clases(args[0]),
    },
}


# ── Signal for return statement ───────────────────────────────────────────────

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value


# ── Callable types ────────────────────────────────────────────────────────────

class TrezFunction:
    """Named closure: captures params, body AST, and definition environment."""
    def __init__(self, name, params, body_ctx, env):
        self.name = name
        self.params = params
        self.body_ctx = body_ctx
        self.env = env

    def __repr__(self):
        return f"<func {self.name}({', '.join(self.params)})>"


class TrezLambda:
    """Anonymous single-parameter lambda: \\param -> rhs."""
    def __init__(self, param, body_ctx, env):
        self.param = param
        self.body_ctx = body_ctx
        self.env = env

    def __repr__(self):
        return f"<lambda {self.param}>"


class TrezBuiltin:
    """Wraps a native Python callable so it can be passed as a first-class value."""
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def __repr__(self):
        return f"<builtin {self.name}>"


# ── Scope chain ───────────────────────────────────────────────────────────────

class Environment:
    """Linked scopes — functional lookup chain, no global mutable state."""
    def __init__(self, parent=None):
        self.bindings = {}
        self.parent = parent

    def get(self, name):
        if name in self.bindings:
            return self.bindings[name]
        if self.parent:
            return self.parent.get(name)
        raise UndefinedSymbolError(name)

    def set(self, name, value):
        self.bindings[name] = value

    def update(self, name, value):
        """Update existing binding in nearest enclosing scope; create locally if not found."""
        if name in self.bindings:
            self.bindings[name] = value
            return
        if self.parent and self.parent.has(name):
            self.parent.update(name, value)
            return
        self.bindings[name] = value

    def has(self, name):
        if name in self.bindings:
            return True
        if self.parent:
            return self.parent.has(name)
        return False


# ── Visitor ───────────────────────────────────────────────────────────────────

class TrezVisitor(AntlrTrezVisitor):
    def __init__(self):
        super().__init__()
        self.global_env = Environment()
        self.env = self.global_env
        self._call_depth = 0  # >0 when inside a function/lambda body
        self._register_builtins()

    def _register_builtins(self):
        """Register native math functions as first-class values in global scope."""
        builtins = {
            'relu':      lambda x: math_utilsdoz.relu(x),
            'sigmoid':   lambda x: math_utilsdoz.sigmoid(x),
            'sqrt':      lambda x: math_utilsdoz.sqrt_doz(x),
            'exp':       lambda x: math_utilsdoz.exp_doz(x),
            'log':       lambda x: math_utilsdoz.log_doz(x),
            'sin':       lambda x: math_utilsdoz.sin_doz(x),
            'cos':       lambda x: math_utilsdoz.cos_doz(x),
            'tan':       lambda x: math_utilsdoz.tan_doz(x),
            'abs':       lambda x: math_utilsdoz.abs_doz(x),
            'factorial': lambda x: math_utilsdoz.factorial_doz(x),
        }
        for name, fn in builtins.items():
            self.global_env.set(name, TrezBuiltin(name, fn))

    # ── program ──────────────────────────────────────────────────────────────

    def visitProgram(self, ctx: TrezParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # ── rhs delegation (lambda | expr) ──────────────────────────────────────

    def visitLambdaDef(self, ctx: TrezParser.LambdaDefContext):
        param = ctx.ID().getText()
        return TrezLambda(param, ctx.rhs(), self.env)

    def visitExprRhs(self, ctx: TrezParser.ExprRhsContext):
        return self.visit(ctx.expr())

    # ── statements ───────────────────────────────────────────────────────────

    def visitLet_stmt(self, ctx: TrezParser.Let_stmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.rhs())
        self.env.update(name, value)
        return value

    def visitBind_tuple(self, ctx: TrezParser.Bind_tupleContext):
        """let [a, b, c] = rhs  — destructures a list into named bindings."""
        names = [tok.getText() for tok in ctx.ID()]
        value = self.visit(ctx.rhs())
        if not isinstance(value, list):
            raise TrezRuntimeError(
                f"Desestructuración de tupla requiere una lista, recibió {type(value).__name__}."
            )
        if len(value) < len(names):
            raise TrezRuntimeError(
                f"Desestructuración: se esperaban {len(names)} elementos, la lista tiene {len(value)}."
            )
        for name, val in zip(names, value):
            self.env.update(name, val)
        return value

    def visitFunc_def(self, ctx: TrezParser.Func_defContext):
        name = ctx.ID().getText()
        params = [p.getText() for p in ctx.param_list().ID()] if ctx.param_list() else []
        fn = TrezFunction(name, params, ctx.block(), self.env)
        self.env.set(name, fn)
        return fn

    def visitReturn_stmt(self, ctx: TrezParser.Return_stmtContext):
        raise ReturnSignal(self.visit(ctx.rhs()))

    def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
        result = self.visit(ctx.rhs())
        if result is not None and self._call_depth == 0:
            print(result)
        return result

    def visitIf_stmt(self, ctx: TrezParser.If_stmtContext):
        cond = self.visit(ctx.rhs())
        if cond:
            return self.visit(ctx.block(0))
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.block(1) is not None:
            return self.visit(ctx.block(1))
        return None

    def visitWhile_stmt(self, ctx: TrezParser.While_stmtContext):
        while self.visit(ctx.rhs()):
            self.visit(ctx.block())
        return None

    def visitFor_stmt(self, ctx: TrezParser.For_stmtContext):
        var_name = ctx.ID().getText()
        iterable = self.visit(ctx.rhs())
        if isinstance(iterable, (TrezQueue, TrezStack)):
            iterable = iterable.to_list()
        if not isinstance(iterable, (list, str)):
            raise TrezRuntimeError("for..in requiere una lista o texto.")
        for item in iterable:
            loop_env = Environment(self.env)
            loop_env.set(var_name, item)
            saved = self.env
            self.env = loop_env
            try:
                self.visit(ctx.block())
            finally:
                self.env = saved
        return None

    def visitBlock(self, ctx: TrezParser.BlockContext):
        block_env = Environment(self.env)
        saved = self.env
        self.env = block_env
        result = None
        try:
            for stmt in ctx.statement():
                result = self.visit(stmt)
        finally:
            self.env = saved
        return result

    # ── lambda & pipe ─────────────────────────────────────────────────────────

    def visitPipeOp(self, ctx: TrezParser.PipeOpContext):
        """expr |> expr  ≡  right(left) — left-associative"""
        value = self.visit(ctx.expr(0))
        fn    = self.visit(ctx.expr(1))
        return self._apply(fn, [value])

    def _apply(self, fn, args):
        """Call a TrezFunction, TrezLambda, or builtin with args."""
        if isinstance(fn, TrezLambda):
            call_env = Environment(fn.env)
            call_env.set(fn.param, args[0])
            saved = self.env
            self.env = call_env
            self._call_depth += 1
            try:
                result = self.visit(fn.body_ctx)
            finally:
                self.env = saved
                self._call_depth -= 1
            return result
        if isinstance(fn, TrezFunction):
            return self._call_function(fn, args)
        raise TrezRuntimeError(
            f"El operador |> requiere una función en el lado derecho, recibió {type(fn).__name__}."
        )

    # ── expressions ──────────────────────────────────────────────────────────

    def visitNumExpr(self, ctx: TrezParser.NumExprContext):
        val = ctx.getText()
        return float(val) if '.' in val else int(val)

    def visitStringExpr(self, ctx: TrezParser.StringExprContext):
        raw = ctx.getText()[1:-1]
        raw = raw.replace('\\n', '\n').replace('\\t', '\t')
        raw = raw.replace('\\"', '"').replace('\\\\', '\\')
        return raw

    def visitBoolExpr(self, ctx: TrezParser.BoolExprContext):
        return ctx.getText() == 'true'

    def visitVarExpr(self, ctx: TrezParser.VarExprContext):
        name = ctx.ID().getText()
        if hasattr(math_utilsdoz, 'constants') and name in math_utilsdoz.constants:
            return math_utilsdoz.constants[name]
        return self.env.get(name)

    def visitParenExpr(self, ctx: TrezParser.ParenExprContext):
        return self.visit(ctx.rhs())

    def visitPostfixExpr(self, ctx: TrezParser.PostfixExprContext):
        return self.visit(ctx.postfix())

    def visitAtomExpr(self, ctx: TrezParser.AtomExprContext):
        return self.visit(ctx.atom())

    def visitArrayExpr(self, ctx: TrezParser.ArrayExprContext):
        return self.visit(ctx.array())

    def visitArray(self, ctx: TrezParser.ArrayContext):
        return [self.visit(r) for r in ctx.rhs()]

    def visitDictExpr(self, ctx: TrezParser.DictExprContext):
        return self.visit(ctx.dict_())

    def visitDict(self, ctx: TrezParser.DictContext):
        result = {}
        for entry in ctx.dict_entry():
            key_token = entry.getChild(0).getText()
            key = key_token[1:-1] if key_token.startswith('"') else key_token
            result[key] = self.visit(entry.rhs())
        return result

    # ── operators ────────────────────────────────────────────────────────────

    def visitNotExpr(self, ctx: TrezParser.NotExprContext):
        return not bool(self.visit(ctx.expr()))

    def visitAndExpr(self, ctx: TrezParser.AndExprContext):
        left = self.visit(ctx.expr(0))
        if not bool(left):
            return False
        return bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx: TrezParser.OrExprContext):
        left = self.visit(ctx.expr(0))
        if bool(left):
            return True
        return bool(self.visit(ctx.expr(1)))

    def visitEqExpr(self, ctx: TrezParser.EqExprContext):
        left  = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left == right if ctx.getChild(1).getText() == '==' else left != right

    def visitCompareExpr(self, ctx: TrezParser.CompareExprContext):
        left  = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '<':  return left < right
        if op == '<=': return left <= right
        if op == '>':  return left > right
        return left >= right

    def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
        left  = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if isinstance(left, list) and isinstance(right, list):
            if len(left) != len(right):
                raise TrezRuntimeError("Listas de distinto tamaño en suma/resta.")
            if op == '+':
                return [l + r for l, r in zip(left, right)]
            return [l - r for l, r in zip(left, right)]
        if op == '+':
            return left + right
        return left - right

    def visitMulDivExpr(self, ctx: TrezParser.MulDivExprContext):
        left  = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            if isinstance(left, (int, float)) and isinstance(right, list):
                return [left * r for r in right]
            if isinstance(left, list) and isinstance(right, (int, float)):
                return [l * right for l in left]
            return left * right
        if op == '/':
            if right == 0:
                raise TrezRuntimeError("División por cero.")
            return left / right
        return left % right

    def visitPowExpr(self, ctx: TrezParser.PowExprContext):
        return math_utilsdoz.pow_doz(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitUnaryMinusExpr(self, ctx: TrezParser.UnaryMinusExprContext):
        val = self.visit(ctx.expr())
        if isinstance(val, list):
            return [-v for v in val]
        return -val

    # ── postfix ───────────────────────────────────────────────────────────────

    def visitIndexExpr(self, ctx: TrezParser.IndexExprContext):
        obj = self.visit(ctx.postfix())
        idx = self.visit(ctx.expr())
        if isinstance(obj, (list, str)):
            if not isinstance(idx, int):
                idx = int(idx)
            if idx < 0 or idx >= len(obj):
                raise TrezRuntimeError(f"Índice {idx} fuera de rango (tamaño {len(obj)}).")
            return obj[idx]
        if isinstance(obj, dict):
            key = idx if isinstance(idx, str) else str(idx)
            if key not in obj:
                raise TrezRuntimeError(f"Clave '{key}' no existe en el diccionario.")
            return obj[key]
        raise TrezRuntimeError("El operador [] requiere lista, texto o diccionario.")

    def visitMethodCallExpr(self, ctx: TrezParser.MethodCallExprContext):
        method      = ctx.ID().getText()
        module_name = ctx.postfix().getText()
        args        = [self.visit(r) for r in ctx.rhs()]

        # Namespace dispatch — check module name BEFORE evaluating postfix
        if module_name in _NAMESPACES:
            ns = _NAMESPACES[module_name]
            if method not in ns:
                raise TrezRuntimeError(
                    f"El módulo '{module_name}' no tiene la función '{method}'."
                )
            return ns[method](args)

        obj = self.visit(ctx.postfix())
        return self._dispatch_method(obj, method, args)

    def _dispatch_method(self, obj, method, args):
        # ── list ──
        if isinstance(obj, list):
            if method == 'append':   return obj + [args[0]]
            if method == 'head':
                if not obj: raise TrezRuntimeError("head() en lista vacía.")
                return obj[0]
            if method == 'tail':     return obj[1:]
            if method == 'len':      return len(obj)
            if method == 'contains': return args[0] in obj
            if method == 'reverse':  return obj[::-1]
            if method == 'get':
                idx = int(args[0])
                if idx < 0 or idx >= len(obj):
                    raise TrezRuntimeError(f"Índice {idx} fuera de rango.")
                return obj[idx]
            if method == 'slice':
                return obj[int(args[0]):int(args[1])]
            raise TrezRuntimeError(f"Lista no tiene método '{method}'.")

        # ── dict ──
        if isinstance(obj, dict):
            if method == 'get':
                key = args[0] if isinstance(args[0], str) else str(args[0])
                if key not in obj: raise TrezRuntimeError(f"Clave '{key}' no existe.")
                return obj[key]
            if method == 'keys':   return list(obj.keys())
            if method == 'values': return list(obj.values())
            if method == 'has':
                key = args[0] if isinstance(args[0], str) else str(args[0])
                return key in obj
            if method == 'set':
                key = args[0] if isinstance(args[0], str) else str(args[0])
                new_d = dict(obj)
                new_d[key] = args[1]
                return new_d
            raise TrezRuntimeError(f"Diccionario no tiene método '{method}'.")

        # ── Queue ──
        if isinstance(obj, TrezQueue):
            if method == 'enqueue': return obj.enqueue(args[0])
            if method == 'dequeue':
                val, new_q = obj.dequeue()
                return [val, new_q]
            if method == 'peek':    return obj.peek()
            if method == 'isEmpty': return obj.is_empty()
            if method == 'size':    return obj.size()
            if method == 'toList':  return obj.to_list()
            raise TrezRuntimeError(f"Queue no tiene método '{method}'.")

        # ── Stack ──
        if isinstance(obj, TrezStack):
            if method == 'push':    return obj.push(args[0])
            if method == 'pop':
                val, new_s = obj.pop()
                return [val, new_s]
            if method == 'peek':    return obj.peek()
            if method == 'isEmpty': return obj.is_empty()
            if method == 'size':    return obj.size()
            if method == 'toList':  return obj.to_list()
            raise TrezRuntimeError(f"Stack no tiene método '{method}'.")

        # ── string ──
        if isinstance(obj, str):
            if method == 'len':      return len(obj)
            if method == 'contains': return args[0] in obj
            raise TrezRuntimeError(f"Texto no tiene método '{method}'.")

        raise TrezRuntimeError(f"El objeto no soporta métodos (tipo: {type(obj).__name__}).")

    # ── function call ─────────────────────────────────────────────────────────

    def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        args = [self.visit(r) for r in ctx.rhs()]

        # ── I/O ──
        if func_name == 'leer':     return read_file_doz(args[0])
        if func_name == 'usar':
            ruta = args[0]
            if not os.path.isabs(ruta):
                ruta = os.path.join(os.path.dirname(__file__), ruta)
            if not os.path.exists(ruta):
                raise TrezRuntimeError(f"usar(): archivo '{ruta}' no encontrado.")
            from antlr4 import FileStream as _FS, CommonTokenStream as _CTS
            from parser.TrezLexer import TrezLexer as _Lex
            from parser.TrezParser import TrezParser as _Par
            _stream = _FS(ruta, encoding='utf-8')
            _lexer  = _Lex(_stream)
            _tokens = _CTS(_lexer)
            _parser = _Par(_tokens)
            _tree   = _parser.program()
            saved_depth = self._call_depth
            self._call_depth = 1
            self.visit(_tree)
            self._call_depth = saved_depth
            return None
        if func_name == 'escribir': return write_file_doz(args[0], args[1])
        if func_name in ('mostrar', 'print'):
            print(args[0])
            return None

        # ── structures ──
        if func_name == 'Queue': return make_queue()
        if func_name == 'Stack': return make_stack()

        # ── collection utils ──
        if func_name == 'len':
            obj = args[0]
            if isinstance(obj, (list, str)):              return len(obj)
            if isinstance(obj, (TrezQueue, TrezStack)):   return obj.size()
            raise TrezRuntimeError("len() requiere lista, texto o estructura.")
        if func_name == 'append':
            if not isinstance(args[0], list): raise TrezRuntimeError("append() requiere lista.")
            return args[0] + [args[1]]
        if func_name == 'head':
            if not isinstance(args[0], list) or not args[0]:
                raise TrezRuntimeError("head() requiere lista no vacía.")
            return args[0][0]
        if func_name == 'tail':
            if not isinstance(args[0], list): raise TrezRuntimeError("tail() requiere lista.")
            return args[0][1:]
        if func_name == 'keys':
            if not isinstance(args[0], dict): raise TrezRuntimeError("keys() requiere diccionario.")
            return list(args[0].keys())
        if func_name == 'values':
            if not isinstance(args[0], dict): raise TrezRuntimeError("values() requiere diccionario.")
            return list(args[0].values())
        if func_name == 'range':
            if len(args) == 1: return list(_range_doz(0, int(args[0]), 1))
            if len(args) == 2: return list(_range_doz(int(args[0]), int(args[1]), 1))
            return list(_range_doz(int(args[0]), int(args[1]), int(args[2])))
        if func_name == 'str': return str(args[0])
        if func_name == 'num':
            try:
                v = float(str(args[0]))
                return int(v) if v == int(v) else v
            except Exception:
                raise TrezRuntimeError(f"num() no pudo convertir '{args[0]}' a número.")

        # ── math ──
        math_map = {
            'relu':      lambda: math_utilsdoz.relu(args[0]),
            'sigmoid':   lambda: math_utilsdoz.sigmoid(args[0]),
            'dot':       lambda: math_utilsdoz.dot(args[0], args[1]),
            'transpose': lambda: math_utilsdoz.transpose(args[0]),
            'mse':       lambda: math_utilsdoz.mse(args[0], args[1]),
            'mse_grad':  lambda: math_utilsdoz.mse_grad(args[0], args[1]),
            'abs':       lambda: math_utilsdoz.abs_doz(args[0]),
            'sqrt':      lambda: math_utilsdoz.sqrt_doz(args[0]),
            'pow':       lambda: math_utilsdoz.pow_doz(args[0], args[1]),
            'exp':       lambda: math_utilsdoz.exp_doz(args[0]),
            'log':       lambda: math_utilsdoz.log_doz(args[0]),
            'sin':       lambda: math_utilsdoz.sin_doz(args[0]),
            'cos':       lambda: math_utilsdoz.cos_doz(args[0]),
            'tan':       lambda: math_utilsdoz.tan_doz(args[0]),
            'factorial': lambda: math_utilsdoz.factorial_doz(args[0]),
        }
        if func_name in math_map:
            return math_map[func_name]()

        # ── user-defined function, lambda, or builtin ──
        fn = self.env.get(func_name)
        if isinstance(fn, (TrezFunction, TrezLambda, TrezBuiltin)):
            return self._apply(fn, args)
        raise TrezRuntimeError(f"'{func_name}' no es una función.")

    def _call_function(self, fn: TrezFunction, args):
        if len(args) != len(fn.params):
            raise TrezRuntimeError(
                f"'{fn.name}' espera {len(fn.params)} arg(s), recibió {len(args)}."
            )
        call_env = Environment(fn.env)
        for param, val in zip(fn.params, args):
            call_env.set(param, val)
        call_env.set(fn.name, fn)  # self-reference for recursion
        saved = self.env
        self.env = call_env
        self._call_depth += 1
        result = None
        try:
            for stmt in fn.body_ctx.statement():
                self.visit(stmt)
        except ReturnSignal as r:
            result = r.value
        finally:
            self.env = saved
            self._call_depth -= 1
        return result

    def _apply(self, fn, args):
        """Unified call for TrezFunction, TrezLambda, and TrezBuiltin."""
        if isinstance(fn, TrezBuiltin):
            return fn.fn(*args)
        if isinstance(fn, TrezFunction):
            return self._call_function(fn, args)
        if isinstance(fn, TrezLambda):
            call_env = Environment(fn.env)
            call_env.set(fn.param, args[0])
            saved = self.env
            self.env = call_env
            self._call_depth += 1
            try:
                result = self.visit(fn.body_ctx)
            finally:
                self.env = saved
                self._call_depth -= 1
            return result
        raise TrezRuntimeError(
            f"|> requiere una función en el lado derecho, recibió {type(fn).__name__}."
        )


# ── native range (zero external deps) ────────────────────────────────────────

def _range_doz(start, stop, step):
    if step == 0:
        raise TrezRuntimeError("range() step no puede ser 0.")
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        yield i
        i += step
