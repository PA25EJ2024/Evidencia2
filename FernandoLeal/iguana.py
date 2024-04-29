class iguana:
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
    
    def tipo(self):
        print("{self.__nombre}, puede llegar a ser iguana terrestre o marina.")

    def habitat(self):
        print("Esta criatura diminuta {self.__nombre} puede estar tanto en areas tropicales como en ambientes costeros y marinos")

    def alimentacion(self):
        print("La comida favorita de {self.__nombre} pueden ser hojas, frutas y flores, hasta tambien comen insectos u otros animales mas chicos que ellos.")

    def caracteristicas(self):
        print("Lo fascinante de {self.__nombre} es que pueden regular su temperatura corporal atraves de la expocision del sol.")

    def inteligencia(self):
        print("{self.__nombre}, es especial en la busqueda de alimentos y en la interaccion en su entorno.")

    def __str__(self):
        return (f"Iguana: \n Nombre: {self.__nombre}\n Peso: {self.__peso}\n Edad: {self.__edad}\n Sexo: {self.__sexo}\n Color: {self.__color}")