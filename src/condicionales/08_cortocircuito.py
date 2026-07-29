# Evaluación de cortocircuito

# Evitar acceder a una posición inexistente
lista = []

if lista and lista[0] == "Python":
    print("El primer elemento es 'Python'.")
else:
    print("La lista está vacía o el primer elemento no es 'Python'.")


# Evitar una división por cero
dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")


# Uso de any()
numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")


# Uso de all()
condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")