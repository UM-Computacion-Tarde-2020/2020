def probando_variable(a):
    a.append("hola")
    print("dentro de la funcion a", end="")
    print(a)
    c = ["mundo"]
    print("dentro de la funcion c", end="")
    print(c)
    return(c)

if __name__ == '__main__':
    b = []
    print('antes de la funcion ', end="")
    print(b)
    d = probando_variable(b)
    print('despues de la funcion b ', end="")
    print (b)
    print('despues de la funcion d ', end="")
    print (d)