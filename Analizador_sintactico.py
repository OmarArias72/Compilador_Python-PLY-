from Analizador_lexico import tokens
import ply.yacc as yacc
from Analizador_lexico import analizador
import ast

resultado_gramatica=[]
revision_gramatica=False
errores_gramatica=[]
resultado=""
term_gramatica=[]
precedencia=(
    ('right',"ASIGNACION"),
    ('left',"MAYOR","MENOR","MAYOR_IGUAL","MENOR_IGUAL"),
    ('left',"SUMA","RESTA"),
    ('left',"MULTIPLICACION","DIVISION"),
    ('left',"LPAREN","RPAREN")
)
        
def p_programa(p):
    '''programa : vacio 
                      | instrucciones'''
    p[0]=p[1]
def p_instrucciones(p):
    '''instrucciones : INSTRUCCION estructura_for
                     | INSTRUCCION estructura_while
                     | INSTRUCCION estructura_if
                     | INSTRUCCION estructura_elif
                     | INSTRUCCION estructura_else
                     | INSTRUCCION estructura_def
                     | INSTRUCCION estructura_return
                     | INSTRUCCION estructura_print
                     | declaracion_variable
                     | vacio'''
                     
                     
    # resultado_gramatica.append(p[1])
    # print(resultado_gramatica)
    
    if(p[1]=="for"):
        print("VALIDACION FOR")
        if(p[2]!=None and revision_gramatica):
            print("NO SE LLAMA A LA GRAMATICA")
            p[0]=p[1]+p[2]
        else:
            errores_gramatica.append(f"Error de sintaxis en")
    elif(p[1]=="while"):
        if(p[2]!=None):
            p[0]=p[1]+p[2]
        else:
            errores_gramatica.append(f"Error de sintaxis en")
    elif(p[1]=="if"):
        print("VALIDACION IF")
        if(p[2]!=None):
            p[0]=p[1]+p[2]
        else:
            errores_gramatica.append(f"Error de sintaxis en")
            return
    elif(p[1]=="elif"):
        p[0]=p[1]+p[2]
    elif(p[1]=="else"):
        print("VALIDACION ELSE")
        #print(f"vALOR DE {p[1]} y {p[2]}")
        print(f"Tipo de valor de {p[2]} es {type(p[2])}")
        if(p[2]!="None" and p[2]!=None):
            p[0]=p[1]+p[2]
            print(f"Tipo de valor en P[2] {p[2]} ")
        else:
            errores_gramatica.append(f"Error de sintaxis en")
    elif(p[1]=="def"):
        print("validacion DEF")
        p[0]=p[1]+p[2]
    elif(p[1]=="return"):
        print("validacion RETURN")
        p[0]=p[1]+p[2]
    elif(p[1]=="print"):
        p[0]=p[1]+p[2]
    elif(len(p)==2):
        print("EVALUACION DECLARACION VARIABLE")
        p[0]=p[1]
    
        
        


     
def p_estructura_for(p):
    '''estructura_for : IDENTIFICADOR INSTRUCCION INSTRUCCION LPAREN parametros_for RPAREN DOS_PUNTOS'''
    print("SE LLAMA A LA GRAMATICA")
    #revision_gramatica=True
    if(p[5]==None and p[2]=="in" and p[3]=="range"):
        p[0]=p[1]+p[2]+p[3]+p[4]+p[6]+p[7]
    elif(p[2]=="in" and p[3]=="range"):    
        p[0]=p[1]+p[2]+p[3]+p[4]+str(p[5])+p[6]+p[7]
    else:
        errores_gramatica.append("Error")
    
def p_parametros_for(p):
    '''parametros_for : argumento SEPARADOR argumento
                      | argumento
                      | argumento OPERADOR_ARITMETICO argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento
                      | argumento SEPARADOR argumento OPERADOR_ARITMETICO argumento
                      | vacio'''
    if(len(p)==4):
        p[0]=str(p[1])+p[2]+str(p[3])
    elif(len(p)==2):
        if(es_digito(p[1])):
            p[0]=str(p[1])
        else:
            p[0]=p[1]
    elif(len(p)==6):
        p[0]=str(p[1])+p[2]+str(p[3])+p[4]+str(p[5])
    elif(len(p)==8):
        p[0]=str(p[1])+p[2]+str(p[3])+p[4]+str(p[5])+p[6]+str(p[7])

