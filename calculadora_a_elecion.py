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
try:
    # Pidiendo al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Pidiendo al usuario que seleccione la operación a realizar
    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("6. Módulo de división")

    opcion = int(input("Ingrese su elección (1/2/3/4/5/6): "))

    # Realizando la operación seleccionada
    if opcion == 1:
        resultado = num1 + num2
        print(num1, "+", num2, "=", resultado)
    elif opcion == 2:
        resultado = num1 - num2
        print(num1, "-", num2, "=", resultado)
    elif opcion == 3:
        resultado = num1 * num2
        print(num1, "*", num2, "=", resultado)
    elif opcion == 4:
        if division_cero(num1, num2):
            resultado = None
        else:
            resultado = num1 / num2
            print(num1, "/", num2, "=", resultado)
    elif opcion == 5:
        if potencia_invalida(num1, num2):
            resultado = None
        else:
            resultado = num1 ** num2
            print(num1, "^", num2, "=", resultado)
    elif opcion == 6:
        if division_cero(num1, num2):
            resultado = None
        else:
            resultado = num1 % num2
            print(num1, "%", num2, "=", resultado)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        resultado = None

    # Mostrando mensaje de error si se produjo un error en la operación
    if resultado is None:
        print("esta operación no es posible de realizar, Prueba usar otros numeros xd.")
except ValueError:
    print("solo numeros, chistoso.")