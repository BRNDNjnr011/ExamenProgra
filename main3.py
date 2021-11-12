class VestimentaEmpresa:
    def __init__(self, TCalzado, TPeinado, Formal = True ):
        self.TCalzado = TCalzado
        self.TPeinado =TPeinado
        self.Formal = Formal

    def Descrip(self):
        print("El calzado debe ser: ", self.TCalzado)
        print("El tipo de peinado debe ser: ", self.TPeinado)
        if self.Formal:
            print("Usted se vestira formal")
        else:
            print("Usted no vestira formal")

#Declaración de subclase
class CEO(VestimentaEmpresa):
    def __init__(self,Saco, PantalonDVestir,Camisa,Corbata, Calcetas,TCalzado, TPeinado, Formal = True):
        super().__init__(TCalzado, TPeinado, Formal = True)
        self.Saco = Saco
        self.Pantalon = PantalonDVestir
        self.Camisa = Camisa
        self.Corbata = Corbata
        self.Calcetas = Calcetas

    def Descrip(self):
        super().Descrip()
        print("Usted usara un saco color: ", self.Saco)
        print("Usted usara pantalon color: ", self.Pantalon)
        print("Usted usara camisa color: ", self.Camisa)
        print("Usted usara corbata color: ", self.Corbata)
        print("Usted usara calcetas color: ", self.Calcetas)

class SUBCEO(VestimentaEmpresa):
    pass

class GERENTE(VestimentaEmpresa):
    pass

class JEFEDEAREA(VestimentaEmpresa):
    pass

class EMPLEADO(VestimentaEmpresa):
    pass
