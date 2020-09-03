def mes_a_letras(mes):
    # defino una lista con los meses del año en letras
    meses = ['Diciembre', 'Noviembre', 'Octubre', 'Setiembre', 'Agosto',
             'Julio', 'Junio', 'Mayo', 'Abril', 'Marzo', 'Febrero', 'Enero']
    # busco la posición del número dentro de la lista
    nombre_mes = meses[12-mes]
    # devuelvo el valor encontrado
    return nombre_mes
