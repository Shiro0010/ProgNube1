#definimos las variables
radio= float(input("ingrese el radio: "))
area= 3.14159 * radio ** 2
def radio_z (radio):
    if radio <= 0: 
        print("el radio no puede ser 0 o menor a 0")
        return True
    else:
        return False
if radio_z (radio):
    radio = None
else: 
    print("el area del circulo es igual a: ", area)

if radio == None: print("no se pudo determinar el area, prueba usar numeros positivos")