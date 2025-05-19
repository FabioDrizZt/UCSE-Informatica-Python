# Operadores Lógicos
# AND
# Es verdadero cuando ambas partes son verdaderas

print(True and True) #true
print(False and True)
print(True and False)
print(False and False)

""" usuario = input("Ingrese usuario: ")
password = input("Ingrese password: ")
usuario_correcto =  "admin"
password_correcto =  "123456"
print(f"Puede ingresar: {usuario==usuario_correcto and password==password_correcto}") """

# OR
# Es falso cuando ambas partes son falsas

print(True or True)
print(False or True)
print(True or False)
print(False or False) #falso

# NOT
# Valor negado de lo anterio
print(not(True))
print(not(False))

edad = 19
rango_edad = edad >= 18 and edad <=100
no-esta-rango_edad = not (edad >= 18 and edad <=100) # edad < 18 or edad>100