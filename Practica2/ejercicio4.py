import random
preguntas = [('Buenos Aires limita con Santiago del Estero' ,'no'), ('Jujuy limita con Bolivia', 'si'), ('San Juan limita con Misiones', 'no'),('Nequen esta en la Patagonia' ,'si')]
print ('Responda a las siguientes afirmaciones con SI (verdadero) o NO (falso)')
print('')
puntos = 0
rango= len(preguntas)
while rango>0:
    i= random.randrange(rango)
    print (preguntas[i][0])
    respuesta = input().lower()
    if (respuesta == preguntas[i][1]):
        print ('CORRECTO')
        puntos+=1
    else:
        print('INCORRECTO')
    preguntas.pop(i)
    rango= rango -1
print('Puntaje: ', puntos)
