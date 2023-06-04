numero = int(input("Ingresa un número entero: "))
binario = []
while numero > 0:
    residuo = numero % 2
    binario.append(residuo)
    numero = numero // 2
print("El valor binario es:", "".join(map(str, reversed(binario))))