try:
    print("a")
    def calcular_mcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def calcular_mcm(a, b):
        producto = a * b
        mcd = calcular_mcd(a, b)
        mcm = producto // mcd
        print("El MCD de", a, "y", b, "es:", mcd)
        print("El MCM de", a, "y", b, "es:", mcm)
        return mcm

    def simplificar_fraccion(numerador, denominador):
        mcd = calcular_mcd(numerador, denominador)
        numerador_simplificado = numerador // mcd
        denominador_simplificado = denominador // mcd
        print("La fracción", numerador, "/", denominador, "se simplifica a:", numerador_simplificado, "/", denominador_simplificado)
        return numerador_simplificado, denominador_simplificado

    def sumar_fracciones(fraccion1, fraccion2, fraccion3):
        denominador_comun = calcular_mcm(fraccion1[1], calcular_mcm(fraccion2[1], fraccion3[1]))
        numerador_suma = fraccion1[0] * (denominador_comun // fraccion1[1]) + fraccion2[0] * (denominador_comun // fraccion2[1]) + fraccion3[0] * (denominador_comun // fraccion3[1])
        
        return simplificar_fraccion(numerador_suma, denominador_comun)

    numerador1 = int(input("Ingrese el numerador de la primera fraccion: "))
    denominador1 = int(input("Ingrese el denominador de la primera fraccion: "))
    numerador2 = int(input("Ingrese el numerador de la segunda fraccion: "))
    denominador2 = int(input("Ingrese el denominador de la segunda fraccion: "))
    numerador3 = int(input("Ingrese el numerador de la tercera fraccion: "))
    denominador3 = int(input("Ingrese el denominador de la tercera fraccion: "))
    print( )
    print("Las fracciones ingresadas son:" )
    print(" ", numerador1," ", numerador2, " ", numerador3 )
    print(" --- --- ---")
    print(" ", denominador1, " ", denominador2, " ", denominador3 )

    print()  
    
    fraccion1 = simplificar_fraccion(numerador1, denominador1)
    fraccion2 = simplificar_fraccion(numerador2, denominador2)
    fraccion3 = simplificar_fraccion(numerador3, denominador3)

    resultado = sumar_fracciones(fraccion1, fraccion2, fraccion3)

    print("El resultado es igual a:")
    print(" ", resultado[0])
    print("-----") 
    print(" ", resultado[1])
except ValueError:
    print("Solo se admiten caracteres numéricos.")