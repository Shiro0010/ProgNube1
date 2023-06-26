#organizar numeros de menor a mayor 
num1 = float(input("ingrese el primer numero: "));
num2 = float(input("ingrese el segundo numero: "));

print("los valores ingresados son: " + str(num1), "y", str(num2));
print("ordenados de menor a mayor serian: ");
if num1 < num2:
    print(num1, ",", num2);
elif num1 > num2:
    print(num2, ",", num1);
else:
    print("oh vaya, los numero son iguales, independientemente del orden que se les de xd");