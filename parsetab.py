
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION BOOLEANO CADENA CHAR DOS_PUNTOS IDENTIFICADOR INSTRUCCION LPAREN NUMERO_ENTERO OPERADOR_ARITMETICO OPERADOR_COMPARACION OPERADOR_LOGICO RPAREN SEPARADORprograma : vacio \n                      | instruccionesinstrucciones : INSTRUCCION estructura_for\n                     | INSTRUCCION estructura_while\n                     | INSTRUCCION estructura_if\n                     | INSTRUCCION estructura_elif\n                     | INSTRUCCION estructura_else\n                     | INSTRUCCION estructura_def\n                     | INSTRUCCION estructura_return\n                     | INSTRUCCION estructura_print\n                     | declaracion_variable\n                     | expr_arit\n                     | vacioestructura_for : IDENTIFICADOR INSTRUCCION INSTRUCCION LPAREN parametros_for RPAREN DOS_PUNTOSparametros_for : argumento SEPARADOR argumento\n                      | argumento\n                      | argumento OPERADOR_ARITMETICO argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento\n                      | argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento\n                      | vacioargumento : IDENTIFICADOR \n                 | NUMERO_ENTEROestructura_while : expr_condi DOS_PUNTOS\n                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOSexpr_condi : LPAREN argumento OPERADOR_COMPARACION argumento RPAREN\n                  | argumento OPERADOR_COMPARACION argumento\n                  | LPAREN expr_arit OPERADOR_COMPARACION argumento RPARENestructura_if :  expr_condi DOS_PUNTOS\n                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOSestructura_else : DOS_PUNTOSestructura_elif : expr_condi DOS_PUNTOS\n                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOSestructura_def : IDENTIFICADOR LPAREN parametros RPAREN DOS_PUNTOS\n                      | IDENTIFICADOR LPAREN parametros RPARENparametros : IDENTIFICADOR parametros\n                    | SEPARADOR IDENTIFICADOR parametros\n                    | vacioestructura_return : expr_arit\n                           | expr_condi\n                           | IDENTIFICADOR\n                           | NUMERO_ENTERO\n                           | BOOLEANO\n                           | vacioexpr_arit : term expr_arit\n                 | OPERADOR_ARITMETICO term expr_arit\n                 | vacioterm : IDENTIFICADOR\n              | NUMERO_ENTERO\n              | LPAREN expr_arit RPARENestructura_print : LPAREN CADENA RPAREN\n                        | LPAREN IDENTIFICADOR RPAREN\n                        | LPAREN RPARENdeclaracion_variable : IDENTIFICADOR ASIGNACION IDENTIFICADOR\n                            | IDENTIFICADOR ASIGNACION NUMERO_ENTERO\n                            | IDENTIFICADOR ASIGNACION expr_arit\n                            | IDENTIFICADOR ASIGNACION BOOLEANO\n                            | IDENTIFICADOR ASIGNACION estructura_def\n                            | IDENTIFICADOR ASIGNACION CADENA\n                            | IDENTIFICADOR LPAREN parametros RPAREN\n                            | IDENTIFICADOR ASIGNACION IDENTIFICADOR LPAREN parametros RPAREN\n                            | IDENTIFICADORvacio :'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,29,32,33,34,35,39,44,47,48,49,50,51,52,57,58,61,62,67,68,69,72,75,78,86,87,88,89,93,],[-61,0,-1,-2,-61,-11,-12,-46,-47,-61,-3,-4,-5,-6,-7,-8,-9,-10,-39,-29,-38,-37,-40,-41,-42,-61,-45,-46,-43,-61,-51,-22,-46,-47,-54,-55,-56,-57,-48,-44,-49,-50,-20,-21,-25,-58,-33,-23,-32,-24,-26,-33,-14,]),'INSTRUCCION':([0,20,36,],[4,36,59,]),'IDENTIFICADOR':([0,4,7,8,9,10,11,20,21,25,29,30,33,35,37,40,43,45,46,47,48,53,55,57,63,64,66,70,73,74,80,91,92,96,97,100,],[7,20,-46,-47,33,33,33,-46,40,-47,47,53,-46,33,53,-46,-47,67,67,-46,-47,53,73,-48,67,67,80,53,53,67,-46,67,67,67,67,67,]),'OPERADOR_ARITMETICO':([0,4,7,8,9,10,20,21,25,29,33,35,40,43,47,48,57,66,67,68,80,84,94,99,],[11,11,-46,-47,11,11,-46,11,-47,11,-46,11,-46,-47,-46,-47,-48,11,-20,-21,-46,92,96,100,]),'NUMERO_ENTERO':([0,4,7,8,9,10,11,20,21,25,29,33,35,40,43,45,46,47,48,57,63,64,66,74,80,91,92,96,97,100,],[8,25,-46,-47,8,8,8,-46,43,-47,48,-46,8,-46,-47,68,68,-46,-47,-48,68,68,43,68,-46,68,68,68,68,68,]),'LPAREN':([0,4,7,8,9,10,11,20,21,25,29,33,35,40,43,45,47,48,57,59,66,80,],[9,21,30,-47,9,9,9,37,9,-47,9,-46,9,-46,-47,66,70,-47,-48,74,9,-46,]),'DOS_PUNTOS':([4,23,65,67,68,69,75,87,88,89,90,],[22,44,78,-20,-21,-25,86,-24,-26,86,93,]),'BOOLEANO':([4,29,],[26,50,]),'ASIGNACION':([7,],[29,]),'RPAREN':([8,9,10,21,30,31,32,33,34,35,37,38,40,42,43,53,54,56,57,58,60,67,68,70,71,73,74,76,77,81,82,83,84,85,94,98,101,],[-47,-61,-61,39,-61,57,-45,-46,-43,-61,-61,61,62,57,-47,-61,72,-36,-48,-44,75,-20,-21,-61,-34,-61,-61,87,88,89,-35,90,-16,-19,-15,-18,-17,]),'OPERADOR_COMPARACION':([8,10,20,21,25,28,32,33,34,35,40,41,42,43,57,58,66,67,68,79,80,],[-47,-61,-20,-61,-21,46,-45,-46,-43,-61,-20,63,64,-21,-48,-44,-61,-20,-21,64,-20,]),'CADENA':([21,29,],[38,52,]),'OPERADOR_LOGICO':([23,67,68,69,87,88,],[45,-20,-21,-25,-24,-26,]),'SEPARADOR':([30,37,53,67,68,70,73,84,95,],[55,55,55,-20,-21,55,55,91,97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vacio':([0,4,9,10,21,29,30,35,37,53,66,70,73,74,],[2,27,32,32,32,32,56,32,56,56,32,56,56,85,]),'instrucciones':([0,],[3,]),'declaracion_variable':([0,],[5,]),'expr_arit':([0,4,9,10,21,29,35,66,],[6,24,31,34,42,49,58,79,]),'term':([0,4,9,10,11,21,29,35,66,],[10,10,10,10,35,10,10,10,10,]),'estructura_for':([4,],[12,]),'estructura_while':([4,],[13,]),'estructura_if':([4,],[14,]),'estructura_elif':([4,],[15,]),'estructura_else':([4,],[16,]),'estructura_def':([4,29,],[17,51,]),'estructura_return':([4,],[18,]),'estructura_print':([4,],[19,]),'expr_condi':([4,45,],[23,65,]),'argumento':([4,21,45,46,63,64,66,74,91,92,96,97,100,],[28,41,28,69,76,77,41,84,94,95,98,99,101,]),'parametros':([30,37,53,70,73,],[54,60,71,81,82,]),'parametros_for':([74,],[83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> vacio','programa',1,'p_programa','Analizador_sintactico.py',19),
  ('programa -> instrucciones','programa',1,'p_programa','Analizador_sintactico.py',20),
  ('instrucciones -> INSTRUCCION estructura_for','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',23),
  ('instrucciones -> INSTRUCCION estructura_while','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',24),
  ('instrucciones -> INSTRUCCION estructura_if','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',25),
  ('instrucciones -> INSTRUCCION estructura_elif','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',26),
  ('instrucciones -> INSTRUCCION estructura_else','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',27),
  ('instrucciones -> INSTRUCCION estructura_def','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',28),
  ('instrucciones -> INSTRUCCION estructura_return','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',29),
  ('instrucciones -> INSTRUCCION estructura_print','instrucciones',2,'p_instrucciones','Analizador_sintactico.py',30),
  ('instrucciones -> declaracion_variable','instrucciones',1,'p_instrucciones','Analizador_sintactico.py',31),
  ('instrucciones -> expr_arit','instrucciones',1,'p_instrucciones','Analizador_sintactico.py',32),
  ('instrucciones -> vacio','instrucciones',1,'p_instrucciones','Analizador_sintactico.py',33),
  ('estructura_for -> IDENTIFICADOR INSTRUCCION INSTRUCCION LPAREN parametros_for RPAREN DOS_PUNTOS','estructura_for',7,'p_estructura_for','Analizador_sintactico.py',72),
  ('parametros_for -> argumento SEPARADOR argumento','parametros_for',3,'p_parametros_for','Analizador_sintactico.py',79),
  ('parametros_for -> argumento','parametros_for',1,'p_parametros_for','Analizador_sintactico.py',80),
  ('parametros_for -> argumento OPERADOR_ARITMETICO argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento','parametros_for',7,'p_parametros_for','Analizador_sintactico.py',81),
  ('parametros_for -> argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento','parametros_for',5,'p_parametros_for','Analizador_sintactico.py',82),
  ('parametros_for -> vacio','parametros_for',1,'p_parametros_for','Analizador_sintactico.py',83),
  ('argumento -> IDENTIFICADOR','argumento',1,'p_argumento','Analizador_sintactico.py',97),
  ('argumento -> NUMERO_ENTERO','argumento',1,'p_argumento','Analizador_sintactico.py',98),
  ('estructura_while -> expr_condi DOS_PUNTOS','estructura_while',2,'p_estructura_while','Analizador_sintactico.py',105),
  ('estructura_while -> expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS','estructura_while',4,'p_estructura_while','Analizador_sintactico.py',106),
  ('expr_condi -> LPAREN argumento OPERADOR_COMPARACION argumento RPAREN','expr_condi',5,'p_expr_condi','Analizador_sintactico.py',113),
  ('expr_condi -> argumento OPERADOR_COMPARACION argumento','expr_condi',3,'p_expr_condi','Analizador_sintactico.py',114),
  ('expr_condi -> LPAREN expr_arit OPERADOR_COMPARACION argumento RPAREN','expr_condi',5,'p_expr_condi','Analizador_sintactico.py',115),
  ('estructura_if -> expr_condi DOS_PUNTOS','estructura_if',2,'p_estructura_if','Analizador_sintactico.py',128),
  ('estructura_if -> expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS','estructura_if',4,'p_estructura_if','Analizador_sintactico.py',129),
  ('estructura_else -> DOS_PUNTOS','estructura_else',1,'p_estructura_else','Analizador_sintactico.py',136),
  ('estructura_elif -> expr_condi DOS_PUNTOS','estructura_elif',2,'p_estructura_elif','Analizador_sintactico.py',142),
  ('estructura_elif -> expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS','estructura_elif',4,'p_estructura_elif','Analizador_sintactico.py',143),
  ('estructura_def -> IDENTIFICADOR LPAREN parametros RPAREN DOS_PUNTOS','estructura_def',5,'p_estructura_def','Analizador_sintactico.py',152),
  ('estructura_def -> IDENTIFICADOR LPAREN parametros RPAREN','estructura_def',4,'p_estructura_def','Analizador_sintactico.py',153),
  ('parametros -> IDENTIFICADOR parametros','parametros',2,'p_parametros','Analizador_sintactico.py',166),
  ('parametros -> SEPARADOR IDENTIFICADOR parametros','parametros',3,'p_parametros','Analizador_sintactico.py',167),
  ('parametros -> vacio','parametros',1,'p_parametros','Analizador_sintactico.py',168),
  ('estructura_return -> expr_arit','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',190),
  ('estructura_return -> expr_condi','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',191),
  ('estructura_return -> IDENTIFICADOR','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',192),
  ('estructura_return -> NUMERO_ENTERO','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',193),
  ('estructura_return -> BOOLEANO','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',194),
  ('estructura_return -> vacio','estructura_return',1,'p_estructura_return','Analizador_sintactico.py',195),
  ('expr_arit -> term expr_arit','expr_arit',2,'p_expr_arit','Analizador_sintactico.py',204),
  ('expr_arit -> OPERADOR_ARITMETICO term expr_arit','expr_arit',3,'p_expr_arit','Analizador_sintactico.py',205),
  ('expr_arit -> vacio','expr_arit',1,'p_expr_arit','Analizador_sintactico.py',206),
  ('term -> IDENTIFICADOR','term',1,'p_term','Analizador_sintactico.py',225),
  ('term -> NUMERO_ENTERO','term',1,'p_term','Analizador_sintactico.py',226),
  ('term -> LPAREN expr_arit RPAREN','term',3,'p_term','Analizador_sintactico.py',227),
  ('estructura_print -> LPAREN CADENA RPAREN','estructura_print',3,'p_estructura_print','Analizador_sintactico.py',249),
  ('estructura_print -> LPAREN IDENTIFICADOR RPAREN','estructura_print',3,'p_estructura_print','Analizador_sintactico.py',250),
  ('estructura_print -> LPAREN RPAREN','estructura_print',2,'p_estructura_print','Analizador_sintactico.py',251),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION IDENTIFICADOR','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',257),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION NUMERO_ENTERO','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',258),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION expr_arit','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',259),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION BOOLEANO','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',260),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION estructura_def','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',261),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION CADENA','declaracion_variable',3,'p_declaracion_variable','Analizador_sintactico.py',262),
  ('declaracion_variable -> IDENTIFICADOR LPAREN parametros RPAREN','declaracion_variable',4,'p_declaracion_variable','Analizador_sintactico.py',263),
  ('declaracion_variable -> IDENTIFICADOR ASIGNACION IDENTIFICADOR LPAREN parametros RPAREN','declaracion_variable',6,'p_declaracion_variable','Analizador_sintactico.py',264),
  ('declaracion_variable -> IDENTIFICADOR','declaracion_variable',1,'p_declaracion_variable','Analizador_sintactico.py',265),
  ('vacio -> <empty>','vacio',0,'p_vacio','Analizador_sintactico.py',287),
]