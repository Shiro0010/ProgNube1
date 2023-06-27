import time
contrasena = ()
x = input("ingrese la contraseña: ")
tm = 0.5
if x == "sagiri":
    contrasena = True
    print("Acceso Concedido.")
else:
    contrasena = False
    print("Contraseña Incorrecta")
    for i in range(5, -1, -1):
        x = input("ingrese la contraseña: ")
        if x == "sagiri":
            contrasena = True
            print("Acceso Concedido.")
            break
        else:
            print("Contraseña incorrecta, quedan ", i, "intentos, espere", tm,"segundos para volver a intentarlo.")
            time.sleep(tm)
            tm += 0.5
            if i == 1:
                print("ultimo intento")