def p_argumento(p):
    '''argumento : IDENTIFICADOR 
                 | NUMERO_ENTERO'''
    if(es_digito(p[1])):
        p[0]=p[1]
    else:
        p[0]=p[1]

def p_estructura_while(p):
    '''estructura_while : expr_condi DOS_PUNTOS
                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS'''
    if(len(p)==3 and p[1]!=None):
        p[0]=p[1]+p[2]
    elif(len(p)==5):
        p[0]=p[1]+p[2]+p[3]+p[4]
    
def p_expr_condi(p):
    '''expr_condi : LPAREN argumento OPERADOR_COMPARACION argumento RPAREN
                  | argumento OPERADOR_COMPARACION argumento
                  | LPAREN expr_arit OPERADOR_COMPARACION argumento RPAREN'''
    # print("ESTRUCTURA IF")
    # resultado_gramatica.append(p[0])
    # print(resultado_gramatica)
    # resultado_gramatica.append(p[1])
    # print(resultado_gramatica)


    if(len(p)==6 and p[2]!=None):
        p[0]=p[1]+str(p[2])+p[3]+str(p[4])+p[5]
    elif(len(p)==4):
        
        p[0]=str(p[1])+p[2]+str(p[3])
       
def p_estructura_if(p):
    '''estructura_if :  expr_condi DOS_PUNTOS
                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS'''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    elif(len(p)==5):
        p[0]=p[1]+p[2]+p[3]+p[4]

def p_estructura_else(p):
    '''estructura_else : DOS_PUNTOS'''
    print(f"VALIDACION ELSE en {p[1]}")
    revision_gramatica=True
    if(len(p)==2 and p[1]!="None"):
        #print("SE REALIZA VALIDACION EN ELSE")
        p[0]=p[1]
        #print(f"P[0] = {p[0]}")
    
def p_estructura_elif(p):
    '''estructura_elif : expr_condi DOS_PUNTOS
                        | expr_condi OPERADOR_LOGICO expr_condi DOS_PUNTOS'''
    
    if(len(p)==3):
        p[0]=p[1]+p[2]
    elif(len(p)==5):
        p[0]=p[1]+p[2]+p[3]+p[4]
        
        
def p_estructura_def(p):
    '''estructura_def : IDENTIFICADOR LPAREN parametros RPAREN DOS_PUNTOS
                      | IDENTIFICADOR LPAREN parametros RPAREN'''
    
    if(len(p)==6):
        if(p[3]==None):
             p[0]=p[1]+p[2]+p[4]+p[5]
        else:
            p[0]=p[1]+p[2]+p[3]+p[4]+p[5]
    elif(len(p)==5):
        if(p[3]==None):
             p[0]=p[1]+p[2]+p[4]
        else:
            p[0]=p[1]+p[2]+p[3]+p[4]
def p_parametros(p):
    '''parametros : IDENTIFICADOR parametros
                    | SEPARADOR IDENTIFICADOR parametros
                    | vacio'''        
    
    # print(f"Valor de p[1] = {p[1]}")
    # if(len(p)==3):
    if(len(p)==3):

        if(p[2]==None):
            p[0]=p[1]
        else:
            p[0]=p[1]+p[2]
    elif(len(p)==4):    
        # p[0]=p[1]+p[2]+str(p[3])
        # resultado_gramatica.append(p[3])
        # print(resultado_gramatica)
        if(p[3]==None):
            p[0]=p[1]+p[2]
        else:
            p[0]=p[1]+p[2]+p[3]

            

def p_estructura_return(p):
    '''estructura_return : expr_arit
                           | expr_condi
                           | IDENTIFICADOR
                           | NUMERO_ENTERO
                           | BOOLEANO
                           | vacio'''
    
    # print("validacion RETURN")
    # resultado_gramatica.append(p[1])
    # print(resultado_gramatica)
    p[0]=str(p[1])

