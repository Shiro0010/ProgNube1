# Obtener los datos del trabajador
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
sueldo_mensual = float(input("Ingrese el sueldo mensual: "))

# Calcular el salario base
if horas_trabajadas <= 35:
    salario_base = horas_trabajadas * tarifa
else:
    horas_normales = 35
    horas_extras = horas_trabajadas - 35
    salario_base = (horas_normales * tarifa) + (horas_extras * tarifa * 1.5)

# Calcular los impuestos
if sueldo_mensual <= 2000:
    impuestos = 0
elif sueldo_mensual <= 2220:
    impuestos = (sueldo_mensual - 2000) * 0.2
else:
    impuestos = 220 * 0.2 + (sueldo_mensual - 2220) * 0.3

# Calcular el salario neto
salario_neto = salario_base - impuestos

# Mostrar la nómina del trabajador
print("Nómina Semanal -", nombre)
print("Salario Base:", salario_base)
print("Impuestos:", impuestos)
print("Salario Neto:", salario_neto)


