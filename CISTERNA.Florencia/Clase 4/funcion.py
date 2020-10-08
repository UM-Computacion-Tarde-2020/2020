def split(a):
    list = []
    list.extend([i for i in a])
    for i in list:
        b = i/2
        if b == int(b):
            list.remove(i)
    print(list)
    return (list)
