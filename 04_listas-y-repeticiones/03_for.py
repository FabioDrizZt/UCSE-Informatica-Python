frutas = ["Pera","Anana","Sandia","Uva","Uva"]
edades = [25,35,48, 18, 27,85,15]

for fruta in frutas:
    print(fruta)
    
for edad in edades:
    print(edad)
    
for index in range(10):
    print(f"Numero: {index+1}")
    
for i, fruta in enumerate(frutas):
    print(f"fruta en la posicion {i}: {fruta}")
    
for i, edad in enumerate(edades):
    print(f"edad de la persona N°{i}: {edad}")

print(list(enumerate(frutas)))

suma = 0
for edad in edades:
    suma+=edad # suma=suma+edad
else:
    print("La suma de las edades es:", suma)
    print("El promedio de las edades es:", round(suma/len(edades)))

cuadrados2=[]
for i in range(10):
    cuadrados2.append(i**2)
print(cuadrados2)

cuadrados = [i**2 for i in range(10)]
print(cuadrados) 
