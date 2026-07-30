"""
Ejercicio integrador de la lección 7
"""

def calcular_precio(precio, descuento=0):

    """
    Calcula el precio final de un producto.

    Args:
        precio: precio original
        descuento: porcentaje de descuento

    Returns:
        Precio con descuento.
    """

    if precio < 0:
        return None

    return precio - (precio * descuento / 100)


def mostrar_producto(nombre, precio):
    print(f"{nombre}: ${precio}")


precio_final = calcular_precio(250000, 15)

mostrar_producto("Mouse Gamer", precio_final)