fila1 = [" " for i in range(3)]
fila2 = [" " for i in range(3)]
fila3 = [" " for i in range(3)]

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("Le toca a la x")
    fila = int(input("Ingrese fila: "))
    columna = int(input("Ingrese columna: "))

    if fila == 1:
        if fila1[columna - 1] == " ":
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == " ":
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == " ":
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("Le toca a la o")
    fila = int(input("Ingrese fila: "))
    columna = int(input("Ingrese columna: "))

    if fila == 1:
        if fila1[columna - 1] == " ":
            fila1[columna - 1] = 'o'
            error = False
    if fila == 2:
        if fila2[columna - 1] == " ":
            fila2[columna - 1] = 'o'
            error = False
    if fila == 3:
        if fila3[columna - 1] == " ":
            fila3[columna - 1] = 'o'
            error = False


print(fila1)
print(fila2)
print(fila3)

# esto se debe repetir 9 veces para completar el tateti
