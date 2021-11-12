class Empresa:
    def __init__(self, Nombre, Ubicacion):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion

    def Descripcion(self):
        print("  ")
        print("Nombre: ", self.Nombre)
        print("Ubicacion: ", self.Ubicacion)

class Puesto:
    def __init__(self,Cargo, Nplaca, Hrtrabajo):
        self.Cargo = Cargo
        self.Nplaca = Nplaca
        self.HrTrabajo = Hrtrabajo

    def Descripcion(self):
        print("Cargo que desempeña: ", self.Cargo)
        print("Numero de identificacion: ", self.Nplaca)
        print("Horas destinadas al trabajo: ", self.HrTrabajo)

#Declaración de subclase
class CEO(Puesto):
    def __init__(self,Cargo, Nplaca, Hrtrabajo, CerrarTrato, Auditoria, Junta, HrAuditoria = None,  HoraDeJunta = None):
        super().__init__(Cargo, Nplaca, Hrtrabajo)
        self.CerrarTrato = CerrarTrato
        self.Junta = Junta
        self.Hora = HoraDeJunta
        self.Auditoria = Auditoria
        self.HrAuditoria = HrAuditoria

    def Descripcion(self):
        print("  ")
        super().Descripcion()
        print("Cerrar algun trato: ", self.CerrarTrato)
        print("Alguna auditoria: ", self.Auditoria)
        print("Hora de la auditoria: ", self.HrAuditoria, "pm")
        print("Alguna junta: ", self.Junta)
        print("Hora de la junta: ", self.Hora , "pm")

class SUBCEO(Empresa):
    pass

class GERENTE(Empresa):
    pass

class JEFEDEAREA(Empresa):
    pass

class EMPLEADO(Empresa):
    pass