def split(list):
    result = []
    result.extend(i for i in list if i % 2 != 0)
    print(result)
    return result
