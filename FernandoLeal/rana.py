class rana:
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
    

    def caracteristica(self):
        print("Asi como {self.__nombre}, hay muchas de ellas que tienen diferencias como lo son su piel húmeda y resbaladiza, ojos saltones y largas patas traseras adaptadas para el salto.")

    def habitat(self):
        print("{self.__nombre}, suele encontrarse en entornos acuáticos como lagos, estanques, ríos y humedales, así como en áreas terrestres cercanas a fuentes de agua.")

    def alimentacion(self):
        print("A {self.__nombre} le encanta comer una gran variedad de insectos, arañas, gusanos y otros pequeños invertebrados que capturan con su lengua pegajosa y retráctil.")

    def vida(self):
        print("Amiguitos como {self.__nombre} pueden llegar a vivir alrededor de 4 a 6 años en la naturaleza, mientras que las especies más grandes, pueden alcanzar hasta 10 años en estado salvaje y más de 20 años en cautiverio con los cuidados adecuados.")

    def curiosidad(self):
        print("Una curiosidad fascinante de {self.__nombre} es su capacidad para absorber agua a través de su piel, lo que les permite mantenerse hidratada en entornos secos.")

    def __str__(self):
        return (f"Rana: \n Nombre: {self.__nombre}\n Peso: {self.__peso}\n Edad: {self.__edad}\n Sexo: {self.__sexo}\n Color: {self.__color}")