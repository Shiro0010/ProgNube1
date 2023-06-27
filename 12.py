def es_potencia_de_dos(numero):
    if numero == 0:
        return False
    while numero != 1:
        if numero % 2 != 0:
            return False
        numero = numero // 2
    return True


def suma_potencias_de_dos(a, b):
    suma = 0
    for numero in range(a, b + 1):
        if es_potencia_de_dos(numero):
            suma += numero
    return suma




'''no tenia la menor idea de como construir este codigo, asi que solicite ayuda y una explicacion
sobre este mismo para aclarar dudas.'''