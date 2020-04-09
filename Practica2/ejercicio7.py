print('ingrese una palabra')
palabra = str(input()).lower()
revez = palabra[::-1]
print('palabra:', palabra)
print('palabra al revez:',revez)
if(palabra == revez):
    print(palabra, 'es palindomo')
else:
    print(palabra,'no es palindomo')
