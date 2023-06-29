'''mas operaciones matematicas que no comprendo, se incluyesn el ejercicio #13,14 y 15'''
import math

def suma_divisores(n):
    suma = 1
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            suma += i
            complemento = n // i
            if complemento != i:
                suma += complemento
    return suma


def primeros_numeros_perfectos(numero):
    numeros_perfectos = []
    exponente = 2
    while True:
        candidato = (2 ** (exponente - 1)) * ((2 ** exponente) - 1)
        if candidato >= numero:
            break
        if suma_divisores(candidato) == candidato:
            numeros_perfectos.append(candidato)
        exponente += 1
    return numeros_perfectos


def primeras_parejas_amigos(numero):
    parejas_amigos = []
    divisores = {}
    a = 1
    while True:
        b = suma_divisores(a)
        if b in divisores and divisores[b] == a and a != b:
            parejas_amigos.append((a, b))
        divisores[a] = b
        a += 1
        if a > numero:
            break
    return parejas_amigos

numero = int(input("Ingrese un número: "))
resultado = suma_divisores(numero)
print("La suma de los divisores de", numero, "es:", resultado)

numeros_perfectos = primeros_numeros_perfectos(numero)
if numeros_perfectos:
    print("Los números perfectos antes de", numero, "son:", numeros_perfectos)
else:
    print("No hay números perfectos antes de", numero)

parejas_amigos = primeras_parejas_amigos(numero)
if parejas_amigos:
    print("Las parejas de números amigos antes de", numero, "son:", parejas_amigos)
else:
    print("No hay parejas de números amigos antes del", numero)

