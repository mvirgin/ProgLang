# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

### additions by

### Matthew Virgin
### Professor Chawathe
### COS 301
### HW1
### 25 February 2023

import sys # so I can output to stderr

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

## added ',' INTD (i.e //) and % to precedence
precedence = (
    ('left', ','),
    ('left', '+', '-'),
    ('left', '*', '/', 'INTD', '%'),
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


### functions to make list/tuple operations easier
## could have 1 func that takes operator as arg - problem for later
def listAdd(a,b):               # assuming lists of equal length
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    result = tuple(result)
    return result

def listSub(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    result = tuple(result)
    return result

def listMult(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    result = tuple(result)
    return result

def listDiv(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] / b[i])
    result = tuple(result)
    return result

def listMod(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] % b[i])
    result = tuple(result)
    return result

def listINTD(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] // b[i])
    result = tuple(result)
    return result

def p_expression_binop(p): 
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '%' expression
                  | expression ',' expression
                  | expression INTD expression
                  | expression '/' expression '''
    if p[2] == '+':            
        if type(p[1]) == tuple:
            p[0] = listAdd(p[1],p[3])
        else:               
            p[0] = p[1] + p[3]
    elif p[2] == '-':
        if type(p[1]) == tuple:
            p[0] = listSub(p[1],p[3])
        else:
            p[0] = p[1] - p[3]
    elif p[2] == '*':
        if type(p[1]) == tuple:
            p[0] = listMult(p[1],p[3])
        else:
            p[0] = p[1] * p[3]
    elif p[2] == '%':
        if type(p[1]) == tuple:
            p[0] = listMod(p[1],p[3])
        else:
            p[0] = p[1] % p[3]
    elif p[2] == ',':
        p[0] = (p[1], p[3])
    elif p[2] == '//':
        if type(p[1]) == tuple:
            p[0] = listINTD(p[1],p[3])
        else:
            p[0] = p[1] // p[3]
    elif p[2] == '/':
        if type(p[1]) == tuple:
            p[0] = listDiv(p[1],p[3])
        else:
            p[0] = p[1] / p[3]
    
## flattens a tuple - useful for p_list
## idea from:
## https://stackoverflow.com/questions/18500541/how-to-flatten-a-tuple-in-python
def flatten(data):                   # takes a piece of data
    if isinstance(data, tuple):      # checks if that data is in the tuple
        if len(data) == 0:      
            return ()                # return empty if no data
        else:
                                    ## else, recursively call on rest of data
            return flatten(data[0]) + flatten(data[1:])
    else:
        return (data,)               # done when data no longer nested


def p_list(p):                    
    "list : '(' expression ')' "
    if type(p[2]) == int:           # i.e just an expression, should drop ()
        p[0] = p[2]
    else:
        p[0] = flatten((p[2]))


def p_list_comma(p):
    "list : '(' expression ',' ')'"
    if type(p[2]) == int:           # i.e singleton
        p[0] = (p[2],)
    else:
        p[0] = flatten((p[2]))
    

def p_empty_list(p):
    '''list : '(' ',' ')'
            | '(' ')' '''
    p[0] = ()


def p_expression_list(p):
    "expression : list"
    p[0] = p[1]


def p_expression_uminus(p):                   
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


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

### Note: python calcx.py < samplei.txt > out.txt
### above line in terminal will call calcx.py on samplei.txt, and store the
### result in out.txt