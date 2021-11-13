"""
A continuacion presentamos el panel de neustra empresa
"""
import main as Examen1
import main2 as Examen2
import main3 as Examen3

###################################################

Empresa1 = Examen1.Empresa("BJ-CORP_UNITE","UNITE STATE")
Empresa1.Descripcion()
#print("------------------EMPRESA-----------------------")
#print("_______________BJ-CORP_UNITE___________________")
print("SELECCIONE EL RANGO AL QUE PERTENECE")
print("CEO-(1)\nSUB_CEO-(2)\nGERENTE-(3)\nJEFE DE AREA-(4)\nEMPLEADO-(5)")

while True:
    Opcion = input("Opcion: ")
    try:
        Opcion = int(Opcion)
        break
    except ValueError:
        print("Por favor ingrese el numero de su rango correctamente")

if Opcion > 5:
    print("****Error digite su numero correctamente****")
if Opcion <= 0:
    print("***Error digite su numero correctamente***")

###################################################

if Opcion == 1:
    print("  ")
    print("Bienvenido CEO")
    Persona1 = Examen2.Empleado("Brandon J. Juarez Gervacio", 45, 1.60, 100000,27,"Masculino")
    Persona1.describir()

    print(" ")
    print("La vestimenta propuesta por la empresa para usted es : ")
    Vestimenta1 = Examen3.CEO("Negro","Negro","Blanco","Roja","Negro","Zapato","Casual pelo corto")
    Vestimenta1.Descrip()

    print(" ")
    print("Las tareas para el dia de hoy son las siguientes")
    CEO1 = Examen1.CEO("CEO de la empresa","001" ,"Indefinidas","Si","No","Si",0,2)
    CEO1.Descripcion()

###################################################

if Opcion == 2:
    print("  ")
    print("Bienvenido SUB_CEO")
    Persona2 = Examen2.Empleado("Ramiro Lopez Urtado", 36,1.70,75000,25, "Masculino")
    Persona2.describir()

    print(" ")
    print("Usted estara en la oficina o visitara la planta")
    print("Oficina-(1)\nPlanta-(2)\n")
    while True:
        Opcion2 = input("Opcion: ")
        try:

            Opcion2 = int(Opcion2)
            break
        except ValueError:
            print("Escoja la opcion de manera correcta")

    if Opcion2 > 2:
        print("****Error digite su numero correctamente****")
    if Opcion2 <= 0:
        print("***Error digite su numero correctamente***")

    if Opcion2 == 1:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la oficina es la siguiente : ")
        Vestimenta2 = Examen3.SUBCEO("Negro","Negro","Blanca","Azul","Negro","Zapato Casual", "Pelo corto casual","no","no")
        Vestimenta2.Descrip()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        SUBCEO = Examen1.SUBCEO("SUB_CEO","002","Indefinidas","Si","Si","No","No","No",2)
        SUBCEO.Descripcion()

    if Opcion2 == 2:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la planta es la siguiente : ")
        Vestimenta3 = Examen3.SUBCEO("no","no","Blanco","Azul","Negro","Bota industrial","Pelo corto casual","Negro de algodon","Algodon",False)
        Vestimenta3.Descrip2()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        SUBCEO2 = Examen1.SUBCEO("SUB_CEO","002","Indefinidas","No","No","Si","Ver el trabajo final","Platica seria",0,)
        SUBCEO2.Descripcion2()

###################################################

