def probando_variable(a):
    a = a + 1
    print("dentro de la funcion " + str(a))


if __name__ == '__main__':
    b = 3
    print("antes de la funcion " + str(b))
    probando_variable(b)
    print("despues de la funcion " + str(b))

# debo convertir la variable numerica en un string para poder trabajar con ella
# para los strings ocurre lo mismo que con los numeros
# he demostrado que si uso una variable numerica o de string y la utilizo como parametro de una funcion, yo puedo modificar a este parametro
# pero fuera de la funcion la variable no se verá afectada, porq es una copia del valor que utilizo
