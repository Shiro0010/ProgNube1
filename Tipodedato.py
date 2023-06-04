
a= input("ingrese un valor o un texto: ")

try:    
    dato = int(a)
    si = "el valor ingresado es un entero"
except ValueError:
    try:
        dato = float(a)
        si = ("el valor ingresado es un float")
    except ValueError:
        si = "el valor ingresado es un string"

print(si)