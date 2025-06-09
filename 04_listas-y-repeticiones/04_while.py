contador = 1
while contador<=10:
    print("Iteración N°:",contador)
    contador+=2
    if contador>5:
        break
else:
    print("Fin del bucle exitoso!")
    
frutas = ["Pera","Anana","Sandia","Uva","Uva"]

index = 0
encontrado=False
while index<len(frutas):
    print(frutas[index])
    if frutas[index]=="Anana":
        encontrado=True
        break
    index+=1
    
if encontrado:
    print("Se encontro la fruta anana en:",index+1)
else:
    print("No se encontro la fruta anana")
    
    
encontrado=False
for index,fruta in enumerate(frutas):
    print(fruta)
    if fruta=="Anana":
        encontrado=True
        break
    
if encontrado:
    print("Se encontro la fruta anana:",index+1)
else:
    print("No se encontro la fruta anana")
    
