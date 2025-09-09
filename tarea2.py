#Autor: Jairo vega Anacona
#Motivo: Tarea 2


#implementar dos clases una de perro y otra de gato, cuyos objetos instanciados, puedan ladrar y maullar. Los datos de los animales deben ser ingresados por consola

print("Hola! vamos a crear a sus mascotas")

class perro:
    def __init__(self,razaP,colorP):
        self.razaP = input("Ingrese la raza de su perro: ")
        self.colorP = input("Ingrese el color de su perro: ")

    def ladrar(self):
        print(f"Su perro {self.colorP} de raza {self.razaP} esta ladrando! ")


class gato:
    def __init__(self,razaG,colorG):
        self.razaG = input("Ingrese la raza de su gato: ")
        self.colorG = input("Ingrese el color de su gato: ")

    def maullar(self):
        print(f"Su gato {self.colorG} de raza {self.razaG} esta maullando! ")

miPerro = perro()
miPerro.ladrar()

miGato = gato ()
miGato.maullar
