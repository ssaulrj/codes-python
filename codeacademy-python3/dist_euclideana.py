#Función realizada en lenguaje python, (la mayoría tiene la misma lógica y sintaxis)
#Importar libreria para distancia euclideana
from scipy.spatial import distance 

def distanciaspuntos (coordenada_puntoI, coordenada_puntoII):
    #Sacar la distancia euclideana 
    distanciaxy = distance.euclidean( (coordenada_puntoI), (coordenada_puntoII) )
    return distanciaxy

def distanciapromedio (var1,var2,var3):
    return distanciatotal = (var1+var2+var3)/3

#Distancias entre puntos P1 a P2, P1  a P3 & P2 a P3
distancia_punto1_punto2 = distanciaspuntos(coordenada_punto1, coordenada_punto2)
distancia_punto1_punto3 = distanciaspuntos(coordenada_punto1, coordenada_punto3)
distancia_punto2_punto3 = distanciaspuntos(coordenada_punto2, coordenada_punto3)

distancia_promedio = (distancia_punto1_punto2, distancia_punto1_punto3, distancia_punto2_punto3)

#Imprimir resultado
print('La distancia promedio es: ' + distancia_promedio)
