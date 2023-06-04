# Variables

nombre = "Juana"
edad = 23
# 2num = 123 # incorrecto
num2 = 12.5
_num2 = 12
num_2 = 11
estado = True

# Constantes
P = 3.14
HORA = 60 # 60 minutos

# Operadores Aritmeticos
a = 50
b = 10
x = a + b # Suma
x = a - b # Resta
x = a * b # Multiplicacion
x = a / b # Division
x = a ** b # Potenciacion

x = a / b
	# 50/10
	# 5
# Modulo (residuo) de la division 
x = a % b
	# 50/10
	# 0

estado = True
	# (-estado)

# Comparadores
a = 5
b = 4
c = 20 

a < b # menor que 
a > b # mayor que 
a <= b # menor o igual que 
	# a < b or a == b	
a >= b # menor o igual que
	# a > b or a == b	
a == b # a es igual a b?
a != b # a es diferente de b?

# Esta operacion retorna un valor booleano True False

# Tablas de Verdad

# V and V = V
# V and F = F
# F and V = F
# F and F = F

# V or V = V
# V or F = V
# F or V = V
# F or F = F

a < b < c #True
a < b and b < c #True
a > b and b > c #True
a > b and (b < c and a > c) #True
a > b or (b < c and a > c) #True
 
# concatenar cadenas de texto str

nombre = "Diego"
apellido = 'Prado'
apellido_temporal = apellido
nombre_completo = nombre + " " + apellido # "Diego Prado"
print(nombre_completo)
print(type(nombre))
numero = '3.14'
print(float(numero))
print (nombre, edad)
print (nombre + " " + str(edad) + " " + str(P))

# Estructuras de control (Condicionales)
print (len(nombre))

# ------------------------------
if len(nombre) == len(nombre):
	print ("son iguales")
else:
	print ("NO son iguales")

# ------------------------------
if len(nombre) == len(nombre):
	print ("son iguales")
elif apellido == apellido:
	print ("Apellidos iguales")
else:
	print ("NO son iguales")

# ------------------------------
if len(nombre) == len(nombre):
	print ("son iguales")
else: 
	if apellido == apellido:
		print ("Apellidos iguales")
	else:
		print ("NO son iguales")

# 
ambiente = 1
# ambiente = 0
# ambiente = "0"
# ambiente = ""
# ambiente = None

if ambiente:
	print ("ambiente tiene algo ")
else: 
	print ("ambiente NO tiene nada ")

# Estructuras Ciclicas

# Bucle FOR
# range(inicio, cond, increm)
for i in range(20, -1, -1):
	# print(type(i))
	print("Diego " + str(i))

# nombre_completo = "Diego Prado"
for c in nombre_completo:
	print (c, end=" ")

# Bucle While

k = 0
while k < 5:
	print(k)
	# k = k + 1
	k += 1


k = 20
while k > -1:
	print(k)
	# k = k + 1
	k -= 1

# Manejo de listas
print("Listas")

lista = [] # lista vacia

lista.append(1)
lista.append(3.14)
lista.append("Hola")

print(len(lista))

# ingresar datos a una lista 
for i in range(5):
	entrada = input("ingrese un valor : ")
	lista.append(entrada)

print(lista)

# mostrar los datos de una lista desde su indice
print("mostrar los datos de una lista desde su indice")
for j in range(len(lista)):
	print (lista[j])

# mostrar los datos partiendo desde el elemento 
print("mostrar los datos partiendo desde el elemento")
for e in lista:
	print(e)


