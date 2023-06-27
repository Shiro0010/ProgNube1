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


def primeros_numeros_perfectos(m):
    numeros_perfectos = []
    numero = 6
    exponente = 2
    while len(numeros_perfectos) < m:
        candidato = (2 ** (exponente - 1)) * ((2 ** exponente) - 1)
        if suma_divisores(candidato) == candidato:
            numeros_perfectos.append(candidato)
        exponente += 1
    return numeros_perfectos


def primeras_parejas_amigos(m):
    parejas_amigos = []
    divisores = {}
    a = 1
    while len(parejas_amigos) < m:
        b = suma_divisores(a)
        if b in divisores and divisores[b] == a and a != b:
            parejas_amigos.append((a, b))
        divisores[a] = b
        a += 1
    return parejas_amigos
# Ingresar número por teclado para calcular la suma de los divisores
numero = int(input("Ingrese un número: "))
resultado = suma_divisores(numero)
print("La suma de los divisores de", numero, "es:", resultado)

# Ingresar número por teclado para obtener los primeros números perfectos
m = int(input("Ingrese la cantidad de números perfectos a obtener: "))
numeros_perfectos = primeros_numeros_perfectos(m)
print("Los primeros", m, "números perfectos son:", numeros_perfectos)

# Ingresar número por teclado para obtener las primeras parejas de números amigos
m = int(input("Ingrese la cantidad de parejas de números amigos a obtener: "))
parejas_amigos = primeras_parejas_amigos(m)
print("Las primeras", m, "parejas de números amigos son:", parejas_amigos)
