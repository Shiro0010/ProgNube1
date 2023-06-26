#vamos a hacer el codigo en un bloque de intento. explicacion en el proximo comentario
try:
    print("bienvenido a Disconet, por favor, a continuación: ")
    nombre =  input("Ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    #haremos la funcionalidad para reconocer si es o no mayor de edad
    if edad >= 18:
    #reconocido el mayor de edad, se pedira la identificación para verificar datos
        id = int(input("para verificar los datos. ingrese su # de identificación: "))
        if id == 1234321:
            print(nombre,", Bienvenida de nuevo")
        elif id == 98765432:
            print(nombre,", bienvenido de nuevo")
    #aqui, al no estar registrada la identificacion, se mostrara un mensjae que indica que los datos son erroneos
    #o no se han registrado.
        else:
            print("identificación no registrada. Favor registrarse en la pagina web.")
            print("no se ha podido encontrar al usuario. favor registrarse o verificar los datos.")
    #este else dara el mensaje de acceso denegado si el usuario no es mayor de edad
    else:
        print(" menor de edad, acceso denegado.")
except ValueError:
    print ("por favor, utilice numeros enteros positivos en las casillas de identificación y edad.")

'''se presentan 2 identificaciones para ejemplificar. se hizo en un bloque try para evitar que se ingresen letras
en las casillas numéricas.'''