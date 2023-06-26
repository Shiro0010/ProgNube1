#calcular la raiz cuadrada de un numero considerando los casos donde el numero dado es negativo
import cmath

numero = float(input("Ingrese un número: "))

if numero >= 0:
    raiz_cuadrada = numero ** 0.5
    print("La raíz cuadrada de", numero, "es", raiz_cuadrada)
else:
    raiz_cuadrada_compleja = cmath.sqrt(numero)
    print("La raíz cuadrada de", numero, "es", raiz_cuadrada_compleja)
#me tomo un buen rato investigando y al final consulte en GPT para que me expliquecomo hacer esto jaja
#no se si debe procesar numeros negativos asi que bueno, lo hice asi
#sigo sin entender como se leen los resultados negativos, o bueno, porque llevan una "j"
