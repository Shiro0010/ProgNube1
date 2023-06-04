def convertir_datos(valor, unidad):
    if unidad == 'bits':
        bits = valor
    elif unidad == 'bytes':
        bits = valor * 8
    elif unidad == 'KB':
        bits = valor * 8 * 1024
    elif unidad == 'MB':
        bits = valor * 8 * 1024 * 1024
    elif unidad == 'GB':
        bits = valor * 8 * 1024 * 1024 * 1024
    else:
        print("Unidad no válida. Intente bits, bytes, KB, MB o GB.")
        return []

    return [bits, bits/8, bits/8/1024, bits/8/1024/1024, bits/8/1024/1024/1024]

valor = float(input("Ingrese el valor: "))
unidad = input("Ingrese la unidad (bits, bytes, KB, MB, GB): ")

conversiones = convertir_datos(valor, unidad)

if valor < 0:
    print("solo se admiten unidades positivas")
else:
    print(f"{valor} {unidad} son:")
    print(f"{conversiones[0]} bits")
    print(f"{conversiones[1]} bytes")
    print(f"{conversiones[2]} KB")
    print(f"{conversiones[3]} MB")
    print(f"{conversiones[4]} GB")

