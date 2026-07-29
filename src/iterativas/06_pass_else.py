print("PASS")

for i in range(5):

    if i == 2:
        pass
    else:
        print(i)

print("\nELSE EN FOR")

for i in range(5):
    print(i)
else:
    print("El bucle terminó normalmente")

print("\nELSE CON BREAK")

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Nunca apareceré")