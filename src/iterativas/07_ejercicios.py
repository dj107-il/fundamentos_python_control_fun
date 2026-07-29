# Suma de los primeros 10 números

suma = 0

for i in range(1, 11):
    suma += i

print("La suma es:", suma)

print()

# Tabla del 7

for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

print()

# Números pares

for i in range(2, 21, 2):
    print(i)

print()

# Triángulo con while

fila = 1

while fila <= 5:
    print("*" * fila)
    fila += 1