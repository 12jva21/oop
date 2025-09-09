'''
Abstraer elementos
Esquema modular y diagrama de clases
Los requerimientos son el contexto. El levantamiento de requerimientos es identificar el tipo de variables que necesitan los atributos.
Los atributos son las figuras a las que aplican las acciones
Los metodos son las acciones
Los objetos son el producto de uno o varios atributos, metodos y clases
Una instancia es darle los valores a las variables de los objetos
Hay tipo de valor objeto
El constructor es el metodo que crea los atributos de los objetos de la clase( __init__- self)
getters setters para obtener y cambiar los atributos
'''

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
        print(f"El perro")


class gato:
    def __init__(self,razaG,colorG,nombreG):
        self.razaG = razaG
        self.colorG = colorG
        self.nombreG = nombreG

    def maullar(self):
        print(f"Su gato {self.colorG} de raza {self.razaG} esta maullando! ")


nombreP = input("Ingrese el nombre de su perro: ")
razaP = input("Ingrese la raza de su perro: ")
colorP = input("Ingrese el color de su perro: ")

miPerro = perro()
miPerro.ladrar()

nombreG = input("Ingrese el nombre de su gato: ")
razaG = input("Ingrese la raza de su gato: ")
colorG = input("Ingrese el color de su gato: ")

miGato = gato ()
miGato.maullar 

