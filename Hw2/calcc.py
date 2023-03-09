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
### HW2
### 9 March 2023

### drops list operations from hw1, converting everything else into a compiler
### for JCoCo instead of an interpreter

import sys # so I can output to stderr

## dictionaries to track locals, constants, and globals to put in .casm file
casm_locals = {None:0}
casm_constants = {None:0} 
casm_globals = {'print':0}
## list of instructions to be used in .casm file 
casm_instructions = [] 

# Add a list of tuples encoding casm instructions to the global list.
def append_instructions(lst):
    global casm_instructions
    casm_instructions += lst


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

## added INTD (i.e //) and % to precedence
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/', 'INTD', '%'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}

def p_statement_assign(p):
    'statement : NAME "=" expression'
    append_instructions([('STORE_FAST', locals_index(p[1]))])


def p_statement_expr(p):                          
    'statement : expression'
    append_instructions([
        ('LOAD_GLOBAL', 0),
        ('ROT_TWO',),
        ('CALL_FUNCTION', 1),
        ('POP_TOP',),
    ])


def p_expression_binop(p): 
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '%' expression
                  | expression INTD expression
                  | expression '/' expression '''
    if p[2] == '+':
        append_instructions([('BINARY_ADD',)])                       
    elif p[2] == '-':
        append_instructions([('BINARY_SUBTRACT',)])    
    elif p[2] == '*':
        append_instructions([('BINARY_MULTIPLY',)])
    elif p[2] == '%':
        append_instructions([('BINARY_MODULO',)])
    elif p[2] == '//':
        append_instructions([('BINARY_FLOOR_DIVIDE',)]) 
    elif p[2] == '/':
        append_instructions([('BINARY_TRUE_DIVIDE',)]) 


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    append_instructions([('LOAD_CONST', constants_index(-1)),])
    append_instructions([('BINARY_MULTIPLY',)])

def p_expression_group(p):
    "expression : '(' expression ')'"
    # do nothing, expression is already on stack

def p_expression_number(p):         
    "expression : NUMBER"           
    append_instructions([('LOAD_CONST', constants_index(int(p[1]))),])

def p_expression_name(p):
    "expression : NAME"
    try:
        append_instructions([('LOAD_FAST', locals_index(p[1])),])
    except LookupError:
        print("Undefined name '%s'" % p[1], file = sys.stderr)


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value, file = sys.stderr)
    else:
        print("Syntax error at EOF", file = sys.stderr)


import ply.yacc as yacc
parser = yacc.yacc()


## If key is in not in dict d then add it with a value len(d),
## returning (possibly updated) d and the value corresponding to key.
def dict_idx(d, key):
    idx = d.get(key)
    if idx == None:
        idx = len(d)
        d[key] = idx
    return d, idx

## finds k in casm_constants and returns its index, 
## if it's not there dict_idx will add it
def constants_index(k):
    global casm_constants
    casm_constants, idx = dict_idx(casm_constants, k) 
    return idx

def locals_index(k):
    global casm_locals
    casm_locals, idx = dict_idx(casm_locals, k)
    return idx

def print_casm_header_data(hdr_tag, hdr_dict):
    if hdr_dict:
        rdict = dict([(idx, k) for (k, idx) in hdr_dict.items()])
        print(hdr_tag + ':', ', '.join(map(str, rdict.values())))

# tup = (instr) or (instr, arg) or (label, instr, arg)
# TODO better formatting
def print_casm_instr(tup):
    if len(tup) < 3: print('\t', end='')
    print('\t'.join(map(str,tup)))

def print_casm():
    append_instructions([('LOAD_CONST', 0), ('RETURN_VALUE',),])
    print('Function: main/0')
    print_casm_header_data('Constants', casm_constants)
    print_casm_header_data('Locals', casm_locals)
    print_casm_header_data('Globals', casm_globals)
    print('BEGIN')
    for tup in casm_instructions: print_casm_instr(tup)
    print("END")

while True:
    try:
        s = input()
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
print_casm()

### Note: python calcc.py < samplei.txt > out.casm
### above line in terminal will call calcc.py on samplei.txt, and store the
### result in out.casm, which can be run using jcoco to see result