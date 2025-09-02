#Autor: Jairo vega Anacona
#Motivo: Tarea 1

#Encontrar los numeros primos entre cero y 50
#El operador clave es el modulo

contador=0

for i in range (2,50):
    for k in range (1,i+1):
        if(i%k == 0):
            contador+=1
    if(contador==2):
        print(i)
    contador=0


