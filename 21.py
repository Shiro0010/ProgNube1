def contar_vocales(oracion):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for letra in oracion:
        letra = letra.lower()         
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1

    # Mostrar los resultados
    print("Cantidad de 'a':", contador_a)
    print("Cantidad de 'e':", contador_e)
    print("Cantidad de 'i':", contador_i)
    print("Cantidad de 'o':", contador_o)
    print("Cantidad de 'u':", contador_u)

oracion = input("Ingrese una oración: ")
contar_vocales(oracion)
'''este tipo de ejercicios son un poquito menos complejos que los de matematicas, me gustan.'''