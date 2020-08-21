def suma(a, b):
    resultado = a + b
    return resultado


if __name__ == '__main__':
    operando1 = int(input("ingrese un valor: "))
    operando2 = int(input("ingrese otro valor: "))
    resultado = suma(operando1, operando2)
    print("resultado ", resultado)
