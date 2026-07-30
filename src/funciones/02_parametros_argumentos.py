# Parámetros y argumentos

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Juan")


# Parámetros con valor por defecto

def bienvenida(nombre, mensaje="Bienvenido"):
    print(f"{mensaje}, {nombre}")

bienvenida("Carlos")
bienvenida("Ana", "Buenos días")


# Parámetros por nombre

def dividir(dividendo, divisor):
    return dividendo / divisor

print(dividir(divisor=2, dividendo=10))


# *args

def sumar(*numeros):
    return sum(numeros)

print(sumar(1,2,3,4,5))


# **kwargs

def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, ":", valor)

mostrar_datos(nombre="Juan", edad=20, ciudad="Medellín")