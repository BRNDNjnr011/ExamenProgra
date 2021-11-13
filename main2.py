"""
AQUI INTANCIAMOS LO QUE SON LAS PERSONAS Y SUS CARACTERISTICAS

"""
###################################################

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

    def describir2(self):
        print(" ")
        print(self.__nombre)
        print("Tengo: ", self.__edad, "Años")


    def setNombre(self, value):
        self.__nombre = value

###################################################

class Empleado(Persona):
    def __init__(self, nombre, edad, estatura, sueldo, antiguedad, genero = "x"):
        super().__init__(nombre, edad, estatura, genero)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad

    def describir(self):
        super().describir()
        print("Sueldo:", self.__sueldo, "$")
        print("Antigûedad:", self.__antiguedad, "Años")

    def desribir2(self):
        super().describir2()
        print("Mi tiempo en esta empresa es de: ", self.__antiguedad, "Años")

    def describirCu(self):
        pass

class Profesion(Empleado):
    def __init__(self, nombre, edad, estatura, peso, empleo, sueldo, antiguedad, genero = "x"):
        super().__init__(nombre, edad, estatura, peso, sueldo, antiguedad, genero)
        self.__empleo = empleo

    def describirCu(self):
        super().describirCu()
        print("Antigua profecion: ", self.__empleo)
