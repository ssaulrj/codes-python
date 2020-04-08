#Escrito en lenguaje Python

def arregloARRandENT (arreglos, ent)
   apariciones = arreglos.count(ent)
   return str(apariciones) 

arreglo = [2,3,4,3,2,1]
ent = 3

print('Apariciones: ' + arregloARRandENT(arreglo, ent))
