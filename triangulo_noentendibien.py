'''este es otro que no comprendi muy bien
tambien tuve que buscar un poco de ayuda, ya que no sabia como calcular el area usando los lados'''
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

semiperimetro = (lado1 + lado2 + lado3) / 2
area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

print("El área del triángulo dados sus lados es:", area)
'''no se si esto sea lo que se pidio.'''