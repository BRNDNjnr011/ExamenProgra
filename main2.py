#Superclase Persona
class Persona:
    def __init__(self, nombre, edad, estatura, genero = "x"):
        self.__nombre = nombre
        self.genero = genero
        self.__edad = edad
        self.__estatura = estatura


    def describir(self):
        print(" ")
        print("Nombre:", self.__nombre)
        print("Género:", self.genero)
        print("Edad:", self.__edad, "Años")
        print("Estatura:", self.__estatura, "mt")


    def setNombre(self, value):
        self.__nombre = value

#Declaración de subclase
class Empleado(Persona):
    def __init__(self, nombre, edad, estatura, sueldo, antiguedad, genero = "x"):
        super().__init__(nombre, edad, estatura, genero)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad

    def describir(self):
        super().describir()
        print("Sueldo:", self.__sueldo, "$")
        print("Antigûedad:", self.__antiguedad, "Años")