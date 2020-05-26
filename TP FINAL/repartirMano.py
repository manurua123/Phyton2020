import random
import string
import pattern.es
from pattern.es import parse


letras_puntos={'a':1,'b':3,'c':2,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':6,'k':8,'l':1,'m':3,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':8,'x':8,'y':4,'z':10}
letras_cantidad={'a':11,'b':3,'c':4,'d':4,'e':11,'f':2,'g':2,'h':2,'i':6,'j':2,'k':1,'l':4,'m':3,'n':5,'o':8,'p':2,'q':1,'r':4,'s':7,'t':4,'u':6,'v':2,'w':2,'x':1,'y':1,'z':1}

def palabrasEnJuego():
    '''
    arma una lista con las palabras de mas de dos letras y menos de 7 que proporciona pattern.es
    '''
    palabras = list(pattern.es.spelling.keys())
    palabrasOK= []
    for i in palabras:
        if(len(i)<7)&(len(i)>2):
             palabrasOK.append(i)
    return palabrasOK

palabras_validas = palabrasEnJuego()

def repartirMano(bolsa_letras,fichas_jugador = 0):
    ''' recibe como parametro la cantidad de fichas que hay en la bolsa y la cantidad de fichas que faltan en la mano del jugador
    y retorna la cantidad de fichas que falten para llegar a 7 y elimina esas fichas de la bolsa de fichas.
    '''
    mano = []
    while (len(mano)<7-fichas_jugador):
        letra = random.choice(string.ascii_letters).lower()
        if(bolsa_letras[letra] > 0):
            mano.append(letra)
            bolsa_letras[letra] = bolsa_letras[letra] -1
    return mano

def generaPalabra(mano,tipoPalabra):
    '''
    genera una palabra al azar dentro del diccionario de palabras que generamos (2<caracteres<7), crea una lista con las letras que la forman,
    tranforma esa esa lista en un conjunto y toma los elementos que comparte este conjunto con las letras de la mano, si todos las letras de la palbra random estan
    en la mano y la palabra es del tipo indicado devuelve la palabra encontrada
    '''
    palabra = ''
    letras = set(mano)
    while(parse(palabra,tokenize = True,tags = True,chunks = False).replace(palabra,'') != tipoPalabra):
        palabraRandom = list(random.choice(palabras_validas))
        print("".join(palabraRandom)) #eso es para ver que este funcionando
        res = list(set(palabraRandom) & letras)
        if (len(res) == len(palabraRandom)):
            palabra = "".join(palabraRandom)
    return palabra

mano = repartirMano(letras_cantidad)
print('MANO: ',mano)
palabra = generaPalabra(mano,'/NN')
print('MANO: ', mano, "Palabra encotrada: ", palabra)
