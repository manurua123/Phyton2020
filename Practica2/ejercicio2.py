tam = ['im1 4,14','im2 33,15','im3 6,34','im4 410,134']
print ('tam= ' , tam)
lista_a=[]
for i in tam:
    parte=i.partition(' ')
    a=parte[2].partition(',')
    a1=int(a[0])
    a2=int(a[2])
    lista_a.append((a1,a2))
lista_b=sorted(lista_a)
print('LISTA= ' , lista_a)
print('LISTA ORDENADA= ' , lista_b)
