
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left,left+-left*/INTD%rightUMINUSINTD NAME NUMBERstatement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'%\' expression\n                  | expression \',\' expression\n                  | expression INTD expression\n                  | expression \'/\' expression list : \'(\' expression \')\' list : \'(\' expression \',\' \')\'list : \'(\' \',\' \')\'\n            | \'(\' \')\' expression : listexpression : \'-\' expression %prec UMINUSexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,7,8,9,10,11,12,13,14,15,30,],[2,17,17,17,17,17,17,17,17,17,17,17,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,],[4,-17,10,4,-14,-16,4,4,4,4,4,4,4,4,4,-15,-17,10,-13,10,-3,-4,-5,-6,10,-8,-9,-10,4,-12,-11,]),'NUMBER':([0,4,7,8,9,10,11,12,13,14,15,30,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'(':([0,4,7,8,9,10,11,12,13,14,15,30,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'$end':([1,2,3,5,6,16,17,19,21,22,23,24,25,26,27,28,29,31,32,],[0,-17,-2,-14,-16,-15,-17,-13,-1,-3,-4,-5,-6,-7,-8,-9,-10,-12,-11,]),'=':([2,],[8,]),'+':([2,3,5,6,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,9,-14,-16,-15,-17,9,-13,9,-3,-4,-5,-6,9,-8,-9,-10,-12,-11,]),'*':([2,3,5,6,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,11,-14,-16,-15,-17,11,-13,11,11,11,-5,-6,11,-8,-9,-10,-12,-11,]),'%':([2,3,5,6,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,12,-14,-16,-15,-17,12,-13,12,12,12,-5,-6,12,-8,-9,-10,-12,-11,]),',':([2,3,5,6,7,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,13,-14,-16,20,-15,-17,30,-13,13,-3,-4,-5,-6,-7,-8,-9,-10,-12,-11,]),'INTD':([2,3,5,6,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,14,-14,-16,-15,-17,14,-13,14,14,14,-5,-6,14,-8,-9,-10,-12,-11,]),'/':([2,3,5,6,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,],[-17,15,-14,-16,-15,-17,15,-13,15,15,15,-5,-6,15,-8,-9,-10,-12,-11,]),')':([5,6,7,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,],[-14,-16,19,-15,-17,29,-13,31,-3,-4,-5,-6,-7,-8,-9,-10,32,-12,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,7,8,9,10,11,12,13,14,15,30,],[3,16,18,21,22,23,24,25,26,27,28,26,]),'list':([0,4,7,8,9,10,11,12,13,14,15,30,],[5,5,5,5,5,5,5,5,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','calcx.py',64),
  ('statement -> expression','statement',1,'p_statement_expr','calcx.py',69),
  ('expression -> expression + expression','expression',3,'p_expression_binop','calcx.py',118),
  ('expression -> expression - expression','expression',3,'p_expression_binop','calcx.py',119),
  ('expression -> expression * expression','expression',3,'p_expression_binop','calcx.py',120),
  ('expression -> expression % expression','expression',3,'p_expression_binop','calcx.py',121),
  ('expression -> expression , expression','expression',3,'p_expression_binop','calcx.py',122),
  ('expression -> expression INTD expression','expression',3,'p_expression_binop','calcx.py',123),
  ('expression -> expression / expression','expression',3,'p_expression_binop','calcx.py',124),
  ('list -> ( expression )','list',3,'p_list','calcx.py',173),
  ('list -> ( expression , )','list',4,'p_list_comma','calcx.py',181),
  ('list -> ( , )','list',3,'p_empty_list','calcx.py',189),
  ('list -> ( )','list',2,'p_empty_list','calcx.py',190),
  ('expression -> list','expression',1,'p_expression_list','calcx.py',195),
  ('expression -> - expression','expression',2,'p_expression_uminus','calcx.py',200),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcx.py',205),
  ('expression -> NAME','expression',1,'p_expression_name','calcx.py',210),
]
