"""
AQUI PROPONEMOS LO QUE SON LAS VESTIMENTAS

"""
###################################################

class VestimentaEmpresa:
    def __init__(self, TCalzado, TPeinado, Formal = True ):
        self.TCalzado = TCalzado
        self.TPeinado =TPeinado
        self.Formal = Formal

    def Descrip(self):
        print(" ")
        print("El calzado debe ser: ", self.TCalzado)
        print("El tipo de peinado debe ser: ", self.TPeinado)
        if self.Formal:
            print("--Usted se vestira formal--")

    def Descrip2(self):
        print(" ")
        if self.Formal == False:
            print("El calzado debe ser: ", self.TCalzado)
            print("El tipo de peinado debe ser: ", self.TPeinado)
            print("--Usted no vestira formal--")


###################################################

class CEO(VestimentaEmpresa):
    def __init__(self,Saco, PantalonDVestir,Camisa,Corbata, Calcetas,TCalzado, TPeinado, Formal = True):
        super().__init__(TCalzado, TPeinado, Formal)
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

###################################################

class SUBCEO(CEO):
    def __init__(self, Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Chaleco, PantalonB, Formal=True):
        super().__init__(Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Formal)
        self.Chaleco = Chaleco
        self.PantalonB = PantalonB

    def Descrip(self):
        super().Descrip()

    def Descrip2(self):
        super().Descrip2()
        print("Usted esta usara chaleco: ", self.Chaleco)
        print("Usted usara camisa color: ", self.Camisa)
        print("Usted usara corbata color: ", self.Corbata)
        print("Usted debera usar un pantalon de: ", self.PantalonB)

###################################################

class GERENTE(SUBCEO):
    def __init__(self, Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Chaleco, PantalonB,Formal=True):
        super().__init__(Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Chaleco, PantalonB, Formal)

    def Descrip(self):
        super().Descrip()

    def Descrip2(self):
        super().Descrip2()

###################################################

class JEFEDEAREA(SUBCEO):
    def __init__(self, Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Chaleco, PantalonB,Formal=True):
        super().__init__(Saco, PantalonDVestir, Camisa, Corbata, Calcetas, TCalzado, TPeinado, Chaleco, PantalonB, Formal)

    def Descrip2(self):
        super().Descrip2()

###################################################

class EMPLEADO(VestimentaEmpresa):
    def __init__(self, TCalzado, TPeinado,Guantes, Formal=True):
        super().__init__(TCalzado, TPeinado, Formal)
        self.Guantes = Guantes
        self.Playera = "Algodon"
        self.Pantalon = "Algodon"
        self.Calcetin = "Textil"
        self.Casco = "Plastico Resistente"

    def Descrip2(self):
        super().Descrip2()
        print("Usted usara una playera de : ", self.Playera)
        print("Usted usara un pantalon de: ", self.Pantalon)
        print("Usted usara calcetines de tela: ", self.Calcetin)
        print("Usara un casco de: ", self.Casco)



