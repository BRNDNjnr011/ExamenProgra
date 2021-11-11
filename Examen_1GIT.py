"""
A continuacion presentamos el panel de neustra empresa
"""
import main as Examen
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

if Opcion == 1:
    print("Bienvenido CEO")

if Opcion == 2:
    print("Bienvenido SUB_CEO")

if Opcion == 3:
    print("Bienvenido GERENTE")

if Opcion == 4:
    print("Bienvenido JEFE DE AREA")

if Opcion == 5:
    print("Bienvenido EMPLEADO")