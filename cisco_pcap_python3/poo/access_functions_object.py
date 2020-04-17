class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

#-------------------------------
class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

obj = Nivel3()

print(obj.var, obj.fun())

#-------------------------------
class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha):
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())
