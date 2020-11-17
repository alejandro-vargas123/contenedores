#print("prueba python")

import time

n=0
f = open ('archivo.txt','r')
mensaje = f.read()
while mensaje != 'exit':
    f = open ('archivo.txt','r')
    mensaje = f.read()
    print(mensaje)
    #k=open("respuesta.txt","w")
    #k.write(mensaje)
    #k.close()
    f.close()
    time.sleep(1)
    n=n+1

f = open ('archivo.txt','w')
f.write('archivo de prueba')
k=open("respuesta.txt","w")
k.write("Fin del programa\n")
k.close()
