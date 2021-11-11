class Empresa:
    def __init__(self, Nombre, Ubicacion):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion

    def Descripcion(self):
        print("Nombre: ", self.Nombre)
        print("Ubicacion: ", self.Ubicacion)

class CEO(Empresa):
    pass

class SUBCEO(Empresa):
    pass

class GERENTE(Empresa):
    pass

class JEFEDEAREA(Empresa):
    pass

class EMPLEADO(Empresa)