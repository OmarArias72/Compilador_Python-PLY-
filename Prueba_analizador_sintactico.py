from Analizador_lexico import tokens
import ply.yacc as yacc
from Analizador_lexico import analizador
from Analizador_sintactico import errores_gramatica
from Analizador_sintactico import parser
from PILA_COMILLAS import*
from PILA_PARENTESIS import*
import re
import textwrap

errores_sintaxis=[]

identificador_regex = r"[a-zA-Z][a-zA-Z0-9_]*"
estructura_for=r"for"
estructura_while=r"while"
estructura_if=r"if"
estructura_else=r"else"
estructura_elif=r"elif"
estructura_funcion=r"def"
instruccion_return=r"return"
instruccion_print=r"print"

instrucciones=f"{estructura_for}|{estructura_while}|{estructura_if}|{estructura_elif}|{estructura_funcion}"

def evaluar_codigo(cadena):
    while True:
        try:
            s = cadena
        except EOFError:
            break
        if not s: 
            continue
        result = parser.parse(s)
        print(result)
        break
    
def verificar_estructura(caracter,counter):
    coincidencia=re.match(instrucciones,caracter)
    print("Coincidencia if,for,def")
    print(coincidencia)
    if(coincidencia):
        if(validar_parentesis2(caracter)):
            if(caracter.endswith(":")):
                return True
            else:
                errores_sintaxis.append(f"Error de sintaxis: se esperaba : en {caracter} en la linea {counter}")
                return False
        else:
            errores_sintaxis.append(f"Error de sintaxis: paréntesis de apertura/cierre sin paréntesis de apertura/cierre correspondiente en {caracter} en la linea {counter}")
            return False
    print("Coincidencia print")
    coincidencia=re.match(instruccion_print,caracter)
    print(coincidencia)
    if(coincidencia):
        if(validar_parentesis2(caracter)):
            if(validar_comillas(caracter)):
                return True
            else:
                errores_sintaxis.append(f"Error de sintaxis: comillas de apertura/cierre sin comillas de apertura/cierre correspondiente en {caracter} en la linea {counter}")
                return False
        else:
            errores_sintaxis.append(f"Error de sintaxis: paréntesis de apertura/cierre sin paréntesis de apertura/cierre correspondiente en {caracter} en la linea {counter}")
            return False
    return True
    
codigo_prueba="""
if():
print("Hola mundo")
for i in range(,b):
"""
global counter
global errores_contador
errores_contador=0
counter=1
lineas_codigo=[]
def separar_codigo(cadena):
    global counter
    counter=1
    codigo_sin_indentacion=textwrap.dedent(cadena)
    lineas_codigo=codigo_sin_indentacion.split("\n")
    for i in lineas_codigo:
        print(f"Elemento a verificar {i}")
        if(i==""):
            counter +=1
            continue
        if(verificar_estructura(i.strip(),counter)):
            errores_gramatica.clear()
            evaluar_codigo(i.strip())
            print(errores_gramatica)
            if(len(errores_gramatica)!=0):
                errores_sintaxis.append(f"Error de sintaxis en {i} en la linea {counter}")

        counter +=1
   