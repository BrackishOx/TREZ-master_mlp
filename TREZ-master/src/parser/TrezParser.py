# Generated from TrezParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,68,8,3,10,3,
        12,3,71,9,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,82,8,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,3,7,102,8,7,3,7,104,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,10,1,10,5,10,120,8,10,10,10,12,10,123,9,10,1,10,1,10,
        1,11,1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,12,1,12,1,12,
        1,12,1,12,3,12,140,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,148,8,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,174,
        8,13,10,13,12,13,177,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,194,8,14,10,14,12,14,197,
        9,14,3,14,199,8,14,1,14,5,14,202,8,14,10,14,12,14,205,9,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,216,8,15,10,15,12,15,
        219,9,15,3,15,221,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,231,8,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,239,8,16,10,16,12,
        16,242,9,16,1,16,1,16,3,16,246,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        5,17,254,8,17,10,17,12,17,257,9,17,1,17,1,17,3,17,261,8,17,1,18,
        1,18,1,18,1,18,1,18,0,2,26,28,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,5,1,0,16,17,2,0,18,19,21,22,2,0,23,23,38,
        39,1,0,36,37,1,0,41,42,291,0,39,1,0,0,0,2,54,1,0,0,0,4,56,1,0,0,
        0,6,62,1,0,0,0,8,77,1,0,0,0,10,86,1,0,0,0,12,90,1,0,0,0,14,93,1,
        0,0,0,16,105,1,0,0,0,18,111,1,0,0,0,20,117,1,0,0,0,22,126,1,0,0,
        0,24,139,1,0,0,0,26,147,1,0,0,0,28,178,1,0,0,0,30,230,1,0,0,0,32,
        245,1,0,0,0,34,260,1,0,0,0,36,262,1,0,0,0,38,40,3,2,1,0,39,38,1,
        0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,
        44,5,0,0,1,44,1,1,0,0,0,45,55,3,4,2,0,46,55,3,6,3,0,47,55,3,8,4,
        0,48,55,3,10,5,0,49,55,3,12,6,0,50,55,3,14,7,0,51,55,3,16,8,0,52,
        55,3,18,9,0,53,55,3,20,10,0,54,45,1,0,0,0,54,46,1,0,0,0,54,47,1,
        0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,
        52,1,0,0,0,54,53,1,0,0,0,55,3,1,0,0,0,56,57,5,1,0,0,57,58,5,42,0,
        0,58,59,5,35,0,0,59,60,3,24,12,0,60,61,5,34,0,0,61,5,1,0,0,0,62,
        63,5,1,0,0,63,64,5,31,0,0,64,69,5,42,0,0,65,66,5,33,0,0,66,68,5,
        42,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        72,1,0,0,0,71,69,1,0,0,0,72,73,5,32,0,0,73,74,5,35,0,0,74,75,3,24,
        12,0,75,76,5,34,0,0,76,7,1,0,0,0,77,78,5,2,0,0,78,79,5,42,0,0,79,
        81,5,27,0,0,80,82,3,22,11,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,
        0,0,0,83,84,5,28,0,0,84,85,3,20,10,0,85,9,1,0,0,0,86,87,5,3,0,0,
        87,88,3,24,12,0,88,89,5,34,0,0,89,11,1,0,0,0,90,91,3,24,12,0,91,
        92,5,34,0,0,92,13,1,0,0,0,93,94,5,4,0,0,94,95,5,27,0,0,95,96,3,24,
        12,0,96,97,5,28,0,0,97,103,3,20,10,0,98,101,5,5,0,0,99,102,3,14,
        7,0,100,102,3,20,10,0,101,99,1,0,0,0,101,100,1,0,0,0,102,104,1,0,
        0,0,103,98,1,0,0,0,103,104,1,0,0,0,104,15,1,0,0,0,105,106,5,6,0,
        0,106,107,5,27,0,0,107,108,3,24,12,0,108,109,5,28,0,0,109,110,3,
        20,10,0,110,17,1,0,0,0,111,112,5,7,0,0,112,113,5,42,0,0,113,114,
        5,8,0,0,114,115,3,24,12,0,115,116,3,20,10,0,116,19,1,0,0,0,117,121,
        5,29,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,
        5,30,0,0,125,21,1,0,0,0,126,131,5,42,0,0,127,128,5,33,0,0,128,130,
        5,42,0,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,23,1,0,0,0,133,131,1,0,0,0,134,135,5,26,0,0,135,136,
        5,42,0,0,136,137,5,20,0,0,137,140,3,24,12,0,138,140,3,26,13,0,139,
        134,1,0,0,0,139,138,1,0,0,0,140,25,1,0,0,0,141,142,6,13,-1,0,142,
        143,5,11,0,0,143,148,3,26,13,8,144,145,5,37,0,0,145,148,3,26,13,
        2,146,148,3,28,14,0,147,141,1,0,0,0,147,144,1,0,0,0,147,146,1,0,
        0,0,148,175,1,0,0,0,149,150,10,11,0,0,150,151,5,12,0,0,151,174,3,
        26,13,12,152,153,10,10,0,0,153,154,5,15,0,0,154,174,3,26,13,11,155,
        156,10,9,0,0,156,157,5,14,0,0,157,174,3,26,13,10,158,159,10,7,0,
        0,159,160,7,0,0,0,160,174,3,26,13,8,161,162,10,6,0,0,162,163,7,1,
        0,0,163,174,3,26,13,7,164,165,10,5,0,0,165,166,7,2,0,0,166,174,3,
        26,13,6,167,168,10,4,0,0,168,169,7,3,0,0,169,174,3,26,13,5,170,171,
        10,3,0,0,171,172,5,13,0,0,172,174,3,26,13,4,173,149,1,0,0,0,173,
        152,1,0,0,0,173,155,1,0,0,0,173,158,1,0,0,0,173,161,1,0,0,0,173,
        164,1,0,0,0,173,167,1,0,0,0,173,170,1,0,0,0,174,177,1,0,0,0,175,
        173,1,0,0,0,175,176,1,0,0,0,176,27,1,0,0,0,177,175,1,0,0,0,178,179,
        6,14,-1,0,179,180,3,30,15,0,180,203,1,0,0,0,181,182,10,3,0,0,182,
        183,5,31,0,0,183,184,3,26,13,0,184,185,5,32,0,0,185,202,1,0,0,0,
        186,187,10,2,0,0,187,188,5,24,0,0,188,189,5,42,0,0,189,198,5,27,
        0,0,190,195,3,24,12,0,191,192,5,33,0,0,192,194,3,24,12,0,193,191,
        1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,199,
        1,0,0,0,197,195,1,0,0,0,198,190,1,0,0,0,198,199,1,0,0,0,199,200,
        1,0,0,0,200,202,5,28,0,0,201,181,1,0,0,0,201,186,1,0,0,0,202,205,
        1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,29,1,0,0,0,205,203,1,
        0,0,0,206,231,5,40,0,0,207,231,5,41,0,0,208,231,5,9,0,0,209,231,
        5,10,0,0,210,211,5,42,0,0,211,220,5,27,0,0,212,217,3,24,12,0,213,
        214,5,33,0,0,214,216,3,24,12,0,215,213,1,0,0,0,216,219,1,0,0,0,217,
        215,1,0,0,0,217,218,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,220,
        212,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,222,231,5,28,0,0,223,
        231,5,42,0,0,224,225,5,27,0,0,225,226,3,24,12,0,226,227,5,28,0,0,
        227,231,1,0,0,0,228,231,3,32,16,0,229,231,3,34,17,0,230,206,1,0,
        0,0,230,207,1,0,0,0,230,208,1,0,0,0,230,209,1,0,0,0,230,210,1,0,
        0,0,230,223,1,0,0,0,230,224,1,0,0,0,230,228,1,0,0,0,230,229,1,0,
        0,0,231,31,1,0,0,0,232,233,5,31,0,0,233,246,5,32,0,0,234,235,5,31,
        0,0,235,240,3,24,12,0,236,237,5,33,0,0,237,239,3,24,12,0,238,236,
        1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,243,
        1,0,0,0,242,240,1,0,0,0,243,244,5,32,0,0,244,246,1,0,0,0,245,232,
        1,0,0,0,245,234,1,0,0,0,246,33,1,0,0,0,247,248,5,29,0,0,248,261,
        5,30,0,0,249,250,5,29,0,0,250,255,3,36,18,0,251,252,5,33,0,0,252,
        254,3,36,18,0,253,251,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,
        256,1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,259,5,30,0,0,259,
        261,1,0,0,0,260,247,1,0,0,0,260,249,1,0,0,0,261,35,1,0,0,0,262,263,
        7,4,0,0,263,264,5,25,0,0,264,265,3,24,12,0,265,37,1,0,0,0,23,41,
        54,69,81,101,103,121,131,139,147,173,175,195,198,201,203,217,220,
        230,240,245,255,260
    ]

