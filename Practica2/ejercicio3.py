original = ['Auto', '123', 'Viaje', '50', '120']
lista_int = []
lista_string = []
for i in original:
    if i.isdecimal():
        lista_int.append(i)
    else:
        lista_string.append(i)
print('Lista original:' , original)
print('Lista enteros:' , lista_int)
print('Lista palabras:' , lista_string)
