# Uso de return

def cuadrado(numero):
    return numero ** 2

print(cuadrado(8))


# Retorno múltiple

def estadisticas(lista):
    return (
        sum(lista),
        sum(lista)/len(lista),
        min(lista),
        max(lista)
    )

suma, promedio, menor, mayor = estadisticas([2,4,6,8])

print(suma)
print(promedio)
print(menor)
print(mayor)


# Return anticipado

def dividir_seguro(a, b):

    if b == 0:
        return None

    return a / b

print(dividir_seguro(10,2))
print(dividir_seguro(10,0))