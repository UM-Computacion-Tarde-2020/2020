def mes_a_letras(mes):        #las funciones comienzan con "def". Además, "mes" es el parámetro de la función
    #defino una lista con los meses del año en letras
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo','Junio','Julio'
             'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] 
    #busco la posicion del  numero dentro de la lista
    nombre_mes = meses[mes -1] #resto 1 porque comienza a contar desde 0. El mes Enero es el mes 0, y Febrero sería el mes 2
    #devuelvo el valor encontrado
    return nombre_mes #se escribe return para que la función devuleva un valor
