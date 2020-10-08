import sys


def jugada(letra, secuencia):
    error = True
    while error:
        print('Le toca a la ', letra)
        fila = int(input('Ingrese la fila: '))
        columna = int(input('Ingrese la columna: '))
        if fila == 1:
            if fila1[columna - 1] == '':
                fila1[columna - 1] = letra
                error = False
        if fila == 2:
            if fila2[columna - 1] == '':
                fila2[columna - 1] = letra
                error = False
        if fila == 3:
            if fila3[columna - 1] == '':
                fila3[columna - 1] = letra
                error = False
    if fila1[0] == fila1[1] == fila1[2] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila2[0] == fila2[1] == fila2[2] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila3[0] == fila3[1] == fila3[2] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila1[0] == fila2[0] == fila3[0] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila1[1] == fila2[1] == fila3[1] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila1[2] == fila2[2] == fila3[2] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila1[0] == fila2[1] == fila3[2] == letra:
        print('Ganó la ', letra)
        sys.exit()
    if fila1[2] == fila2[1] == fila3[0] == letra:
        print('Ganó la ', letra)
        sys.exit()
    print(fila1)
    print(fila2)
    print(fila3)


fila1 = ['' for i in range(3)]
fila2 = ['' for i in range(3)]
fila3 = ['' for i in range(3)]
print(fila1)
print(fila2)
print(fila3)
letras = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
secuencia = 1
for letra in letras:
    jugada(letra, secuencia)
    secuencia += 1
print('Empate')
