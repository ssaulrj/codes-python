numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

###
