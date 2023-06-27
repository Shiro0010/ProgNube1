def factorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

numero = int(input("Ingrese un número: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
'''use una funcion tal como en la reunion de hace mas o menos un mes, cuando
me encontraba fuera de Popayán.'''
