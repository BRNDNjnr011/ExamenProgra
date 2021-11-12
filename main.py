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
        print("Trabajando en oficina...")
        print("Cargo que desempeña: ", self.Cargo)
        print("Numero de identificacion: ", self.Nplaca)
        print("Horas destinadas al trabajo: ", self.HrTrabajo)

    def Descripcion2(self):
        print("Trabajando en Planta...")
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

class SUBCEO(Puesto):
    def __init__(self,Cargo, Nplaca, Hrtrabajo, ConfirmarCompras, AsistenciaAuditoria, AutorizarContrataciones,RevisarPlanta, AsistirGerente, HrAuditoria = None):
        super().__init__(Cargo, Nplaca, Hrtrabajo)
        self.Compras = ConfirmarCompras
        self.AsisAuditoria = AsistenciaAuditoria
        self.HrAuditoria = HrAuditoria
        self.RevisionDContra = AutorizarContrataciones
        self.RevPlanta = RevisarPlanta
        self.AsisGerente = AsistirGerente

    def Descripcion(self):
        super().Descripcion()
        print("Revisar las compras realizadas: ", self.Compras)
        print("Asisitir a la auditoria: ",self.AsisAuditoria)
        print("Hora de la auditoria: ", self.HrAuditoria,"pm")

    def Descripcion2(self):
        super().Descripcion2()
        print("Autorizar Contrataciones: ", self.RevisionDContra)
        print("Revisar el trabajo en planta: ", self.RevPlanta)
        print("Dar instrucciones avanzadas al gerente: ", self.AsisGerente)


class GERENTE(Empresa):
    pass

class JEFEDEAREA(Empresa):
    pass

class EMPLEADO(Empresa):
    pass