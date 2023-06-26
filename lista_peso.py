menos_40kg = 0
entre_40_50kg = 0
mas_50_menos_60kg = 0
mas_igual_60kg = 0

while True:
    peso = float(input("Ingrese el peso del alumno (ingrese un # negativo para finalizar. xd): "))

    if peso <= -1:
        break

    if peso < 40:
        menos_40kg += 1
    elif peso >= 40 and peso < 50:
        entre_40_50kg += 1
    elif peso >= 50 and peso < 60:
        mas_50_menos_60kg += 1
    elif peso >= 60:
        mas_igual_60kg += 1

print("Estadísticas de pesos de alumnos:")
print("Alumnos de menos de 40 kg:", menos_40kg)
print("Alumnos entre 40 y 50 kg:", entre_40_50kg)
print("Alumnos de más de 50 kg y menos de 60 kg:", mas_50_menos_60kg)
print("Alumnos de más o igual a 60 kg:", mas_igual_60kg)

'''aqui use un booleano para poder ingresar las cantidades de peso cuales quiera y 
en caso de terminar de ingresar los datos, ingresar "-1" para finalizar el proceso de
recopilacio de datos y pasar a mostrar la lista. ademas de impedir que se pongan pesos negativos'''