class TrezParser ( Parser ):

    grammarFileName = "TrezParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'func'", "'return'", "'if'", 
                     "'else'", "'while'", "'for'", "'in'", "'true'", "'false'", 
                     "'not'", "'|>'", "'**'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<='", "'>='", "'->'", "'<'", "'>'", "'%'", "'.'", 
                     "':'", "'\\'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "LET", "FUNC", "RETURN", "IF", "ELSE", 
                      "WHILE", "FOR", "IN", "TRUE", "FALSE", "NOT", "PIPE", 
                      "POW", "AND", "OR", "EQEQ", "NEQ", "LE", "GE", "ARROW", 
                      "LT", "GT", "MOD", "DOT", "COLON", "BACKSLASH", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COMMA", "SEMI", "EQ", "PLUS", "MINUS", "MUL", "DIV", 
                      "NUMBER", "STRING", "ID", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_let_stmt = 2
    RULE_bind_tuple = 3
    RULE_func_def = 4
    RULE_return_stmt = 5
    RULE_expr_stmt = 6
    RULE_if_stmt = 7
    RULE_while_stmt = 8
    RULE_for_stmt = 9
    RULE_block = 10
    RULE_param_list = 11
    RULE_rhs = 12
    RULE_expr = 13
    RULE_postfix = 14
    RULE_atom = 15
    RULE_array = 16
    RULE_dict = 17
    RULE_dict_entry = 18

    ruleNames =  [ "program", "statement", "let_stmt", "bind_tuple", "func_def", 
                   "return_stmt", "expr_stmt", "if_stmt", "while_stmt", 
                   "for_stmt", "block", "param_list", "rhs", "expr", "postfix", 
                   "atom", "array", "dict", "dict_entry" ]

    EOF = Token.EOF
    LET=1
    FUNC=2
    RETURN=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    IN=8
    TRUE=9
    FALSE=10
    NOT=11
    PIPE=12
    POW=13
    AND=14
    OR=15
    EQEQ=16
    NEQ=17
    LE=18
    GE=19
    ARROW=20
    LT=21
    GT=22
    MOD=23
    DOT=24
    COLON=25
    BACKSLASH=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    LBRACK=31
    RBRACK=32
    COMMA=33
    SEMI=34
    EQ=35
    PLUS=36
    MINUS=37
    MUL=38
    DIV=39
    NUMBER=40
    STRING=41
    ID=42
    WS=43
    LINE_COMMENT=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TrezParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.StatementContext)
            else:
                return self.getTypedRuleContext(TrezParser.StatementContext,i)


        def getRuleIndex(self):
            return TrezParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TrezParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.statement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7836906032862) != 0)):
                    break

            self.state = 43
            self.match(TrezParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let_stmt(self):
            return self.getTypedRuleContext(TrezParser.Let_stmtContext,0)


        def bind_tuple(self):
            return self.getTypedRuleContext(TrezParser.Bind_tupleContext,0)


        def func_def(self):
            return self.getTypedRuleContext(TrezParser.Func_defContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(TrezParser.Return_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(TrezParser.Expr_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(TrezParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(TrezParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(TrezParser.For_stmtContext,0)


        def block(self):
            return self.getTypedRuleContext(TrezParser.BlockContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TrezParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.let_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.bind_tuple()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.func_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.expr_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.if_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.while_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.for_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 53
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(TrezParser.LET, 0)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def EQ(self):
            return self.getToken(TrezParser.EQ, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def SEMI(self):
            return self.getToken(TrezParser.SEMI, 0)

        def getRuleIndex(self):
            return TrezParser.RULE_let_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_stmt" ):
                return visitor.visitLet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def let_stmt(self):

        localctx = TrezParser.Let_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_let_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(TrezParser.LET)
            self.state = 57
            self.match(TrezParser.ID)
            self.state = 58
            self.match(TrezParser.EQ)
            self.state = 59
            self.rhs()
            self.state = 60
            self.match(TrezParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bind_tupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(TrezParser.LET, 0)

        def LBRACK(self):
            return self.getToken(TrezParser.LBRACK, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.ID)
            else:
                return self.getToken(TrezParser.ID, i)

        def RBRACK(self):
            return self.getToken(TrezParser.RBRACK, 0)

        def EQ(self):
            return self.getToken(TrezParser.EQ, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def SEMI(self):
            return self.getToken(TrezParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def getRuleIndex(self):
            return TrezParser.RULE_bind_tuple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBind_tuple" ):
                return visitor.visitBind_tuple(self)
            else:
                return visitor.visitChildren(self)




    def bind_tuple(self):

        localctx = TrezParser.Bind_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bind_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(TrezParser.LET)
            self.state = 63
            self.match(TrezParser.LBRACK)
            self.state = 64
            self.match(TrezParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 65
                self.match(TrezParser.COMMA)
                self.state = 66
                self.match(TrezParser.ID)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(TrezParser.RBRACK)
            self.state = 73
            self.match(TrezParser.EQ)
            self.state = 74
            self.rhs()
            self.state = 75
            self.match(TrezParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TrezParser.FUNC, 0)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TrezParser.BlockContext,0)


        def param_list(self):
            return self.getTypedRuleContext(TrezParser.Param_listContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = TrezParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TrezParser.FUNC)
            self.state = 78
            self.match(TrezParser.ID)
            self.state = 79
            self.match(TrezParser.LPAREN)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 80
                self.param_list()


            self.state = 83
            self.match(TrezParser.RPAREN)
            self.state = 84
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TrezParser.RETURN, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def SEMI(self):
            return self.getToken(TrezParser.SEMI, 0)

        def getRuleIndex(self):
            return TrezParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = TrezParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(TrezParser.RETURN)
            self.state = 87
            self.rhs()
            self.state = 88
            self.match(TrezParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def SEMI(self):
            return self.getToken(TrezParser.SEMI, 0)

        def getRuleIndex(self):
            return TrezParser.RULE_expr_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = TrezParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.rhs()
            self.state = 91
            self.match(TrezParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TrezParser.IF, 0)

        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.BlockContext)
            else:
                return self.getTypedRuleContext(TrezParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(TrezParser.ELSE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(TrezParser.If_stmtContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = TrezParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TrezParser.IF)
            self.state = 94
            self.match(TrezParser.LPAREN)
            self.state = 95
            self.rhs()
            self.state = 96
            self.match(TrezParser.RPAREN)
            self.state = 97
            self.block()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 98
                self.match(TrezParser.ELSE)
                self.state = 101
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 99
                    self.if_stmt()
                    pass
                elif token in [29]:
                    self.state = 100
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TrezParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TrezParser.BlockContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = TrezParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(TrezParser.WHILE)
            self.state = 106
            self.match(TrezParser.LPAREN)
            self.state = 107
            self.rhs()
            self.state = 108
            self.match(TrezParser.RPAREN)
            self.state = 109
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TrezParser.FOR, 0)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def IN(self):
            return self.getToken(TrezParser.IN, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def block(self):
            return self.getTypedRuleContext(TrezParser.BlockContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = TrezParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TrezParser.FOR)
            self.state = 112
            self.match(TrezParser.ID)
            self.state = 113
            self.match(TrezParser.IN)
            self.state = 114
            self.rhs()
            self.state = 115
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TrezParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TrezParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.StatementContext)
            else:
                return self.getTypedRuleContext(TrezParser.StatementContext,i)


        def getRuleIndex(self):
            return TrezParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = TrezParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(TrezParser.LBRACE)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7836906032862) != 0):
                self.state = 118
                self.statement()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(TrezParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.ID)
            else:
                return self.getToken(TrezParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def getRuleIndex(self):
            return TrezParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = TrezParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(TrezParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 127
                self.match(TrezParser.COMMA)
                self.state = 128
                self.match(TrezParser.ID)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrezParser.RULE_rhs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRhs" ):
                return visitor.visitExprRhs(self)
            else:
                return visitor.visitChildren(self)


    class LambdaDefContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BACKSLASH(self):
            return self.getToken(TrezParser.BACKSLASH, 0)
        def ID(self):
            return self.getToken(TrezParser.ID, 0)
        def ARROW(self):
            return self.getToken(TrezParser.ARROW, 0)
        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaDef" ):
                return visitor.visitLambdaDef(self)
            else:
                return visitor.visitChildren(self)



    def rhs(self):

        localctx = TrezParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rhs)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = TrezParser.LambdaDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(TrezParser.BACKSLASH)
                self.state = 135
                self.match(TrezParser.ID)
                self.state = 136
                self.match(TrezParser.ARROW)
                self.state = 137
                self.rhs()
                pass
            elif token in [9, 10, 11, 27, 29, 31, 37, 40, 41, 42]:
                localctx = TrezParser.ExprRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrezParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PostfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix(self):
            return self.getTypedRuleContext(TrezParser.PostfixContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpr" ):
                return visitor.visitPostfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class PipeOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def PIPE(self):
            return self.getToken(TrezParser.PIPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipeOp" ):
                return visitor.visitPipeOp(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def AND(self):
            return self.getToken(TrezParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def MUL(self):
            return self.getToken(TrezParser.MUL, 0)
        def DIV(self):
            return self.getToken(TrezParser.DIV, 0)
        def MOD(self):
            return self.getToken(TrezParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def LT(self):
            return self.getToken(TrezParser.LT, 0)
        def LE(self):
            return self.getToken(TrezParser.LE, 0)
        def GT(self):
            return self.getToken(TrezParser.GT, 0)
        def GE(self):
            return self.getToken(TrezParser.GE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def EQEQ(self):
            return self.getToken(TrezParser.EQEQ, 0)
        def NEQ(self):
            return self.getToken(TrezParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def POW(self):
            return self.getToken(TrezParser.POW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpr" ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(TrezParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(TrezParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(TrezParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)

        def OR(self):
            return self.getToken(TrezParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(TrezParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TrezParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = TrezParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 142
                self.match(TrezParser.NOT)
                self.state = 143
                self.expr(8)
                pass
            elif token in [37]:
                localctx = TrezParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(TrezParser.MINUS)
                self.state = 145
                self.expr(2)
                pass
            elif token in [9, 10, 27, 29, 31, 40, 41, 42]:
                localctx = TrezParser.PostfixExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.postfix(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 173
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = TrezParser.PipeOpContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 150
                        self.match(TrezParser.PIPE)
                        self.state = 151
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = TrezParser.OrExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 152
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 153
                        self.match(TrezParser.OR)
                        self.state = 154
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = TrezParser.AndExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 155
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 156
                        self.match(TrezParser.AND)
                        self.state = 157
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = TrezParser.EqExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 159
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = TrezParser.CompareExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 162
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7077888) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = TrezParser.MulDivExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 165
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 824642109440) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = TrezParser.AddSubExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 168
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(5)
                        pass

                    elif la_ == 8:
                        localctx = TrezParser.PowExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 171
                        self.match(TrezParser.POW)
                        self.state = 172
                        self.expr(4)
                        pass

             
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrezParser.RULE_postfix

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AtomExprContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(TrezParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class IndexExprContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix(self):
            return self.getTypedRuleContext(TrezParser.PostfixContext,0)

        def LBRACK(self):
            return self.getToken(TrezParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(TrezParser.RBRACK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallExprContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix(self):
            return self.getTypedRuleContext(TrezParser.PostfixContext,0)

        def DOT(self):
            return self.getToken(TrezParser.DOT, 0)
        def ID(self):
            return self.getToken(TrezParser.ID, 0)
        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)
        def rhs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.RhsContext)
            else:
                return self.getTypedRuleContext(TrezParser.RhsContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpr" ):
                return visitor.visitMethodCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def postfix(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TrezParser.PostfixContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_postfix, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TrezParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 179
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = TrezParser.IndexExprContext(self, TrezParser.PostfixContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                        self.state = 181
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 182
                        self.match(TrezParser.LBRACK)
                        self.state = 183
                        self.expr(0)
                        self.state = 184
                        self.match(TrezParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = TrezParser.MethodCallExprContext(self, TrezParser.PostfixContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                        self.state = 186
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 187
                        self.match(TrezParser.DOT)
                        self.state = 188
                        self.match(TrezParser.ID)
                        self.state = 189
                        self.match(TrezParser.LPAREN)
                        self.state = 198
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7836906032640) != 0):
                            self.state = 190
                            self.rhs()
                            self.state = 195
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==33:
                                self.state = 191
                                self.match(TrezParser.COMMA)
                                self.state = 192
                                self.rhs()
                                self.state = 197
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 200
                        self.match(TrezParser.RPAREN)
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrezParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(TrezParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(TrezParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(TrezParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(TrezParser.ArrayContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(TrezParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpr" ):
                return visitor.visitNumExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class DictExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dict_(self):
            return self.getTypedRuleContext(TrezParser.DictContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictExpr" ):
                return visitor.visitDictExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)
        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)

        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)
        def LPAREN(self):
            return self.getToken(TrezParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(TrezParser.RPAREN, 0)
        def rhs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.RhsContext)
            else:
                return self.getTypedRuleContext(TrezParser.RhsContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = TrezParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = TrezParser.NumExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(TrezParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = TrezParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(TrezParser.STRING)
                pass

            elif la_ == 3:
                localctx = TrezParser.BoolExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(TrezParser.TRUE)
                pass

            elif la_ == 4:
                localctx = TrezParser.BoolExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(TrezParser.FALSE)
                pass

            elif la_ == 5:
                localctx = TrezParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(TrezParser.ID)
                self.state = 211
                self.match(TrezParser.LPAREN)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7836906032640) != 0):
                    self.state = 212
                    self.rhs()
                    self.state = 217
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==33:
                        self.state = 213
                        self.match(TrezParser.COMMA)
                        self.state = 214
                        self.rhs()
                        self.state = 219
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 222
                self.match(TrezParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = TrezParser.VarExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.match(TrezParser.ID)
                pass

            elif la_ == 7:
                localctx = TrezParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 224
                self.match(TrezParser.LPAREN)
                self.state = 225
                self.rhs()
                self.state = 226
                self.match(TrezParser.RPAREN)
                pass

            elif la_ == 8:
                localctx = TrezParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 228
                self.array()
                pass

            elif la_ == 9:
                localctx = TrezParser.DictExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 229
                self.dict_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(TrezParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(TrezParser.RBRACK, 0)

        def rhs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.RhsContext)
            else:
                return self.getTypedRuleContext(TrezParser.RhsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def getRuleIndex(self):
            return TrezParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = TrezParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(TrezParser.LBRACK)
                self.state = 233
                self.match(TrezParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(TrezParser.LBRACK)
                self.state = 235
                self.rhs()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==33:
                    self.state = 236
                    self.match(TrezParser.COMMA)
                    self.state = 237
                    self.rhs()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243
                self.match(TrezParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TrezParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TrezParser.RBRACE, 0)

        def dict_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(TrezParser.Dict_entryContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TrezParser.COMMA)
            else:
                return self.getToken(TrezParser.COMMA, i)

        def getRuleIndex(self):
            return TrezParser.RULE_dict

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)




    def dict_(self):

        localctx = TrezParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(TrezParser.LBRACE)
                self.state = 248
                self.match(TrezParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(TrezParser.LBRACE)
                self.state = 250
                self.dict_entry()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==33:
                    self.state = 251
                    self.match(TrezParser.COMMA)
                    self.state = 252
                    self.dict_entry()
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 258
                self.match(TrezParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dict_entryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(TrezParser.COLON, 0)

        def rhs(self):
            return self.getTypedRuleContext(TrezParser.RhsContext,0)


        def STRING(self):
            return self.getToken(TrezParser.STRING, 0)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def getRuleIndex(self):
            return TrezParser.RULE_dict_entry

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict_entry" ):
                return visitor.visitDict_entry(self)
            else:
                return visitor.visitChildren(self)




    def dict_entry(self):

        localctx = TrezParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dict_entry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 263
            self.match(TrezParser.COLON)
            self.state = 264
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        self._predicates[14] = self.postfix_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

    def postfix_sempred(self, localctx:PostfixContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




