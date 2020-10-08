import sys


def jugada(letra, secuencia):
    error = True
    while error:
        print(secuencia, ".Le toca a la ", letra)
        fila = int(input("Ingrese fila"))
        columna = int(input("Ingrese columna"))

        if fila == 1:
            if fila1[columna - 1] == ' ':
                fila1[columna - 1] = letra
                error = False
        if fila == 2:
            if fila2[columna - 1] == ' ':
                fila2[columna - 1] = letra
                error = False
        if fila == 3:
            if fila3[columna - 1] == ' ':
                fila3[columna - 1] = letra
                error = False

    print(fila1)
    print(fila2)
    print(fila3)

    #   Horizontales
    if fila1[0] == fila1[1] == fila1[2] == letra:
        print('ganó la ', letra)
        sys.exit()
    if fila2[0] == fila2[1] == fila2[2] == letra:
        print('ganó la ', letra)
        sys.exit()
    if fila3[0] == fila3[1] == fila3[2] == letra:
        print('ganó la ', letra)
        sys.exit()
    #   Verticales
    if fila1[0] == fila2[0] == fila3[0] == letra:
        print('ganó la ', letra)
        sys.exit()
    if fila1[1] == fila2[1] == fila3[1] == letra:
        print('ganó la ', letra)
        sys.exit()
    if fila1[2] == fila2[2] == fila3[2] == letra:
        print('ganó la ', letra)
        sys.exit()
    #   Diagonales
    if fila1[0] == fila2[1] == fila3[2] == letra:
        print('ganó la ', letra)
        sys.exit()
    if fila1[2] == fila2[1] == fila3[0] == letra:
        print('ganó la ', letra)
        sys.exit()


# acá arranca
fila1 = [' ' for i in range(3)]
fila2 = [' ' for i in range(3)]
fila3 = [' ' for i in range(3)]

print(fila1)
print(fila2)
print(fila3)

jugada('x', 1)
jugada('o', 2)
jugada('x', 3)
jugada('o', 4)
jugada('x', 5)
jugada('o', 6)
jugada('x', 7)
jugada('o', 8)
jugada('x', 9)

print("Empate")
