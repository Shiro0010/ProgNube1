try:
    numero = float(input("ingrese un numero: "))
    int(numero)
    if numero == int(numero):
        print("el numero es entero")
    else:
        print("el numero es Real")
except ValueError:
    print("el numero no es un numero :v")