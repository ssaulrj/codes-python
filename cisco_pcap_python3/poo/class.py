#---------------------------------------------------------------------- clase
class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        print("¡Hola!")

objetoPila = Pila()    # instanciando el objeto

#---------------------------------------------------------------------- uso de (.)
class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))

#----------------------------------------------------------------------
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())
