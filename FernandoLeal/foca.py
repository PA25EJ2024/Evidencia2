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
    
    def alimentacion(self):
        print("{self.__nombre},generalmente su dieta se basa en peces, calamares y crustáceos.")

    def habitat(self):
        print("Este pequeño {self.__nombre}, le encanta las aguas frias del oceano, de preferencia cerca de las costas.")

    def categoria(self):
        print("Aun asi sabias que {self.__nombre}, pertenece a los grandes mamiferos marinos")

    def nombreCientifico(self):
        print("Talvez tu lo conoces como {self.__nombre} o foca, pero en su origen se le conoce como  Phoca vitulina")

    def aspecto(self):
        print("{self.__nombre}, hay como muchos y pueden llegar a tener cuerpos alargados y adaptados para nadar en el agua, ademas su color puede llegar a ser gris oscuro hasta marron claro")
    pass