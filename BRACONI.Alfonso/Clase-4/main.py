def split(lista_impares):
    list=[]
    list.extend([i for i in lista_impares])
    for i in list:
        if i % 2 ==0:
            list.remove(i)
    return list