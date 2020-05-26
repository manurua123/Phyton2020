
import PySimpleGUI as sg
import random
import string
import time

listaPorDefecto={'PuntajeLetra':{'a':1,'b':3,'c':2,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':6,'k':8,'l':1,'m':3,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':8,'x':8,'y':4,'z':10},'CantidadLetras':{'a':11,'b':3,'c':4,'d':4,'e':11,'f':2,'g':2,'h':2,'i':6,'j':2,'k':1,'l':4,'m':3,'n':5,'o':8,'p':2,'q':1,'r':4,'s':7,'t':4,'u':6,'v':2,'w':2,'x':1,'y':1,'z':1},'TipoPalabre':['/NM','/VB','/JJ'],'Tiempo': 60}

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
def asignarLetras (mano):
    for i in range(7):
        if(atrilLetras[i][1].getLetra() == ' '):
            atrilLetras[i][1].setLetra(random.choice(mano))
class BotonLetra():
    def __init__ (self,x,y):
        self.name      = ' '
        self.x          = x
        self.y          = y
        self.state      = 1
        self.disabled   = True
        self.key        = (x)
        self.button     = sg.Button(self.name,size= (4,2))
        self.tipo       = 0
    def update(self):
        self.button.update(self.name)
    def getLetra(self):
        return self.name
    def setLetra(self,valor):
        self.name = valor
        self.disabled = False
        self.state = 1
        self.update()
    def enable(self):
        self.disabled = False
        self.update()
    def disable(self):
        self.disabled = True
        self.update()
class BotonAtril(BotonLetra):
    def __init__ (self,x,y):
        BotonLetra.__init__ (self,x,y)
class BotonTablero(BotonLetra):
    def __init__ (self,x,y):
        BotonLetra.__init__ (self,x,y)
    def tipoCelda(self,valor):
        if(valor == 0):
            self.tipo=valor
            self.name='X'
            self.button.update(self.name,button_color=('black','gold'))
        if (valor ==1):
            self.tipo=valor
            self.name='Pala\nx2'
            self.button.update(self.name,button_color=('black','orange'))
        if(valor== 2):
            self.tipo=valor
            self.name='Letra\nx2'
            self.button.update(self.name,button_color=('black','green'))
        if(valor== 3):
            self.tipo=valor
            self.name='Pala\n x3'
            self.button.update(self.name,button_color=('black','red'))
        else:
            None

atrilLetras = [[' ' for j in range(5)] for i in range(7)]
def botonesLetras(x,y):
    atrilLetras[x][y] = BotonLetra(x,y)
    return atrilLetras[x][y].button
matizTablero = [[0 for j in range(15)] for i in range(15)]
def botonTablero(x,y):
    matizTablero[x][y] = BotonTablero(x,y)
    return matizTablero[x][y].button

def asignarPuntajesTablero():
    for i in range(15):
        for j in range(15):
            if(i+j==14)|(i==j):
                matizTablero[i][j].tipoCelda(2)
            if(((i==0) &((j+1)%4==0))|((j==0) &((i+1)%4==0))|((i==14) &((j+1)%4==0))|((j==14) &((i+1)%4==0))|(((i+1)%4==0)&((j+1)%4==0))):
                matizTablero[i][j].tipoCelda(1)
            if(((i==0) &((j+1)%8==0))|((j==0) &((i+1)%8==0))|((i==14) &((j+1)%8==0))|((j==14) &((i+1)%8==0))|(((i+1)%8==0)&((j+1)%8==0))):
                matizTablero[i][j].tipoCelda(3)
            if(i==7)&(j==7):
                matizTablero[i][j].tipoCelda(0)
def bloquearTablero():
    for i in range(15):
        for j in range(15):
            matizTablero[i][j].disable()
def desbloquerTablero():
    for i in range(15):
        for j in range(15):
            if(matizTablero[i][j].State == 0):
                matizTablero[i][j].enable()

tablero=[[botonTablero(x,y) for x in range(15)] for y in range(15)]
columna1 = [
    [sg.Text('MANO')],
    [botonesLetras(z,1)for z in range(7)]
    ]
columna2 = [ #puntos, tiempo y pasar
[sg.Text('PUNTOS',justification='center')],
[sg.Text('PC:'),sg.Text('---',key = 'puntosPc')],
[sg.Text('PJ:'),sg.Text('---',key = 'puntosPj')],
[sg.Text('TIEMPO:'),sg.Text('---',key= 'medidorTiempo')],

]
layout = [
    [sg.Column(tablero), sg.Column(columna2)],
    [sg.Column(columna1),sg.Button('CAMBIAR',),sg.Button('PASAR',)],
    [sg.Button('COMENZAR',auto_size_button=False),sg.Button('Salir',auto_size_button=False)]
]


def main(listaConfiguracion=listaPorDefecto):
    ok = True
    window = sg.Window('', layout)
    while True:
        event , values = window.read()
        if event is None or event == 'Salir':
            break
        bloquearTablero()
        if event is 'COMENZAR':
            window['COMENZAR'].update(disabled=True)
            mano = repartirMano(listaConfiguracion['CantidadLetras'])
            asignarLetras(mano)
            asignarPuntajesTablero()

    window.close()

if __name__ == '__main__':
    main()
