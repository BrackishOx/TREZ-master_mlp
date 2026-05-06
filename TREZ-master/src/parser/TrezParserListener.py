# Generated from TrezParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TrezParser import TrezParser
else:
    from TrezParser import TrezParser

# This class defines a complete listener for a parse tree produced by TrezParser.
class TrezParserListener(ParseTreeListener):

    # Enter a parse tree produced by TrezParser#program.
    def enterProgram(self, ctx:TrezParser.ProgramContext):
        pass

    # Exit a parse tree produced by TrezParser#program.
    def exitProgram(self, ctx:TrezParser.ProgramContext):
        pass


    # Enter a parse tree produced by TrezParser#statement.
    def enterStatement(self, ctx:TrezParser.StatementContext):
        pass

    # Exit a parse tree produced by TrezParser#statement.
    def exitStatement(self, ctx:TrezParser.StatementContext):
        pass


    # Enter a parse tree produced by TrezParser#let_stmt.
    def enterLet_stmt(self, ctx:TrezParser.Let_stmtContext):
        pass

    # Exit a parse tree produced by TrezParser#let_stmt.
    def exitLet_stmt(self, ctx:TrezParser.Let_stmtContext):
        pass


    # Enter a parse tree produced by TrezParser#expr_stmt.
    def enterExpr_stmt(self, ctx:TrezParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by TrezParser#expr_stmt.
    def exitExpr_stmt(self, ctx:TrezParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by TrezParser#if_stmt.
    def enterIf_stmt(self, ctx:TrezParser.If_stmtContext):
        pass

    # Exit a parse tree produced by TrezParser#if_stmt.
    def exitIf_stmt(self, ctx:TrezParser.If_stmtContext):
        pass


    # Enter a parse tree produced by TrezParser#while_stmt.
    def enterWhile_stmt(self, ctx:TrezParser.While_stmtContext):
        pass

    # Exit a parse tree produced by TrezParser#while_stmt.
    def exitWhile_stmt(self, ctx:TrezParser.While_stmtContext):
        pass


    # Enter a parse tree produced by TrezParser#block.
    def enterBlock(self, ctx:TrezParser.BlockContext):
        pass

    # Exit a parse tree produced by TrezParser#block.
    def exitBlock(self, ctx:TrezParser.BlockContext):
        pass


    # Enter a parse tree produced by TrezParser#AndExpr.
    def enterAndExpr(self, ctx:TrezParser.AndExprContext):
        pass

    # Exit a parse tree produced by TrezParser#AndExpr.
    def exitAndExpr(self, ctx:TrezParser.AndExprContext):
        pass


    # Enter a parse tree produced by TrezParser#StringExpr.
    def enterStringExpr(self, ctx:TrezParser.StringExprContext):
        pass

    # Exit a parse tree produced by TrezParser#StringExpr.
    def exitStringExpr(self, ctx:TrezParser.StringExprContext):
        pass


    # Enter a parse tree produced by TrezParser#BoolExpr.
    def enterBoolExpr(self, ctx:TrezParser.BoolExprContext):
        pass

    # Exit a parse tree produced by TrezParser#BoolExpr.
    def exitBoolExpr(self, ctx:TrezParser.BoolExprContext):
        pass


    # Enter a parse tree produced by TrezParser#PowExpr.
    def enterPowExpr(self, ctx:TrezParser.PowExprContext):
        pass

    # Exit a parse tree produced by TrezParser#PowExpr.
    def exitPowExpr(self, ctx:TrezParser.PowExprContext):
        pass


    # Enter a parse tree produced by TrezParser#OrExpr.
    def enterOrExpr(self, ctx:TrezParser.OrExprContext):
        pass

    # Exit a parse tree produced by TrezParser#OrExpr.
    def exitOrExpr(self, ctx:TrezParser.OrExprContext):
        pass


    # Enter a parse tree produced by TrezParser#ArrayExpr.
    def enterArrayExpr(self, ctx:TrezParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by TrezParser#ArrayExpr.
    def exitArrayExpr(self, ctx:TrezParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by TrezParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:TrezParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by TrezParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:TrezParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by TrezParser#NumExpr.
    def enterNumExpr(self, ctx:TrezParser.NumExprContext):
        pass

    # Exit a parse tree produced by TrezParser#NumExpr.
    def exitNumExpr(self, ctx:TrezParser.NumExprContext):
        pass


    # Enter a parse tree produced by TrezParser#CompareExpr.
    def enterCompareExpr(self, ctx:TrezParser.CompareExprContext):
        pass

    # Exit a parse tree produced by TrezParser#CompareExpr.
    def exitCompareExpr(self, ctx:TrezParser.CompareExprContext):
        pass


    # Enter a parse tree produced by TrezParser#EqExpr.
    def enterEqExpr(self, ctx:TrezParser.EqExprContext):
        pass

    # Exit a parse tree produced by TrezParser#EqExpr.
    def exitEqExpr(self, ctx:TrezParser.EqExprContext):
        pass


    # Enter a parse tree produced by TrezParser#VarExpr.
    def enterVarExpr(self, ctx:TrezParser.VarExprContext):
        pass

    # Exit a parse tree produced by TrezParser#VarExpr.
    def exitVarExpr(self, ctx:TrezParser.VarExprContext):
        pass


    # Enter a parse tree produced by TrezParser#ParenExpr.
    def enterParenExpr(self, ctx:TrezParser.ParenExprContext):
        pass

    # Exit a parse tree produced by TrezParser#ParenExpr.
    def exitParenExpr(self, ctx:TrezParser.ParenExprContext):
        pass


    # Enter a parse tree produced by TrezParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:TrezParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by TrezParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:TrezParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by TrezParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:TrezParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by TrezParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:TrezParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by TrezParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:TrezParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by TrezParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:TrezParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by TrezParser#array.
    def enterArray(self, ctx:TrezParser.ArrayContext):
        pass

    # Exit a parse tree produced by TrezParser#array.
    def exitArray(self, ctx:TrezParser.ArrayContext):
        pass



del TrezParser