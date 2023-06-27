try:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero <= 0:
        print("El número debe ser positivo y mayor de 0. :v")
    else:
        factores_primos = []
        divisor = 2

        while numero > 1:
            if numero % divisor == 0:
                factores_primos.append(divisor)
                numero = numero / divisor
            else:
                divisor += 1

        print("La descomposición en factores primos es:", factores_primos)

except ValueError:
    print("Cual es la necesidad de poner letras manito ._.")

'''tuve que buscar un tutorial para aprender a hacer esa operacion jajajkskjdajs
pero ahi esta el codigo, use una lista para hacer mas sencillo el codigo y no extenderlo mas de lo necesario
a mi parecer.'''