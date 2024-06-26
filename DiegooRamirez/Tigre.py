class Tigre:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Sexo):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Sexo=Sexo
    
    def __str__(self):
        return f"Tigre: {self.__Nombre}, Edad: {self.__Edad}, Peso: {self.__Peso} kg, Tamaño: {self.__Tamaño} cm, Sexo: {self.__Sexo}\n"

    def correr(self):
        print("Los tigres pueden alcanzar velocidades de hasta 90km/h, superando a los leopardos")

    def saltar(sefl):
        print("El tigre es uno de los felinos que mas alto salta pues pueden alcanzar hasta los 5 metros de altura")

    def bañarse(self):
        print("A los tigres les encanta el contacto con el agua y son excelentes nadadores")

    def peso(self):
        print(f"Es el felino mas grande del mundo y puede alcanzar un peso de 306 Kg, nuestro tigre pesa: {self.__Peso} kg")
    
    def rugir(self):
        print("El tigre ruge: !!!!GR-GR-GR-GR¡¡¡¡")

    @property
    def nombre(self):
        return self.__Nombre
    @nombre.setter
    def nombre(self,valor):
        self.__Nombre=valor
    
    @property
    def edad(self):
        return self.__Edad
    @edad.setter
    def edad(self, valor):
        self.__Edad=valor

    @property
    def peso(self):
        return self.__Peso
    @peso.setter
    def peso(self,valor):
        self.__Peso=valor

    @property
    def tamaño(self):
        return self.__Tamaño
    @tamaño.setter
    def tamaño(self,valor):
        self.__Tamaño=valor

    @property
    def sexo(self):
        return self._Sexo
    @sexo.setter
    def sonido(self,valor):
        self._Sexo=valor
