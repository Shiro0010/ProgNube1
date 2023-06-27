try:
    import time
    rng = (int(input("Ingrese el numero desde el que desea Empezar: ")))
    lim1= 10
    lim2 = 10
    for i in range((rng), (lim1 + 1), 1):
        print(i)
        if i == 10:
            x = input("Desea continuar? (si/no): ")
            if x == "si":
                lim1 += 10
                for i in range ((lim2),(lim1) + 1, 1):
                    print(i)
                    time.sleep(0.5)
                    x = "no"
            elif x == "no":
                break
        time.sleep(0.5)
except ValueError:
    print("Solo se admite un rango numérico")
    ''' este codigo hace la cuenta hasta el numero 20, parando a preguntar en el numero 10
    se puede extender mucho más y eso, pero lo deje asi como prueba y para no alargarlo mucho
    el siguiente codigo es una version alternativa mejorada
    inicio = int(input("Ingrese el número de inicio: "))
final = int(input("Ingrese el número final: "))
preguntar_cada = 10

while True:
    if inicio > final:
        print("El número de inicio debe ser menor o igual que el número final.")
        break

    for numero in range(inicio, final + 1):
        print(numero)

        if numero % preguntar_cada == 0:
            respuesta = input(f"¿Desea continuar? (s/n) (Próximo número: {numero+1}): ")
            if respuesta == "s" or respuesta == "S":
                final = numero + preguntar_cada
            else:
                break

    else:
        continue

    break

print("Fin del programa")'''
