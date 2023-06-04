try:
    num = int(input("Ingrese el numero entero a calcular: "))

    hexa = hex(num)
    octa = oct(num)
    bina = bin(num)

    print("el valor siguiente a *0x* es el valor de", num, "en hexadecimal: ",hexa)
    print("el valor siguiente a *0o* es el valor de", num, "en octal: ",octa )
    print("el valor siguiente a *0b* es el valor de", num, "en binario: ",bina)
except ValueError:
    print("no se permiten numeros de tipo float, ni cadenas de texto. ")
    