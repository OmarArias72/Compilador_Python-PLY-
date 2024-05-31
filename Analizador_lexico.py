import ply.lex as lex

resultado_lexema=[]

# tokens=["OPERAODR_ARITMETICO","OPERADOR_BOOLEANO","OPERADOR_LOGICO","BOOLEANO","CHAR","ASIGNACION",
#         "NUMERO_ENTERO","LPAREN","RPAREN","IDENTIFICADOR","CADENA","SEPARADOR","DOS_PUNTOS",
#         "PRINT","IF","ELSE","ELIF","FOR","IN","RANGE","WHILE","DEF","RETURN"]
tokens=["OPERADOR_ARITMETICO","OPERADOR_COMPARACION","OPERADOR_LOGICO","BOOLEANO","CHAR","ASIGNACION",
        "NUMERO_ENTERO","LPAREN","RPAREN","IDENTIFICADOR","CADENA","SEPARADOR","DOS_PUNTOS",
        "INSTRUCCION"]

# t_PRINT=r"print"
# t_IF=r"if"
# t_ELSE=r"else"
# t_ELIF=r"elif"
# t_FOR=r"for"
# t_IN=r"in"
# t_RANGE=r"range"
# t_WHILE=r"while"
# t_DEF=r"def"
# t_RETURN=r"return"

t_SEPARADOR=r","
t_DOS_PUNTOS=r":"
t_LPAREN=r"\("
t_RPAREN=r"\)"
t_OPERADOR_COMPARACION=r">=|<=|!=|==|>|<"
t_ASIGNACION=r"="


def t_INSTRUCCION(t):
    r"print | if | else  | elif | for | in | range | while | def | return"
    return t

def t_BOOLEANO(t):
    r"True | False"
    return t

def t_OPERADOR_ARITMETICO(t):
    r"\+ | - | \* | / | %"
    return t

def t_OPERADOR_LOGICO(t):
    r"and | or | not"
    return t

# def OPERADOR_LOGICO(t):
#     r"> | < | >= | <= | == | !="
#     return t
def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    #print("2"+t.value)
    return t

def t_IDENTIFICADOR(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    return t

def t_NUMERO_FLOTANTE(t):
    r"\d*\.\d*"
    t.value=float(t.value)
    return t

def t_NUMERO_ENTERO(t):
    r"(0 | [1-9][0-9]*)"
    t.value=int(t.value)
    return t



#t_ASIGNACION =r"="

def t_CHAR(t):
    r"'.'"
    t.value = t.value[1]  
    return t

def t_COMMENT(t):
    r"\#.*"
    pass
def t_IGNORE(t):
    r" \t"
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error( t):
    global resultado_lexema
    estado = "Token no valido en la Linea {:4} Valor {:4} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)
    
analizador=lex.lex()
# data="""#Omar Arias Dominguez
#         print(\"Hola Mundo\")
#         a=b>=6
#         if(num!=0):
#         if(2%2)
#    """
# analizador.input(data)

# #Tokenize
# while True:
#    tok = analizador.token()
#    print(tok)
#    if not tok: 
#        break      # No more input

