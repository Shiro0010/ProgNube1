'''no entendi muy bien lo de 'el central', no se si se referia a si es mayor o menor.
yo lo hare como menor a mayor.'''
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    central = num1
elif num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
    central = num2
else:
    central = num3

print("El número central es:", central)
