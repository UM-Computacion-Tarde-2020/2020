def mes_a_letras(numero):
    #defino primero una funcion que tomara valores entre 1-12 defino la lista y enumero los elementos que necesito

    meses_del_año = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    #busco la posicion del numero dentro de la lista
    nombre_mes = meses_del_año[numero - 1]
    #desvolver el resultado
    return nombre_mes
