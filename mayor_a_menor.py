try:
    numero1 = float(input("ingrese el primer numero: "));
    numero2 = float(input("ingrese el segundo numero: "));

    if numero1 < numero2:
        print("el numero mayor es", numero2);
    elif numero1 > numero2:
        print("el numero mayor es", numero1);
    else:
        print("los numeros son iguales");
except ValueError:
    print("solo se admiten numeros.")
#un programa para deducir cual de los 2 numeros ingresados por teclado es Mayor
