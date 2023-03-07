
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/INTD%rightUMINUSINTD NAME NUMBERstatement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'%\' expression\n                  | expression INTD expression\n                  | expression \'/\' expression expression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : NUMBERexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,7,8,9,10,11,12,13,],[2,15,15,15,15,15,15,15,15,15,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,],[4,-12,9,4,4,-11,4,4,4,4,4,4,4,-9,-12,9,9,-3,-4,-5,-6,-7,-8,-10,]),'(':([0,4,5,7,8,9,10,11,12,13,],[5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,7,8,9,10,11,12,13,],[6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,3,6,14,15,17,18,19,20,21,22,23,24,],[0,-12,-2,-11,-9,-12,-1,-3,-4,-5,-6,-7,-8,-10,]),'=':([2,],[7,]),'+':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-12,8,-11,-9,-12,8,8,-3,-4,-5,-6,-7,-8,-10,]),'*':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-12,10,-11,-9,-12,10,10,10,10,-5,-6,-7,-8,-10,]),'%':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-12,11,-11,-9,-12,11,11,11,11,-5,-6,-7,-8,-10,]),'INTD':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-12,12,-11,-9,-12,12,12,12,12,-5,-6,-7,-8,-10,]),'/':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-12,13,-11,-9,-12,13,13,13,13,-5,-6,-7,-8,-10,]),')':([6,14,15,16,18,19,20,21,22,23,24,],[-11,-9,-12,24,-3,-4,-5,-6,-7,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,7,8,9,10,11,12,13,],[3,14,16,17,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','calcc.py',66),
  ('statement -> expression','statement',1,'p_statement_expr','calcc.py',71),
  ('expression -> expression + expression','expression',3,'p_expression_binop','calcc.py',76),
  ('expression -> expression - expression','expression',3,'p_expression_binop','calcc.py',77),
  ('expression -> expression * expression','expression',3,'p_expression_binop','calcc.py',78),
  ('expression -> expression % expression','expression',3,'p_expression_binop','calcc.py',79),
  ('expression -> expression INTD expression','expression',3,'p_expression_binop','calcc.py',80),
  ('expression -> expression / expression','expression',3,'p_expression_binop','calcc.py',81),
  ('expression -> - expression','expression',2,'p_expression_uminus','calcc.py',97),
  ('expression -> ( expression )','expression',3,'p_expression_group','calcc.py',101),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcc.py',105),
  ('expression -> NAME','expression',1,'p_expression_name','calcc.py',110),
]