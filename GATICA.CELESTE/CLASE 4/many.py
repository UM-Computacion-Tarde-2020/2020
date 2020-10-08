def probando_variable(a):
    a = a + ' mundo'
    print("Dentro de la funcion " + str(a))


if __name__ == '__main__':
     b = 'hola'
     print('Antes de la funcion ' + b)
     probando_variable(b)
     print('Despues de la funcion ' + b)
    