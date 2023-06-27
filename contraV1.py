'''si = ()
no = input("Ingrese la contraseña: ")
si = no
while si != "sagiri":
    print("contraseña erronea")
    no = input("ingrese la contraseña: ")
    si = no
print("Acceso concedido")'''
'''de ejercicios parte 3, este era uno de los mas sencillos, aunque creo que me extendi innecesariamente
pero bueno, asi quedo funcional.'''
'''El anterior fue la primera version. despues de leer un poco, me di cuenta que el modulo time debia ser
importado, luego empece a experimentar con la funcion For hasta que obtuve el siguiente resultado'''
import time
pausaxd = 1
for i in range (1, 5, 1):
    i = input("Ingrese la contraseña: ")
    if i == "Sagiri":
        print("Acceso Concedido")
        break
    else:    
        print("Acceso Denegado, espere", pausaxd,"segundos para intentarlo de nuevo.")
        time.sleep(pausaxd)
        pausaxd += 1.5
'''en este codigo se implementa el receso, y el limite de intentos, ademas de un letrero de acceso denegao/concedido'''
#############################################################33
'''enserio tengo que hacerlo con un booleano?
bueno.
lo hare en una version 2.0, no quiero deshacer esta jdjdjadlkjahdf'''