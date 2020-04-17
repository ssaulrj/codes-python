stream = open("tzop.txt", "rt", encoding = "utf-8") # se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto de archivo
print(stream.read()) # se imprime el contenido del archivo

from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))
