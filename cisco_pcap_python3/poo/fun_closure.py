#--------------------------------------------------------------------
def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())

#--------------------------------------------------------------------
def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))
	
"""
Este ejemplo muestra una circunstancia más interesante: puedes crear tantos cierres como quieras usando el mismo código. Esto se hace con una función llamada crearcierre(). Nota:

    El primer cierre obtenido de crearcierre() define una herramienta que eleva al cuadrado su argumento.
    El segundo está diseñado para elevar el argumento al cubo.

"""
