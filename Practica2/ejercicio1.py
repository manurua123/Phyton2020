tam = ['im1 4,14','im2 33,15','im3 6,34','im4 410,134']
print (tam)
print('ingrese un numero entero')
numero = int(input())
lista_a=[]
lista_b=[]
for i in tam:
    parte=i.partition(' ')
    a=parte[0]
    b=parte[2].partition(',')
    b1=int(b[0])
    b2=int(b[2])
    if b1 <= numero:
        lista_a.append(a)
        lista_a.append((b1,b2))
    else:
        lista_b.append(a)
        lista_b.append((b1,b2))

print('LISTA 1= ' , lista_a)
print('LISTA 1= ' , lista_b)
