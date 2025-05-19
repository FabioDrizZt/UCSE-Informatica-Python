print(8==8)
print(8==7)

print(8!=7)
print(8!=8)

print(8>7)
print(8>8)

print(8>=7) #true
print(8>=8) #true
print(8>=9) #false

print(8<7)
print(8<8)
print(8<9)

print(8<=7) #false
print(8<=8) #true
print(8<=9) #true

usuario = input("Ingrese usuario")
password = input("Ingrese password")
usuario_correcto =  "admin"
password_correcto =  "123456"
print(f"Usuario ingresado {usuario==usuario_correcto}")
print(f"Usuario ingresado {password==password_correcto}")