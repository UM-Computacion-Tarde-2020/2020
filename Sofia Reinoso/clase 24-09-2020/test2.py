def probando_variable2(c):
    c = c + " mundo"
    print("dentro de la funcion " + c)


if __name__ == '__main__':
    d = "Hola "
    print("antes de la funcion " + d)
    probando_variable2(d)
    print("despues de la funcion " + d)

# hago otro ejemplo pero utilizando listas


def probando_variable_lista(a):
    a.append("hola ")
    print("dentro de la funcion ", end='')
    print(a)


if __name__ == '__main__':
    b = []
    print("antes de la funcion ", end='')
    print(b)
    probando_variable_lista(b)
    print("despues de la funcion ", end='')
    print(b)
