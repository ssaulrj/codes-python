#Este código está destinado a imprimir la cadena "Dentro del ciclo" y el valor almacenado en la variable contador durante un ciclo dado exactamente cinco veces. Una vez que la condición se haya cumplido (la variable contador ha alcanzado 0), se sale del ciclo y aparece el mensaje "Fuera del ciclo". así como el valor almacenado en contador se imprime.

contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)

#compact
contador=5
while contador:
    print("Dentro del ciclo.", contador)
    contador -= 1
print("Fuera del ciclo", contador)