def p_term(p):
    '''term : IDENTIFICADOR
              | NUMERO_ENTERO
              | LPAREN expr_arit RPAREN'''
    print("TERM")
    term_gramatica.append(p[1])
    print(term_gramatica)
    if(len(p)==2):
        p[0]=str(p[1])
    elif(len(p)==4):
        p[0]=p[1]+p[2]+p[3]
    
       
def p_expr_arit(p):
    '''expr_arit : term
                 | term OPERADOR_ARITMETICO term expr_arit
                 | OPERADOR_ARITMETICO term expr_arit
                 | vacio'''
    print("EXPR_ARIT")
    resultado_gramatica.append(p[1])
    print(resultado_gramatica)

    
    if(len(p)==2):
        p[0]=p[1]

    elif(len(p)==4):
        if(p[3]==None):
            p[0]=p[1]+p[2]
        else:
            p[0]=p[1]+p[2]+p[3]  
    elif(len(p)==5):
        print("Se invoca PRODUCCION 2")
        if(p[4]==None):
            p[0]=p[1]+p[2]+p[3]
        else:
            p[0]=p[1]+p[2]+p[3]+p[4]   

# def p_factor(p):
#     '''factor : IDENTIFICADOR
#               | NUMERO_ENTERO
#               | LPAREN expr_arit RPAREN'''
#     # print("FACTOR")
#     # resultado_gramatica.append(p[1])
#     # print(resultado_gramatica)
#     if(len(p)==2):
#         p[0]=str(p[1])
#     elif(len(p)==4):
#         p[0]=p[1]+p[2]+p[3]

def p_estructura_print(p):
    '''estructura_print : LPAREN CADENA RPAREN
                        | LPAREN IDENTIFICADOR RPAREN
                        | LPAREN RPAREN'''
    if(len(p)==4):
        p[0]=p[1]+p[2]+p[3]
    else:
        p[0]=p[1]+p[2]
def p_declaracion_variable(p):
    '''declaracion_variable : IDENTIFICADOR ASIGNACION IDENTIFICADOR
                            | IDENTIFICADOR ASIGNACION NUMERO_ENTERO
                            | IDENTIFICADOR ASIGNACION expr_arit
                            | IDENTIFICADOR ASIGNACION BOOLEANO
                            | IDENTIFICADOR ASIGNACION estructura_def
                            | IDENTIFICADOR ASIGNACION CADENA
                            | IDENTIFICADOR LPAREN parametros RPAREN
                            | IDENTIFICADOR ASIGNACION IDENTIFICADOR LPAREN parametros RPAREN
                            | IDENTIFICADOR'''
    if(len(p)==2):
        p[0]=p[1]
    elif(len(p)==4):
        if(p[3]==None):
            errores_gramatica.append("Error de sintaxis")   
            return
        p[0]=p[1]+p[2]+p[3] 
    elif(len(p)==5):
        if(p[3]==None):
            p[0]=p[1]+p[2]+p[4]
        else:
            p[0]=p[1]+p[2]+p[3]+p[4]
    elif(len(p)==7):
        if(p[5]==None):
            p[0]=p[1]+p[2]+p[3]+p[4]+p[5]+p[6]
        else:
            p[0]=p[1]+p[2]+p[3]+p[4]+p[6]
                   
    

def p_vacio(p):
    '''vacio :'''
    pass     

def p_error(p):
    global resultado_gramatica
    if p:
        #resultado = "Error de sintaxis: en {}".format(str(p.value))
        resultado = "Error de sintaxis: en"
        #print(resultado)
    else:
        #resultado = "Error de sintaxis {}".format(p)
        resultado = "Error de sintaxis en"
        print(resultado)
    resultado_gramatica.append(resultado)
    errores_gramatica.append(resultado)
    
def es_digito(valor):
    try:
        if(valor.isdigit()):
            return True
        else:
            return False
    except AttributeError:
        return False


parser = yacc.yacc()

# print("Analizador sintactico")
# while True:
#    try:
#        s = """else num:"""
#    except EOFError:
#        break
#    if not s: 
#        continue
#    result = parser.parse(s)
#    print(result)
#    break
# print("RESULTADOS GRAMATICA")
# print(resultado_gramatica)
# print("ERRORES GRAMATICA")
# print(errores_gramatica)