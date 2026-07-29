# Expresiones condicionales o condicionales ternarios

edad = 17

mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."

print(mensaje)


# Obtener el número mayor entre dos valores

a = 1
b = 2

print("El máximo es:", a if a > b else b)


# Evitar una división por cero

dividendo = 10
divisor = 0

resultado = (
    dividendo / divisor
    if divisor != 0
    else "División por cero no permitida"
)

print(resultado)