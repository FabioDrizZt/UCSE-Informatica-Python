frutas = ["Pera","Anana","Sandia","Uva","Uva"]
edades = [25,35,48, 18, 27,85,15]


print(frutas)
print(edades)
print("---- Ordenados ----")
frutas.sort()
edades.sort()
print(frutas)
print(edades)
print("---- Ordenados al reves ----")
frutas.reverse()
edades.reverse()
print(frutas)
print(edades)
print("---- Contar uvas ----")
print(frutas.count("Uva"))
print("---- Eliminar Uvas ----")
frutas.remove("Uva")
print(frutas)
frutas.pop(0)
print(frutas)
print("---- Agregar Uvas ----")
frutas.append("Uva")
print(frutas)
frutas.insert(0,"Uva")
print(frutas)
print("---- Modificar Anana ----")
frutas[3] = "Piña"
print(frutas)
print("---- Acceso a elementos ----")
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
# print(frutas[5]) --> IndexError
print(frutas[-1]) # último elemento
print(frutas[-2]) # anteúltimo elemento
print(frutas[-5]) # primer elemento
# print(frutas[-6]) --> IndexError

print("---- Cantidad de elementos (len) ----")
print(f"cantidad frutas: {len(frutas)}")
print("cantidad edades: " + str(len(edades)))
print("cantidad edades:", (len(edades)))

frutas2 = ("Pera","Anana","Sandia","Uva","Uva")
print(frutas2[0])
print(frutas2[1])
print(frutas2[2])
print(frutas2[3])
print(frutas2[4])
