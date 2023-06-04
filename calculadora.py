# Definiendo una función que maneja la división por cero
def division_cero(num1, num2):
    if num2 == 0:
        print("No se puede dividir entre cero, usa otro numero pls")
        return True
    else:
        return False

# Definiendo una función que maneja la potenciación con exponente negativo y base cero
def potencia_invalida(num1, num2):
    if num1 == 0 and num2 < 0:
        print("No se puede elevar cero a un exponente negativo, no tiene sentido xd")
        return True
    else:
        return False

# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Calculamos la suma, resta, división, potenciación, multiplicación y módulo
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
potencia = num1 ** num2
if potencia_invalida(num1, num2):
    potencia = None   
else:
    potencia = num1 ** num2
    print(num1, "^", num2, "=", potencia)
multiplicacion = num1 * num2
modulo = num1 % num2

# Imprimimos los resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La división es:", division)
print("La potenciación es:", potencia)
print("La multiplicación es:", multiplicacion)
print("El módulo es:", modulo)
# Mostrando mensaje de error si se produjo un error en la operación
if potencia is None:
    print("esta operación no es posible de realizar, Prueba usar otros numeros xd.")
if division is None:
    print("esta operación no es posible de realizar, Prueba usar otros numeros xd.")