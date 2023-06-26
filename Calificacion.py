try:
    nota = int(input("Ingrese la Calificación en un puntaje del 0 al 100: "))
    if nota < 0:
        print("tan mal le fue como para sacar una nota negativa?")
    elif nota > 100:
        print("q buen estudiant")
    else:
        if nota == 100 and nota > 99:
            print("A+")
        elif nota >= 90:
            print("A")
        elif nota < 90 and nota > 79:
            print("B")
        elif nota < 80 and nota > 69:
            print("C")
        elif nota < 70 and nota > 68:
            print("D")
        else:
            print("F")
except ValueError:
    print("El puntaje en letras se da en base al puntaje en numeros. Ingresa Solo NUMEROS ._.")
'''puse un A+ pq si, y use en and para que los casos sean mas especificos, auqneu podria haberlo hecho de otro modo 
usando >= o <=, pero se me vino a la mente usar el and asi que bueno, ahi esta. puse algunas lineas para evitar que
se procesen letras y para evitar que los puntajes ingresados excedan o sean inferiores a lo establecido'''