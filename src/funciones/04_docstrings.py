def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista.

    Args:
        numeros: lista de números.

    Returns:
        Promedio de la lista.
    """
    return sum(numeros) / len(numeros)


print(calcular_promedio([5,7,9]))


help(calcular_promedio)


def es_mayor_edad(edad):
    """
    Verifica si una persona es mayor de edad.
    """
    return edad >= 18


print(es_mayor_edad(20))