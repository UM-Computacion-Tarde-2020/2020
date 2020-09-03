def mes_a_letras(a):
    a= int(input("Ingrese un numero del 1 al 12:"))
    meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 
        'Agosto', 'Septiembre', 'Octumbre', 'Noviembre', 'Diciembre'] 
    nombre_mes=(meses[a-1])
    return nombre_mes
