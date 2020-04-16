#-----------------------------------------
class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        ClaseEjemplo.varia = val

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)

#-----------------------------------------
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

try:
    print(objetoEjemplo.b)
except AttributeError:
    pass

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)

#-----------------------------------------
