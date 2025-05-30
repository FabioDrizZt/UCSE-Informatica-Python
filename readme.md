# 🐍 Introducción a Python - UCSE Informática 2025

¡Bienvenido/a a este repositorio! Aquí encontrarás ejemplos y explicaciones de los conceptos fundamentales de Python, pensados para quienes inician en la programación. 📚✨

## 📦 Estructura del repositorio
- **01_Basicos/**: Conceptos básicos de Python
- **02_Operadores/**: Operadores aritméticos, de comparación y lógicos
- **03_condicionales/**: Estructuras condicionales y funciones

---

## 1️⃣ Conceptos Básicos

### 👋 Hola Mundo y la función `print()`
El clásico primer programa. Aprenderás a mostrar mensajes en pantalla usando `print()` y a interactuar con el usuario mediante `input()`.

```python
print("Hola mundo")
nombre = input("¿Cómo te llamas?")
print("Hola", nombre)
```

### 📝 Tipos de datos
Python tiene varios tipos de datos:
- `int`: Números enteros
- `float`: Números decimales
- `complex`: Números complejos
- `str`: Cadenas de texto
- `bool`: Booleanos (`True` o `False`)
- `None`: Ausencia de valor

Puedes usar `type()` para saber el tipo de un dato:
```python
print(type(10))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("hola")) # <class 'str'>
```

### 🏷️ Variables y f-strings
Las variables almacenan información. Puedes usar f-strings para mostrar variables dentro de textos:
```python
nombre = "Ana"
edad = 20
print(f"Hola soy {nombre} y tengo {edad} años")
```

### 🔄 Conversión de tipos (Casting)
Convierte entre tipos de datos usando funciones como `int()`, `str()`, etc.:
```python
edad = int(input("Ingrese su edad: "))
print("En 5 años tendrás", edad + 5)
```

---

## 2️⃣ Operadores en Python

### ➕ Operadores aritméticos
Permiten realizar operaciones matemáticas:
- Suma: `+`
- Resta: `-`
- Multiplicación: `*`
- División: `/`
- Potencia: `**`
- Módulo (resto): `%`

```python
print(7 + 8)
print(2 ** 3)  # 2 elevado a 3
```

### 🔍 Operadores de comparación
Comparan valores y devuelven `True` o `False`:
- Igual: `==`
- Distinto: `!=`
- Mayor: `>`
- Menor: `<`
- Mayor o igual: `>=`
- Menor o igual: `<=`

```python
print(8 == 8)  # True
print(5 < 3)   # False
```

### 🧠 Operadores lógicos
Combinan condiciones:
- `and`: Verdadero si ambas condiciones lo son
- `or`: Verdadero si al menos una lo es
- `not`: Invierte el valor lógico

```python
print(True and False) # False
print(not True)      # False
```

---

## 3️⃣ Estructuras Condicionales y Funciones

### 🔀 Condicionales: if, elif, else
Permiten tomar decisiones según condiciones:
```python
edad = int(input("¿Qué edad tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

### 🧩 Funciones
Agrupan instrucciones bajo un nombre para reutilizarlas:
```python
def saludar():
    print("Hola mundo!")
    print("El clima:")
    print("Hoy está nublado y fresco")

saludar()
```

---

## 🚀 ¡A practicar!
Explora cada carpeta y ejecuta los ejemplos para afianzar los conceptos. ¡La mejor forma de aprender es programando! 💻🎉

---

> Repositorio creado para la materia Informática - UCSE 2025. Docente: Fabio
