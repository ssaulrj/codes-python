from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# --------------------------------------------------------------- bf.read()
# ingresa aquí el código que lee los bytes del stream
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

--------------------------------------------------------------- bf.read(x) , x = numero de bytes a leer
# ingresa aquí el código que lee los bytes del stream
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerr(e.errno))
