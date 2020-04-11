def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

#--------------------------------_compact

def esUnTriangulo_compact(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(esUnTriangulo_compact(1, 1, 1))
print(esUnTriangulo_compact(1, 1, 3))

#------------------------------------------_compact_compact

def esUnTriangulo_compact_compact (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo_compact_compact (1, 1, 1))
print(esUnTriangulo_compact_compact (1, 1, 3))
