try:
    decs = int(input('''conteo ascendente o descendente?
    1. ascendente
    2. descendente
Digite la opcion a continuacion: '''))

    if decs == 1:
        for i in range ((int(input("ingrese un numero: "))), (int(input("ingresa el segundo numero: " ))) + 1, 1):
            print(i)
    elif decs > 2 or decs < 1:
        print("opción invalida")
    else:
        for i in range ((int(input("ingrese un numero: "))), (int(input("ingresa el segundo numero: " ))) - 1, -1):
            print(i)
except ValueError:
    print("Solo se Admiten números en los campos de digitación.")
'''no sabia que se podia poner input ahi, pero probando si pude jajaj
en fin, este codigo toma los 2 primeros datos (inicio y fin) y le suma 1 numero al fin para
que la cuenta llegue hasta ese numero. y en el otro modo es al revez, y el numero de saltos tambien a eleccion.
lo hice opcionado para que sea mas sutil y amigable con el usuario'''
