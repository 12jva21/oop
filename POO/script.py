#Autor: Jairo vega Anacona

#Motivo: Primera actividad en clase

#1: 

texto = input("Hola. Ingrese un texto: ")
print(texto)


#2: Realizar las tablas de multiplicar del numero que se ingrese usando una función: 


def tablasMultiplicar(n):
	i=0
	while (i<11):
		print(n*i)
		i+=1

n = int(input("Ingrese un numero para darle las tablas del 1 al 10: "))
tablasMultiplicar(n)


#3: Usar una funcion para sacer el factorial de un numero:

def factorial(m):
	k=1
	mostrarFactorial=1
	while (k<m+1):
		mostrarFactorial*=k
		k+=1
	print(mostrarFactorial) 	

m = int(input("Ingrese un numero para sacarle el factorial: "))
factorial(m)


