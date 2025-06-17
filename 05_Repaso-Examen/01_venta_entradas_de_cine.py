def calcular_precio(dia, socio):
    precio_general = 1200
    if dia == "Miercoles":
        precio = precio_general - precio_general * 0.20
    else:
        precio = precio_general
    if socio == "S":
        precio -= precio * 0.15
    return precio

cantidad_entradas_socios = 0
cantidad_entradas_no_socios = 0
continuar = "S"
precios = []
while continuar == "S":
    dia = input("Ingrese día de la semana (ej: Lunes, Martes, Miercoles...): ")
    socio = input("¿El cliente es socio? (S/N): ")
    precio = calcular_precio(dia, socio)
    precios.append(precio) # Append agrega el precio a la lista
    if socio == "S":
        cantidad_entradas_socios += 1
    else: 
        cantidad_entradas_no_socios += 1
    print(f"El precio final de la entrada es: ${precio}")
    continuar = input("¿Desea ingresar otro cliente? (S/N): ")

total_recaudado = sum(precios) # Sum suma todos los precios
print(f"Total Recaudado: ${total_recaudado}")
print(f"El menor precio pagado es: ${min(precios)}")
print(f"El mayor precio pagado es: ${max(precios)}")
print(f"Cantidad de entradas a socios: {cantidad_entradas_socios}")
print(f"Cantidad de entradas a no socios: {cantidad_entradas_no_socios}")