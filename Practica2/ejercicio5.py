lista = []
print('Menú de opciones para la lista de números a ingresar:')
print('1: ingresar números')
print('2: ordenar números')
print('3: calcular el máximo')
print('4: calcular el mínimo')
print('5: calcular el promedio')
print('0: para terminar')
print('.........................')
respuesta = int(input())
print(' ')
while respuesta != 0:
    if (respuesta==1):
        print('Ingrese un nuevo valor a la lista')
        valor = int(input())
        lista.append(valor)
    elif (respuesta==2):
        if (len(lista) == 0):
            print('La lista esta vacia')
        else:
            print('lista original:', lista)
            lista = sorted(lista)
            print('lista ordenada:', lista)

    elif (respuesta==3):
        if (len(lista) == 0):
            print('La lista esta vacia')
        else:
            print('El maximo es: ', max(lista))

    elif (respuesta==4):
        if (len(lista) == 0):
            print('La lista esta vacia')
        else:
            print('El minimo es: ', min(lista))

    elif (respuesta==5):
        if (len(lista) == 0):
            print('La lista esta vacia')
        else:
            promedio = sum(lista)/len(lista)
            print('El promedio es: ',promedio)

    elif (respuesta==0):
        if (len(lista) == 0):
            print('La lista esta vacia')
    else:
        print('El valor no corresponde a una opcion valida. Vuelva a intentarlo')
    if(respuesta!=0):
        print(' ')
        print('.........................')
        print('1: ingresar números')
        print('2: ordenar números')
        print('3: calcular el máximo')
        print('4: calcular el mínimo')
        print('5: calcular el promedio')
        print('0: para terminar')
        print('.........................')
        respuesta = int(input())
        print(' ')
