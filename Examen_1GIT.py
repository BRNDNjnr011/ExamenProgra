"""
A continuacion presentamos el panel de neustra empresa

"""
print("------------------EMPRESA-----------------------")
print("_______________BJ-CORP_UNITE___________________")
print("Seleccione el rango al que pertenece")
print("CEO-(1)\nSU_CEO-(2)\nGERENTE-(3)\nJEFE DE AREA-(4)\nEMPLEADO-(5)")

while True:
    Opcion = input("Opcion: ")

    try:
        Opcion = int(Opcion)
        break
    except ValueError:
        print("Por favor ingrese el numero de su rango correctamente")

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