if Opcion == 3:
    print("  ")
    print("Bienvenido GERENTE")
    Persona3 = Examen2.Empleado("Alberto Santos Hernandez",35,1.7,50000,20, "Masculino")
    Persona3.describir()
    print(" ")
    print("Usted estara en la oficina o visitara la planta")
    print("Oficina-(1)\nPlanta-(2)\n")
    while True:
        Opcion3 = input("Opcion: ")
        try:

            Opcion3 = int(Opcion3)
            break
        except ValueError:
            print("Escoja la opcion de manera correcta")

    if Opcion3 == 1:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la oficina es la siguiente : ")
        Vestimenta4 = Examen3.GERENTE("Negro de tres botones","Negro de mesclilla","blanca","Vino","Negras","Zapato casual","Corte militar","no","no")
        Vestimenta4.Descrip()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        GERENTE1 = Examen1.GERENTE("Gerente","003",10,"Si una pendiente","4 solicitudes","No","Si","No")
        GERENTE1.Descripcion()
        print(" ")
        print("Pimera tarea del dia entrevistar al solicitante")
        print("Entrevistar-(1)\nNo entrevistar-(2)\n")
        while True:
            OpcionE = input("Opcion: ")
            try:

                OpcionE = int(OpcionE)
                break
            except ValueError:
                print("Escoja la opcion de manera correcta")

        if OpcionE == 1:
            print("Entrando a  oficina.......")
            print("Empieza la conversacion")
            print("  ")
            print("----------------------------------------------------------------------")
            print(" Hola! un gusto yo soy: ")
            ENTREVISTADOR1 = Examen2.Empleado("Alberto Santos Hernandez",35,1.7,50000,20, "Masculino")
            ENTREVISTADOR1.desribir2()
            ENTREVISTADOR_1 = Examen1.Puesto("Gerente","003",10)
            ENTREVISTADOR_1.DescripcionE()
            print(" ")
            myList = []
            print("Bueno ya hable de mi, ahora es tu turno")
            a = str(input("¿Cuál es tu nombre?:\n"))
            b = str(input("¿Qué edad tienes?:\n"))
            c = str(input("¿Tienes antecedentes en otra empresa?:\n"))
            d = str(input("¿Te desempeñas bien realizado mantenimiento correctivo?:\n"))
            e = str(input("¿Te desempeñas bien realizado mantenimiento preventivo?:\n"))
            f = str(input("¿Tienes las habilidades necesarias?:\n"))
            g = str(input("¿Tienes problema con portar uniforme?:\n"))
            h = str(input("¿Trabajas bien en equipo?:\n"))
            i = str(input("¿Consideras que tu desempeño  individual es bueno?:\n"))
            j = str(input("¿Sabes liderar?:\n"))
            k = str(input("¿Porque quieres trabajar aqui?:\n"))
            myList = [a,b,c,d,e,f,g,h,i,j,k]

            print(" ")
            print(" OK muy bien te tendremos en cosideracion revisare con mas detenimiento tu curriculum\ny si todo sale bien nosotros te llamamos")
            print("Un gusto asta luego ", a)
            print("----------------------------------------------------------------------")
            print("Ingresando al sistema...")
            print("Revisar el Curriculum")
            print("Si-(1)\nNo-(2)\n")
            while True:
                OpcionCu = input("Opcion: ")
                try:

                    OpcionCu = int(OpcionCu)
                    break
                except ValueError:
                    print("Escoja la opcion de manera correcta")


            if OpcionCu == 1:

                print("Curriculum revisado...")
                print("¿Usted desea contrartarlo?")
                print("Si-(1)\nNo-(2)\n")
                while True:
                    OpcionC = input("Opcion: ")
                    try:

                        OpcionC = int(OpcionC)
                        break
                    except ValueError:
                        print("Escoja la opcion de manera correcta")

                if OpcionC == 1:
                    print(" ")
                    print("-Se le enviara un correo notificando que fue aceptado-")
                    print(" ")
                    print("Datos recopilados")
                    print(myList)
                    print("Los datos se pasaran al sistema principal para añadirlo luego de que el reconfirme que acepta estar con nostros")
                    print("El dia de mañana si todo sale bien podra ver al nuevo empleado en el sistema")
                    print("Le mostraremos su tarea siguiente....")

                if OpcionC == 2:
                    print(" ")
                    print("Le mostraremos su tarea siguiente....")

            if OpcionCu == 2:
                print(" ")
                print("Le mostraremos su tarea siguiente....")

        if OpcionE == 2:
            print(" ")
            print("Le mostraremos su tarea siguiente....")

    if Opcion3 == 2:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la planta es la siguiente : ")
        Vestimenta5 = Examen3.GERENTE("No","No","Blanca no inflamable","Vino","Negras","Botas industriales","Corte militar","Negro de algodon","Negro textil",False)
        Vestimenta5.Descrip2()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        GERENTE2 = Examen1.GERENTE("Gerente","003",10,"No","No","Modificar el plan de trabajo","No","Llevar el pago hoy")
        GERENTE2.Descripcion2()


###################################################

if Opcion == 4:
    print("  ")
    print("Bienvenido JEFE DE AREA")
    Persona4 = Examen2.Empleado("Mariana Herrera Torres",28,1.58,25000,10,"Mujer")
    Persona4.describir()
    print(" ")
    print("Usted estara en la oficina o visitara la planta")
    print("Oficina-(1)\nPlanta-(2)\n")
    while True:
        Opcion4 = input("Opcion: ")
        try:

            Opcion4 = int(Opcion4)
            break
        except ValueError:
            print("Escoja la opcion de manera correcta")

    if Opcion4 == 1:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la oficina es la siguiente : ")
        Vestimenta6 = Examen3.JEFEDEAREA("No","No","Blanca manga corta","Cafe","Negras","Zapato casual","Militar","Negro"," Algodon Negro mesclilla",)
        Vestimenta6.Descrip2()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        JEFE1 = Examen1.JEFEDEAREA("Jefe de area","004",12,"No"," 2 Recibos de compra de material","No","7:30")
        JEFE1.Descripcion()


    if Opcion4 == 2:
        print(" ")
        print("La vestimenta propuesta por la empresa para que usted\neste trabajando en la planta es la siguiente : ")
        Vestimenta7 = Examen3.JEFEDEAREA("No","No","Blanca manga corta","Cafe","Negras","Bota industrial","Militar","Negro de algodon","Algodon Negro mesclilla ",False)
        Vestimenta7.Descrip2()
        print(" ")
        print("Las tareas para el dia de hoy son las siguientes")
        JEFE2 = Examen1.JEFEDEAREA("Jefe de area","004",12,"Ir a area de termiando","No","Mostrar el acabado en productos","No")
        JEFE2.Descripcion2()

###################################################

if Opcion == 5:
    print("  ")
    print("Bienvenido EMPLEADO")
    Persona5 = Examen2.Empleado("Juan Estrada Romero",22,1.70,10000,3)
    Persona5.describir()
    print(" ")
    print("La vestimenta propuesta por la empresa para usted es : ")
    Vestimenta8 = Examen3.EMPLEADO("Bota de seguridad industruial", " Corte militar","Si",False)
    Vestimenta8.Descrip2()
    print(" ")
    print("Las tareas para el dia de hoy son las siguientes")
    EMPLEADO1 = Examen1.EMPLEADO("Empleado", "005", 10)
    EMPLEADO1.Descripcion2()