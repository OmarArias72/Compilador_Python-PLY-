class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def validar_parentesis(cadena):
    pila = Stack()
    for caracter in cadena:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()
        elif caracter == ':':
            break  # No se necesita seguir procesando después de ':'
    return pila.is_empty() and cadena.endswith(':')

def validar_parentesis2(cadena):
    pila = Stack()
    for caracter in cadena:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()
    return pila.is_empty()

# a="if (num):"
# b="if (num:"
# print(validar_parentesis(a))
# if(validar_parentesis(b)):
#     print(f"Estrucutra {b} valida")
# else:
#     print(f"Estrucutra {b} invalida")
