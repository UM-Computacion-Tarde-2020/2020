import sys

fila1 = [' ' for i in range(3)]
fila2 = [' ' for i in range(3)]
fila3 = [' ' for i in range(3)]

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("1Le toca a la x")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("1Le toca a la o")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'o'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'o'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'o'
            error = False

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("2Le toca a la x")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("2Le toca a la o")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'o'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'o'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'o'
            error = False

print(fila1)
print(fila2)
print(fila3)

error = True
while error:
    print("3Le toca a la x")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)
if fila1[0] == fila1[1] == fila1[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila2[0] == fila2[1] == fila2[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila3[0] == fila3[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[0] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[1] == fila2[1] == fila3[1] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[2] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[1] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()
error = True
while error:
    print("3Le toca a la o")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'o'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'o'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'o'
            error = False

print(fila1)
print(fila2)
print(fila3)
if fila1[0] == fila1[1] == fila1[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila2[0] == fila2[1] == fila2[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila3[0] == fila3[1] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[0] == fila2[0] == fila3[0] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[1] == fila2[1] == fila3[1] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[2] == fila2[2] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[0] == fila2[1] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[2] == fila2[1] == fila3[0] == 'o':
    print('ganaron las o')
    sys.exit()
error = True
while error:
    print("Le toca a la x")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)
if fila1[0] == fila1[1] == fila1[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila2[0] == fila2[1] == fila2[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila3[0] == fila3[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[0] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[1] == fila2[1] == fila3[1] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[2] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[1] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()

error = True
while error:
    print("Le toca a la o")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'o'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'o'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'o'
            error = False

print(fila1)
print(fila2)
print(fila3)
if fila1[0] == fila1[1] == fila1[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila2[0] == fila2[1] == fila2[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila3[0] == fila3[1] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[0] == fila2[0] == fila3[0] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[1] == fila2[1] == fila3[1] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[2] == fila2[2] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[0] == fila2[1] == fila3[2] == 'o':
    print('ganaron las o')
    sys.exit()
if fila1[2] == fila2[1] == fila3[0] == 'o':
    print('ganaron las o')
    sys.exit()

error = True
while error:
    print("Le toca a la x")
    fila = int(input("Ingrese fila"))
    columna = int(input("Ingrese columna"))

    if fila == 1:
        if fila1[columna - 1] == ' ':
            fila1[columna - 1] = 'x'
            error = False
    if fila == 2:
        if fila2[columna - 1] == ' ':
            fila2[columna - 1] = 'x'
            error = False
    if fila == 3:
        if fila3[columna - 1] == ' ':
            fila3[columna - 1] = 'x'
            error = False

print(fila1)
print(fila2)
print(fila3)
if fila1[0] == fila1[1] == fila1[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila2[0] == fila2[1] == fila2[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila3[0] == fila3[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[0] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[1] == fila2[1] == fila3[1] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[2] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[0] == fila2[1] == fila3[2] == 'x':
    print('ganaron las x')
    sys.exit()
if fila1[2] == fila2[1] == fila3[0] == 'x':
    print('ganaron las x')
    sys.exit()
print('empate')
