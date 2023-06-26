'''necesito investigar sobre el funcionmiento del pico y placa, sin embargo en el codigo esta un ejemplo suponiendo
que asi funciona, pues en colombia el pico y placa tiene que ver con dias pares e impares. proximamente estare haciendo
este mismo codigo pero basado en lass leyes colombianas'''

placa = input("Ingrese el último dígito de la placa de su vehículo: ")
dia = input("Ingrese el día de la semana (en minúsculas, ej. lunes, martes, ...): ")

if dia == "lunes" and (placa == "1" or placa == "2"):
    print("Su vehículo tiene pico y placa los lunes.")
elif dia == "martes" and (placa == "3" or placa == "4"):
    print("Su vehículo tiene pico y placa los martes.")
elif dia == "miércoles" and (placa == "5" or placa == "6"):
    print("Su vehículo tiene pico y placa los miércoles.")
elif dia == "jueves" and (placa == "7" or placa == "8"):
    print("Su vehículo tiene pico y placa los jueves.")
elif dia == "viernes" and (placa == "9" or placa == "0"):
    print("Su vehículo tiene pico y placa los viernes.")
else:
    print("Su vehículo no tiene pico y placa en el día especificado.")
    
'''siendo este el resultado, si me equivoco en algo, me gustaria que me especificara que es para trabajar en solucionarlo...
gracias profe.'''