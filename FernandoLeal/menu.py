from foca import foca
from iguana import iguana
from rana import rana

class Zoologico:
    def __init__(self):
        self.animales = []

    def añadirA(self, animalNuevo):
        self.animales.append(animalNuevo)

    def mostrarA(self):
        for animales in self.animales:
            print(animales)

adminZoo = Zoologico()
while True:
    opcion = int(input("\n1.Agregar animal. \n2.Ver animales. \n3.Salir \n"))
    if opcion == 1:
        animal = int(input("Que animal se desea agregar:  \n1.Foca \n2.Iguana \n3.Rana  \n"))
        if animal == 1:
            nombre = input("Ingresa el nombre: ")
            peso = input("Ingresa el peso: ")
            edad = input("Ingresa la edad: ")
            sexo = input("Ingresa el sexo: ")
            color = input("Ingresa la color: ")
            focaNueva = foca(nombre, peso, edad, sexo, color)
            adminZoo.añadirA(focaNueva)

        elif animal == 2:
            nombre = input("Ingresa el nombre: ")
            peso = input("Ingresa el peso: ")
            edad = input("Ingresa la edad: ")
            sexo = input("Ingresa el sexo: ")
            color = input("Ingresa la color: ")
            iguanaNueva = iguana(nombre, peso, edad, sexo, color)
            adminZoo.añadirA(iguanaNueva)
            
        elif animal == 3:
            nombre = input("Ingresa el nombre: ")
            peso = input("Ingresa el peso: ")
            edad = input("Ingresa la edad: ")
            sexo = input("Ingresa el sexo: ")
            color = input("Ingresa la color: ")
            ranaNueva = rana(nombre, peso, edad, sexo, color)
            adminZoo.añadirA(ranaNueva)

        elif opcion == 2:
            adminZoo.mostrarA()

        elif opcion == 3:
            break