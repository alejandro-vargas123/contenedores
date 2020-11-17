#print("prueba python")

import time

n=0
while n<20:
    f = open ('archivo.txt','r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(0.2)
    n=n+1

k=open("respuesta.txt","w")
k.write("Fin del programa\n")
k.close()
