def split(list):
    impares = []
    #creo una lista vacia para ponr los valores impares
    impares.extend([i for i in list if i % 2 != 0])
    #recorro la lista y agrego los valores impares a la lista
    print(impares)
    #imprimo la lista
    return impares
    #devuelvo la lista
