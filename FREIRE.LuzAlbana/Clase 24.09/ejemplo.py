def probando_variable(a):
    a.append('hola ')
    print("Dentro de la funcion a ", end='')
    print(a)
    c = ['mundo']
    print("Dentro de la funcion c ", end='')
    print(c)
    return c


if _name_ == '_main_':
    b = []
    d = probando_variable(b)
    print("Antes de la funcion b ", end='')
    print(b)
    print("Despues de la funcion d ", end='')
    print(d)