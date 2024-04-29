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

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self,valor):
        self.__peso=valor

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,valor):
        self.__edad=valor

    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self,valor):
        self.__sexo=valor

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,valor):
        self.__color=valor
    