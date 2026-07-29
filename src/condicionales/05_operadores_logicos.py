# operadores lógicos: and, or y not

# Operador and
edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")


# Operador or
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")


# Operador not
llueve = False

if not llueve:
    print("Podemos salir al parque.")


# Combinación de operadores lógicos
edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")