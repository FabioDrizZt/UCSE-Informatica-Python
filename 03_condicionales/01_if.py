edad = input("Ingrese su edad: print")
if edad.isdigit() and int(edad) >= 18:
    ("Eres mayor de edad")
else:
    print("Eres menor de edad")

usuario = input("Ingrese su nombre de usuario: ")
print("usuario:", usuario)
print("usuario:", usuario.lower().strip())

if usuario.lower().strip() == "admin":
    print("Bienvenido administrador")
else:
    print("Bienvenido usuario comun: ", usuario)