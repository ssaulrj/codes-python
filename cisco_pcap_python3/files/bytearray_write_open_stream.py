data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i
    print(data[i])

for b in data:
    print(hex(b))
  
#----------------------------------------------------------------------------------------------write
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

#----------------------------------------------------------------------------------------------open
# ingresa aquí el código que lee los bytes del stream
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))
