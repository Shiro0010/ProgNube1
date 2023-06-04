try:
    nombre = input("escriba su nombre: ")
    edad = int(input("ingrese su edad: "))
    ident = int(input("ingrese su identificacion: "))
    mayor_de_edad = ""
    if edad < 18:
        mayor_de_edad = "menor de edad"
    else:
        mayor_de_edad = "mayor de edad"
    print("usted se llama:", nombre, ", tiene:", edad,"años" ", su identifiacion es:", ident, "y es", mayor_de_edad)     
except ValueError:
    print("en la edad e identifiacion, solo se admiten numeros")