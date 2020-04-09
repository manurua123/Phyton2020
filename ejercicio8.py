def primo(numero):
    if numero < 1:
        return False
    elif numero== 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

palabra=str(input("Introduce una cadena: ")).lower()
lista={}
for letra in palabra:
    if letra in lista:
        lista[letra]=lista[letra]+1
    else:
        lista[letra]=1
for i in lista:
    print('La letra',i,'aparece:',lista[i],'veces')
    if (primo(lista[i])==True):
        print('aparece un numero primo de veces')
    else:
        print('no aparece un numero primo de veces')
