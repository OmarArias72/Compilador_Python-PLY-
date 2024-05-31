import datetime
import re

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

# Formatear la fecha como una cadena
fecha_formateada = "Fecha de creacion: "+fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

#print("La fecha actual es:", fecha_formateada)


#Expresion regular para encabezados
correos_electronicos_regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
numero_regex=r"(\(?\+\d{1,3}\)?\s?)?\d{10}"
nombre_regex=r"[A-Z][a-z]+\s+([A-Z][a-z]+\s+)?[A-Z][a-z]+\s+[A-Z][a-z]+"

#Variables globales
encabezados=[]
texto_escribir=[]
lineas_documentadas=[]

#expresiones regulares para reconocer estructuras y documentarlas
identificador_regex = r"[a-zA-Z][a-zA-Z0-9_]*"
estructura_for=r"for"
estructura_while=r"while"
estructura_if=r"if"
estructura_else=r"else"
estructura_elif=r"elif"
estructura_funcion=r"def"
instruccion_return=r"return"
instruccion_print=r"print"
asignar_funcion=r"[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*[a-zA-Z_][a-zA-Z0-9_]*\((.*?)\)"

def obtener_encabezados(texto):
    encabezados.append(fecha_formateada)
    lineas=texto.split("\n")
    for line in lineas:
        print(f"Elemento a evaluar {line}")
        if(line==""):
            continue
        subcadena=line[1:]
        if(len(encabezados)==4):
            texto_escribir.append(line)
            
        else:
            encabezados.append(encontrar_patron(subcadena))
        
    for elemento in encabezados:
        print(elemento)
        
        
    # for elemento in texto_escribir:
    #     print(f"Linea: {elemento}")
        
def verificar_encabezados():
    count=0
    for i in encabezados:
        print(f"Elemento a evaluar {i}")
        if(i != None):
            count +=1
    if(count==4):
        return True
    else:
        return False     
     
def encontrar_patron(cadena):
    cadena_encontrada=re.search(nombre_regex,cadena)
    if(cadena_encontrada):
        nombre_encontrado=1
        inicio=cadena_encontrada.start()
        end=cadena_encontrada.end()
        cadena_extraida=cadena[inicio:end]
        return cadena_extraida
    
    cadena_encontrada=re.search(numero_regex,cadena)
    if(cadena_encontrada):
        numero_eccontrado=1
        inicio=cadena_encontrada.start()
        end=cadena_encontrada.end()
        cadena_extraida=cadena[inicio:end]
        return cadena_extraida
    
    cadena_encontrada=re.search(correos_electronicos_regex,cadena)
    if(cadena_encontrada):
        correo_encontrado=1
        inicio=cadena_encontrada.start()
        end=cadena_encontrada.end()
        cadena_extraida=cadena[inicio:end]
        return cadena_extraida

def encontrar_patron_codigo(cadena):
    #print(f"Valor a verificar {cadena}\n")
    patron=re.search(instruccion_print,cadena)
    if(patron):
        return f"//La instruccion print realiza la impresion del mensaje/variable en consola//"
    
    patron=re.search(estructura_if,cadena)
    if(patron):
        return f"""//La instruccion if realiza la comprobacion de la condicion para controlar la siguiente instruccion a ejecutar//"""
    patron=re.search(estructura_else,cadena)
    if(patron):
        return f"""//La instruccion else realiza la ejecucion de la siguiente instruccion cuando no se cumple la condicion if//"""
    patron=re.search(estructura_elif,cadena)
    if(patron):
        return f"//La instruccion elif realiza la comprobacion de otra condicion//"
    patron=re.search(estructura_for,cadena)
    if(patron):
        return f"""//La instruccion for permite iterar sobre un valor definido dentro de range() existen dos formas de especificar los parametros. Primera forma: especificar solo un parametro range(a). Segunda forma: especificar dos parametros range(a,b)//"""
    patron=re.search(estructura_while,cadena)
    if(patron):
        return (f"//La instruccion while permite ejecutar una serie de instrucciones siempre y cuando se cumpla una"+ 
    "condicion en caso de que no se cumpla la condicion se sale del ciclo//")
    patron=re.search(estructura_funcion,cadena)
    if(patron):
        return f"""//La instruccion def define una funcion que realiza un conjunto de instrucciones se pueden escribir uno o varios parametros o ninguno por ejemplo def factorial(a,b):, def factorial()//"""
    patron=re.search(instruccion_return,cadena)
    if(patron):
        return (f"//La instruccion return devuelve el control del programa en la linea que se invoco la funcion"+ 
    "ademas puede retornar un valor especificado despues de su declaracion por ejemplo:"+ 
    "return 1, return a*b, return True, etc.//")
    patron=re.search(asignar_funcion,cadena)
    if(patron):
        return f"//La instruccion variable=nombre_funcion permite asignar el valor devuelto por una funcion//"
    patron=re.search(identificador_regex,cadena)
    if(patron):
        return (f"//La siguiente declaracion permite definir una variable/asignar un valor a una variable/asignar/"+ 
    "un valor a traves de una operacion//")


def documentar_lineas():
    lineas_documentadas.append(fecha_formateada)
    lineas_documentadas.append(f"Autor: {encabezados[1]}")
    lineas_documentadas.append(f"Numero telefonico: {encabezados[2]}")
    lineas_documentadas.append(f"Correo electronico: {encabezados[3]}")
    # for encabezado in encabezados:
    #     lineas_documentadas.append(encabezado)
        
    for line in texto_escribir:
        #print(f"ELEMENTO A IMPRIMIR {line}\n")
        if(line.startswith("#")):
            print("SE EXCLUYE COMENTARIO")
            print(f"Comentario contenido: {(subcadena:=line[0:1])}")
            lineas_documentadas.append(line)
            #continue
        else:
            lineas_documentadas.append(encontrar_patron_codigo(line))
            lineas_documentadas.append(line)
            
def limpiar_arreglos():
    lineas_documentadas.clear()
    texto_escribir.clear()
    encabezados.clear()
            
    # for lines in lineas_documentadas:
    #     print(lines)

    
    
cadena_prueba="""
 #Omar Eduardo Arias Dominguez
 #dalba710@gmail.com
 #Comentario
 def calculo_factorial(num):
 #condicion if
    if(num<=0):
        return 0
    resultado = 1
    for n in range(1, num + 1):
        resultado =resultado*n
    return resultado
#Asignacion de numero
numero=5
resultado=calculo_factorial(numero-1)
print(resultado)
"""
# cadena_lineas=cadena_prueba.split("\n")
# obtener_encabezados(cadena_prueba)
# if(not verificar_encabezados()):
#     print(f"No se han obtenido todos los encabezados")

# documentar_lineas()
# for lines in lineas_documentadas:
#         print(lines)