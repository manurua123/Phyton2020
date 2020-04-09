imagenes = ['img1', 'img2', 'img3']
lista_cord= []
lista = []
for i in imagenes:
    print('Ingrese cordenadas x e y para el elmento',i)
    x=int(input("Cordenada X:"))
    y=int(input('Cordenada Y:'))
    for j in lista_cord:
        while(x == j[0]) and (y== j[1]):
            print('ERROR: cordenadas ya utilizadas')
            x=int(input("Ingrese otra cordenada X:"))
            y=int(input("ingrese otra cordenada y:"))
    lista_cord.append([x,y])
    lista.append([i,(x,y)])
print('')
for i in lista:
    print(i[0], ': ', i[1])
