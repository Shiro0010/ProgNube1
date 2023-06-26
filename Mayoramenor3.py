#lo mismo de menor a mayor pero con 3 numeros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

if num1 != mayor and num1 != menor:
    intermedio = num1
elif num2 != mayor and num2 != menor:
    intermedio = num2
else:
    intermedio = num3

print("Los números ingresados son:", num1, ",", num2, "y", num3)
print("Organizados de forma descendente son:", mayor, ",", intermedio, ",", menor)
