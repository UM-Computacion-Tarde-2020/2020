def suma(a, b):
    resultado = a + b
    return resultado


if __name__ == '__main__':
    operando1 = int(input("Ingrese un valor: "))
    operando2 = int(input("Ingrese otro valor: "))
    resultado = suma(operando1, operando2)
    print("Resultado ", resultado) 