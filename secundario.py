#print("prueba python")

import time

print("Escriba exit para salir")
entrada = ''

while entrada != 'exit':
    entrada = input("Ingrese algo para cambiar el archivo.txt ")
    f = open('archivo.txt','w')
    f.write(entrada)
    f.close()

escritura = open('archivo.txt','w')
escritura.write(entrada)
print("Adios")
