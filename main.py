"""
AQUI TENEMOS LO QUE ES LA ESTRUCTURA DE LA EMPRESA Y SUS ACCIONES POR PUESTO

"""
###################################################

class Empresa:
    def __init__(self, Nombre, Ubicacion):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion

    def Descripcion(self):
        print("  ")
        print("Nombre: ", self.Nombre)
        print("Ubicacion: ", self.Ubicacion)

###################################################

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

    def DescripcionE(self):
        print("Cargo que desempeño es : ", self.Cargo)
        print("Mi numero de identificacion: ", self.Nplaca)
        print("Las horas que destino al trabajo son : ", self.HrTrabajo)
        print("Puedes encontrarme en la oficina o en la planta")

###################################################

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

###################################################

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

###################################################

class GERENTE(Puesto):
    def __init__(self, Cargo, Nplaca, Hrtrabajo, Entrevista, SoliEmpleo, InstruJArea, PagosMaterial, SueldoEmpleados):
        super().__init__(Cargo, Nplaca, Hrtrabajo)
        self.Entrevista = Entrevista
        self.SoliEmpleo = SoliEmpleo
        self.Instru  = InstruJArea
        self.PagosM = PagosMaterial
        self.Sueldos = SueldoEmpleados

    def Descripcion(self):
        super().Descripcion()
        print("Realizar una entrevista: ", self.Entrevista)
        print("Revicion de solicitudes de empleo: ", self.SoliEmpleo)
        print("Realizar algun pago de material: ", self.PagosM)

    def Descripcion2(self):
        super().Descripcion2()
        print("Dar instrucciones a Jefe de area: ", self.Instru)
        print("LLevar el sueldo de los empleados a el Jefe de area: ", self.Sueldos)

###################################################

class JEFEDEAREA(Puesto):
    def __init__(self, Cargo, Nplaca, Hrtrabajo, Supervisar, Facturar, IntruirEmpleados, PagarEmpleados):
        super().__init__(Cargo, Nplaca, Hrtrabajo)
        self.Supervisar = Supervisar
        self.Facturar = Facturar
        self.Instruir = IntruirEmpleados
        self.Pagar = PagarEmpleados

    def Descripcion(self):
        super().Descripcion()
        print("Existen recibos por faturar: ", self.Facturar)
        print("Dar el pago a los empleados: ", self.Pagar, "pm")

    def Descripcion2(self):
        super().Descripcion2()
        print("Ver como trabajan los empleados: ", self.Supervisar)
        print("Mostrarles el metodo para realizar las cosas: ", self.Instruir)

###################################################

class EMPLEADO(Puesto):
    def __init__(self, Cargo, Nplaca, Hrtrabajo ,MantenimientoPreventivo = True):
        super().__init__(Cargo, Nplaca, Hrtrabajo)
        self.Mpreventivo = MantenimientoPreventivo

    def Descripcion2(self):
        super().Descripcion2()
        if self.Mpreventivo:
            print("Realizar Mantenimiento Preventivo....")
        else:
            print("Realizar Manteniemiento Correctivo...")






