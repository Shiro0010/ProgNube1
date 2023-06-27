'''esto crece como el almacenamiento o la RAM (2,4,8,16,32,64,128,256,512...)'''
numero = int(input("Ingrese un número: "))
max_terminos = int((2 ** numero) / 2)

for i in range(max_terminos):
    termino = 2 ** i
    if termino <= numero:
        print(termino)
    else:
        break
'''solo pude dar abasto hasta 1024, en una futura actualizacion estare implementando numeros mas altos'''