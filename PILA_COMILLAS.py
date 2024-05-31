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

def validar_comillas(cadena):
    pila = Stack()
    for caracter in cadena:
        if caracter == '"':
            if pila.is_empty() or pila.peek() != '"':
                pila.push(caracter)
            else:
                pila.pop()
    return pila.is_empty()


# a="print(\"Hola\")"
# b="print(\"Hola)"
# print(validar_comillas(a))
# if(validar_comillas(b)):
#     print(f"Estrucutra {b} valida")
# else:
#     print(f"Estrucutra {b} invalida")
