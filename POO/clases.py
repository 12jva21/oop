#Autor: Jairo vega Anacona
#Motivo: Tarea 2


#implementar dos clases una de perro y otra de gato, cuyos objetos instanciados, puedan ladrar y maullar. Los datos de los animales deben ser ingresados por consola

print("Hola! vamos a crear a sus mascotas")

class perro:
    def __init__(self,razaP,colorP,nombreP):
        self.razaP = razaP
        self.colorP = colorP
        self.nombreP = nombreP

    def ladrar(self):
        print(f"Su perro {self.colorP} de raza {self.razaP} esta ladrando! ")
    
    def feliz(self):
        print(f"{self.nombreP} esta siendo acariciado y le gusta")
        print("El perro se siente muy agradecido por su comida :) ")
        print(f"A {self.nombreP} le gusta mucho que lo saque y juegue con el ")
        print(f"{self.nombreP} es feliz! :D ")


class gato:
    def __init__(self,razaG,colorG,nombreG):
        self.razaG = razaG
        self.colorG = colorG
        self.nombreG = nombreG

    def maullar(self):
        print(f"Su gato {self.nombreG} de color {self.colorG} de raza {self.razaG} esta maullando! ")


nombreP = input("Ingrese el nombre de su perro: ")
razaP = input("Ingrese la raza de su perro: ")
colorP = input("Ingrese el color de su perro: ")

miPerro = perro(razaP,colorP,nombreP)
miPerro.ladrar()
miPerro.feliz()

nombreG = input("Ingrese el nombre de su gato: ")
razaG = input("Ingrese la raza de su gato: ")
colorG = input("Ingrese el color de su gato: ")

miGato = gato(razaG,colorG,nombreG)
miGato.maullar()





