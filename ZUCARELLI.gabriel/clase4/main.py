def split(list):
    # creo una lista vacia para poner los valores impares
    result = []
    #recorro la lista list y a cada valor impar lo agrego a la lista return
    result.extend([i for i in list if i % 2 !=0])
    #devuelvo la lista return creada anteriormente
    print(result)
    return result 
    