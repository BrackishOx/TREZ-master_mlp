parser grammar TrezParser;

options { tokenVocab = TrezLexer; }

program: statement+ EOF;

statement
    : let_stmt
    | bind_tuple
    | func_def
    | return_stmt
    | expr_stmt
    | if_stmt
    | while_stmt
    | for_stmt
    | block
    ;

let_stmt:    LET ID EQ rhs SEMI;
bind_tuple:  LET LBRACK ID (COMMA ID)* RBRACK EQ rhs SEMI;
func_def:    FUNC ID LPAREN param_list? RPAREN block;
return_stmt: RETURN rhs SEMI;
expr_stmt:   rhs SEMI;
if_stmt:     IF LPAREN rhs RPAREN block (ELSE (if_stmt | block))?;
while_stmt:  WHILE LPAREN rhs RPAREN block;
for_stmt:    FOR ID IN rhs block;
block:       LBRACE statement* RBRACE;

param_list: ID (COMMA ID)*;

// rhs = lambda | expr — lambda captures everything to its right
rhs
    : BACKSLASH ID ARROW rhs   # LambdaDef
    | expr                     # ExprRhs
    ;

// Binary expressions — lower alternatives = lower precedence in ANTLR4
expr
    : expr PIPE expr                       # PipeOp
    | expr OR expr                         # OrExpr
    | expr AND expr                        # AndExpr
    | NOT expr                             # NotExpr
    | expr (EQEQ | NEQ) expr              # EqExpr
    | expr (LT | LE | GT | GE) expr       # CompareExpr
    | expr (MUL | DIV | MOD) expr         # MulDivExpr
    | expr (PLUS | MINUS) expr            # AddSubExpr
    | expr POW expr                        # PowExpr
    | MINUS expr                           # UnaryMinusExpr
    | postfix                              # PostfixExpr
    ;

// Postfix — index and method/namespace calls, highest precedence
postfix
    : postfix LBRACK expr RBRACK                            # IndexExpr
    | postfix DOT ID LPAREN (rhs (COMMA rhs)*)? RPAREN     # MethodCallExpr
    | atom                                                   # AtomExpr
    ;

atom
    : NUMBER                                                # NumExpr
    | STRING                                                # StringExpr
    | TRUE                                                  # BoolExpr
    | FALSE                                                 # BoolExpr
    | ID LPAREN (rhs (COMMA rhs)*)? RPAREN                 # FuncCallExpr
    | ID                                                    # VarExpr
    | LPAREN rhs RPAREN                                     # ParenExpr
    | array                                                 # ArrayExpr
    | dict                                                  # DictExpr
    ;

array: LBRACK RBRACK
     | LBRACK rhs (COMMA rhs)* RBRACK
     ;

dict: LBRACE RBRACE
    | LBRACE dict_entry (COMMA dict_entry)* RBRACE
    ;

dict_entry: (STRING | ID) COLON rhs;
