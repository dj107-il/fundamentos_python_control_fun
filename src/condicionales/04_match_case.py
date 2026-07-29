fruta = "manzana"

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")


# match-case con una tupla

punto = (0, 0)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")