'''esto es basicamente un juego de adivinar el numero, lo pondre el 1 al 100
y un mensajito de bienvenida y felicitaciones con la cantidad de intentos para ambientar'''
import random

def juego_adivinanza():
    numero_secreto = random.randrange(1, 101)
    intentos = 0

    print("Bienvenido al juego de adivinanza. Adivina el número secreto entre 1 y 100.")

    while True:
        intento = int(input("Ingresa un número: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número secreto es mayor. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("El número secreto es menor. Intenta nuevamente.")
        else:
            print(f"¡Felicitaciones! Adivinaste el número secreto en {intentos} intentos.")
            break

juego_adivinanza()
