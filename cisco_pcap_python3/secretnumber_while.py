numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while True:
    intnum = int(input('Ingresa un numero entero: '))
    if intnum == numeroSecreto:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
