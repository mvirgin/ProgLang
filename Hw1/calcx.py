# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------
import sys

tokens = (
    'NAME', 'NUMBER', 'INTD', 
)

literals = ['=', '+', '-', '*', '/', '(', ')', '%', ',']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_INTD = '//'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    ## output in standard error - do the same for other error messages
    print("Illegal character '%s'" % t.value[0], file=sys.stderr)
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1]) # this is output, goes to standard output


def p_expression_binop(p): #** add more for LIST + LIST, etc
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '%' expression
                  | expression INTD expression
                  | expression ',' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '//':
        p[0] = p[1] // p[3]
    elif p[2] == ',':
        elements = [p[1],p[3]]
        noParen = ', '.join((map(str,elements))) # could be issue w byte for byte ... , list operators - map as ints?
        p[0] = noParen
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    
def flatten(data):
    if isinstance(data, tuple):
        if len(data) == 0:
            return ()
        else:
            return flatten(data[0]) + flatten(data[1:])
    else:
        return (data,)

def p_list(p):
    '''LIST : '(' expression ',' expression ')' 
            | '(' expression ',' expression ',' ')' ''' # - it has to be ( exp , elements , ) where elements --> ( expression , expression ) - can leave List --> same thing tho
    p[0] = (p[2], p[4])

def p_singleton(p):
    "LIST : '(' expression ',' ')'"
  #  a = 1
  #  t1 = (1,2)
  #  t2 = (a, t1)
  #  t3 = flatten(t2) -- LOOKS LIKE THIS WILL WORK W/ ELEMENTS SOLUTION ABOVE
  #  print(t2, t3) 
    p[0] = (p[2],)
    
def p_elist(p):
    '''LIST : '(' ',' ')'
            | '(' ')' '''
    p[0] = ()

def p_expression_list(p):
    "expression : LIST"
    p[0] = p[1]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2] # concatenate p1 and p3 onto as well**


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1], file = sys.stderr)
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value, file = sys.stderr)
    else:
        print("Syntax error at EOF", file = sys.stderr)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input()
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)