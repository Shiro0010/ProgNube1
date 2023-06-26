#determinar un año bisiesto por teclado?
try:
    anio_xd = int(input("Ingrese un año para deducir: "))
    if anio_xd < 0:
        print("hablemos de años D.C por ahora :v")
    else:
        if anio_xd % 400 == 0:
            print("El año ingresado es bisiesto claroquesi.")
        elif anio_xd % 100 == 0:
            print("El año ingresado no es bisiesto.")
        elif anio_xd % 4 == 0:
            print("El año ingresado es bisiesto.")
        else:
            print("El año ingresado no es bisiesto.")
except ValueError:
    print("Error: El valor ingresado no es un año válido.")
