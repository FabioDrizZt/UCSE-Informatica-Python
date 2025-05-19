mi_nombre="Fabio"
print(type(mi_nombre))

edad = 37
print(edad)
print(type(edad))

ciudad = "Jujuy"
ciudad = "Buenos Aires"
print(ciudad)

#Anteponer la f a una cadena permite mostrar variables
print(f"Hola soy {mi_nombre}, tengo {edad+5} años")

mi_nombre, edad, ciudad = "Maria" , 25, "La quiaca"
print(f"Hola soy {mi_nombre}, tengo {edad+5} años y soy de {ciudad}")
