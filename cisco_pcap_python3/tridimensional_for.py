habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]

print(habitaciones)

#El primer índice (0 a 2) selecciona uno de los edificios; 
#el segundo(0 a 14) selecciona el piso, 
#el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas. 

habitaciones[1][9][13] = True 
habitaciones[0][4][1] = False 

vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1
    
print(vacante)
