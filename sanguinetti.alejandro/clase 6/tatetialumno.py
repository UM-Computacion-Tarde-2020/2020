f1 = [' ' for i in range(3)]
f2 = [' ' for i in range(3)]
f3 = [' ' for i in range(3)]


print(f1)
print(f2)
print(f3)

fila = int(input('fila'))
columna = int(input('colomna'))
if fila == 1:
    if f1[columna - 1] == ' ':
        f1[columna - 1] = 'x'
        error = False
if fila == 2:
    if f2[columna - 1] == ' ':
        f2[columna - 1] = 'x'
        error = False
if fila == 3:
    if f3[columna - 1] == ' ':
        f3[columna - 1] = 'x'
        error = False
print(f1)
print(f2)
print(f3)

error = True
fila = int(input('fila'))
columna = int(input('colomna'))
if fila == 1:
    if f1[columna - 1] == ' ':
        f1[columna - 1] = 'o'
        error = False
if fila == 2:
    if f2[columna - 1] == ' ':
        f2[columna - 1] = 'o'
        error = False
if fila == 3:
    if f3[columna - 1] == ' ':
        f3[columna - 1] = 'o'
        error = False
print(f1)
print(f2)
print(f3)
