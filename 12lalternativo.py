def es_potencia_de_dos(numero):
    if numero == 0:
        return False
    while numero != 1:
        if numero % 2 != 0:
            return False
        numero = numero // 2
    return True


def suma_potencias_de_dos():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    suma = 0
    for numero in range(a, b + 1):
        if es_potencia_de_dos(numero):
            suma += numero
    return suma


# Ejemplo de uso
print(es_potencia_de_dos(8))  # True
print(es_potencia_de_dos(12))  # False

resultado = suma_potencias_de_dos()
print("La suma de las potencias de 2 es:", resultado)

