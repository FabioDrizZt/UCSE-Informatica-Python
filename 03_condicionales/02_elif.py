nota = int(input("Ingrese nota del alumno: "))

# Validar PRIMERO el error
if (nota<0 or nota>10):
    print("Nota invalida")
elif nota>=7:
    print("Promocionado")    
elif nota>=4:
    print("Regular")
else:
    print("Reprobado")