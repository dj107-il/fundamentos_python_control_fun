# Definición de funciones

def saludar():
    print("¡Hola, mundo!")

saludar()


def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


resultado = calcular_area_rectangulo(5, 3)
print("Área:", resultado)


def es_par(numero):
    return numero % 2 == 0


print(es_par(10))


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print(celsius_a_fahrenheit(25))


# Funciones como variables

convertir = celsius_a_fahrenheit
print(convertir(30))