"""
A continuacion presentamos el panel de neustra empresa
"""
import main as Examen
import main2 as Examen2
Empresa1 = Examen.Empresa("BJ-CORP_UNITE","UNITE STATE")
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
    print("No es una de la opciones")
if Opcion < 1:
    print("No es una de la opciones")

if Opcion == 1:
    print("  ")
    print("Bienvenido CEO")
    Persona1 = Examen2.Empleado("Brandon J. Juarez Gervacio", 45, 1.60, 60, 100000,20,"Masculino")
    Persona1.describir()
    print("La vestimenta propuesta por la empresa para usted es : ")
    #Se inserta el main y se crea su vestimenta
    print("Las tareas para el dia de hoy son las siguientes: ")
    CEO1 = Examen.CEO("CEO de la empresa",1 ,"indefinidas","SI","NO","SI",0.0,2)
    CEO1.Descripcion()

if Opcion == 2:
    print("Bienvenido SUB_CEO")

if Opcion == 3:
    print("Bienvenido GERENTE")

if Opcion == 4:
    print("Bienvenido JEFE DE AREA")

if Opcion == 5:
    print("Bienvenido EMPLEADO")