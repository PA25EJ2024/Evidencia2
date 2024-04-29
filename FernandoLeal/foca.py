class foca:
    def __init__(self, nombre, peso, edad, sexo, color):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.sexo = sexo
        self.color = color

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor