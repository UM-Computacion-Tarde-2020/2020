def probando_variable(a):
    a.append('hola')
    print("Dentro de la función a:", end='')
    print(a)
    c = ['mundo']
    print("Dentro de la función c:", end='')
    print(c)
    return c


if __name__ == '__main__':
    b = []
    print('Antes de la función:', end='')
    print(b)
    d = probando_variable(b)
    print('Después de la función:', end='')
    print(b)
    print('Después de la función:', end='')
    print(d)
