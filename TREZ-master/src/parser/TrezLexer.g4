lexer grammar TrezLexer;

// Keywords
LET:       'let';
FUNC:      'func';
RETURN:    'return';
IF:        'if';
ELSE:      'else';
WHILE:     'while';
FOR:       'for';
IN:        'in';
TRUE:      'true';
FALSE:     'false';
NOT:       'not';

// Symbols — longer tokens must come first to avoid ambiguity
PIPE:      '|>';
POW:       '**';
AND:       '&&';
OR:        '||';
EQEQ:     '==';
NEQ:       '!=';
LE:        '<=';
GE:        '>=';
ARROW:     '->';
LT:        '<';
GT:        '>';
MOD:       '%';
DOT:       '.';
COLON:     ':';
BACKSLASH: '\\';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA:  ',';
SEMI:   ';';
EQ:     '=';
PLUS:   '+';
MINUS:  '-';
MUL:    '*';
DIV:    '/';

// Literals
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n\\] | '\\' .)* '"';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip
WS:           [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
