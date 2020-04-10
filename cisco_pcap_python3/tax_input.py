ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso > 85528:
    impuesto = 14839.02 +(85528*0.32)
elif ingreso <= 85528:
    impuesto = (ingreso*.18) - 556.02

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
