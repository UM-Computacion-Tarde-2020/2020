def mes_a_letras(mes):
    lista = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    numero = int(input("Ingrese el numero: "))
    if(numero <= 12):
        return(lista[numero - 1])
        print(mes)
    else:
        print("Error")


def mes_a_letras_reves(mes_reves):
    lista_reves = ["Diciembre", "Noviembre", "Octubre", "Septiembre", "Agosto",
                   "Julio", "Junio", "Mayo", "Abril", "Marzo", "Febrero",
                   "Enero"]
    numero_reves = int(input("Ingrese el numero: "))
    if(numero_reves <= 12):
        return(lista_reves[12 - numero_reves])
        print(mes_reves)
    else:
        print("Error")
