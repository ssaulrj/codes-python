#-----------------------------------------
class Uno:
    def hazlo(self):
        print("hazlo de Uno")

    def haz_algo(self):
        self.hazlo()

class Dos(Uno):
    def hazlo(self):
        print("hazlo de Dos")

uno = Uno()
dos = Dos()

uno.haz_algo()
dos.haz_algo()

#-----------------------------------------
import time

class VehiculoOruga:
    def control_de_pista(izquierda, alto):
        pass

    def girar(izquierda):
        control_de_pista(izquierda, True)
        time.sleep(0.25)
        control_de_pista(izquierda, False)


class VehiculoTerrestre:
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def girar(izquierda):
        girar_ruedas_delanteras(izquierda, True)
        time.sleep(0.25)
        girar_ruedas_delanteras(izquierda, False)

#-----------------------------------------
import time

class Vehiculo:
    def cambiardireccion(izquierda, on):
        pass

    def girar(izquierda):
        cambiardireccion(izquierda, True)
        time.sleep(0.25)
        cambiardireccion(izquierda, False)

class VehiculoOruga(Vehiculo):
    def control_de_pista(izquierda, alto):
        pass

    def cambiardireccion(izquierda, on):
        control_de_pista(izquierda, on)

class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def cambiardireccion(izquierda, on):
        girar_ruedas_delanteras(izquierda, on)
        
#-----------------------------------------
import time

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)

#-----------------------------------------

#-----------------------------------------
