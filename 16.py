def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primoswe(n):
    for num in range(2, n + 1):
        if es_primo(num):
            print(num)


# Ingresar número por teclado
numero = int(input("Ingrese un número natural: "))
print("Números primos hasta", numero)
primoswe(numero)
