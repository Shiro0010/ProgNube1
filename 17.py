'''este fue una combinacion de codigos mas sencillos que las otras operaciones matematcias mas complejas xD'''
acumulado = 0
contador = 0
numero = int(input("Ingrese un número (0 para finalizar): "))

while numero != 0:
    acumulado += numero
    contador += 1
    numero = int(input("Ingrese un número (0 para finalizar): "))

'''lawea para mostrar el num acumulao y el num de acumulaciones'''

print("El número acumulado es:", acumulado)
print("La cantidad de números ingresados es:", contador)
