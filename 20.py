oracion = input("Ingrese una oración: ")
letra_buscar = input("Ingrese la letra a buscar: ")
letra_buscar = letra_buscar.lower()
contador = 0

for letra in oracion:
    letra = letra.lower()
    if letra == letra_buscar:
        contador += 1


print(f"La oración tiene {contador} letras '{letra_buscar}'")
'''el letra lower es para que se puedan distinguir las letras sin importar que sean Mayuscular o minusculas
tuve que leer sobre eso jksajda'''