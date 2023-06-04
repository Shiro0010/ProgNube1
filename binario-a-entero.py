try:
    numbin = input("Ingrese un número binario: ")
    numint = int(numbin, 2)
    print("la equivalencia del numero binario:",numbin ,"en numero entero, es igual a:", numint)
except ValueError:
    print("solo se admiten numeros binarios")