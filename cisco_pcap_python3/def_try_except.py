def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")
