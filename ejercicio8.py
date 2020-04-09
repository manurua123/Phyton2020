def primo(numero):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

palabra=input("Introduce una cadena: ")
lista={}
for letra in palabra:
    if letra in lista:
        lista[letra]=lista[letra]+1
    else:
        lista[letra]=1
for i in lista:
    print('La letra',i,'aparece:',lista[i],'veces')
    if (primo(lista[i])==True):
        print('es primo')
    else:
        print('no es primo')
