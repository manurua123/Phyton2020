import PySimpleGUI as sg

import string
import random



b2 = [[0 for j in range(10)] for i in range(10)] #Grid de 10x10

b1 = [[0 for j in range(5)] for i in range(5)]  #Fila con las 5 letras random

def button2(x, y):               # define cell as instance of button and
    b2[x][y] = buttonA(x,y)           # bulid Button
    return b2[x][y].button


def button1(x,y):
    b1[x][y] = buttonB(x,y)
    return b1[x][y].button



#BotonB para la fila de botones con letras

class buttonB():
    def __init__ (self,x,y):
        self.name       = random.choice(string.ascii_letters)
        self.x          = x
        self.y          = y
        self.state      = 1
        self.disabled   = False
        self.key        = (x,y)
        self.button     = sg.Button(self.name,auto_size_button=False,
                        border_width=2,
                        disabled=self.disabled,
                        focus=False,key=self.key,
                        pad=(1,1))


    def update(self):
        self.button.update(disabled=self.disabled)

    def getLetra(self):
        return self.name

    def enable(self):
        self.disabled = False
        self.update()

    def disable(self):
        self.disabled = True
        self.update()





#BotonA es para el cuadro de 10x10

class buttonA():
    def __init__ (self,x,y):
        self.name       = " "
        self.x          = x
        self.y          = y
        self.state      = 0   #Vamos a hacer que State sea si ya tiene valor o no, 0 es no tiene y 1 ya tiene
        self.disabled   = False
        self.key        = (x,y)
        self.button     = sg.Button(self.name,auto_size_button=False,
                        border_width=2,
                        disabled=self.disabled,
                        focus=False,key=self.key,
                        pad=(1,1))


    def update(self):
        self.button.update(self.name,disabled=self.disabled)

    def setLetra(self,name):
        self.name = name
        self.disabled = True
        self.state = 1
        self.update()

    def disable(self):
        self.disabled = True
        self.update()

    def enable(self):
        self.disabled = False
        self.update()



ven = [[sg.Text("TablaB ")],
       [button1(z,1)for z in range(5)],
       [sg.Text("Tabla A")]]+[
       [button2(x, y) for x in range(10)] for y in range(10)]


win = sg.Window("Ej_1",layout=ven,finalize=True)

"""
Enable/disable de A y B los uso justamente por lo que hablo mas abajo, para controlar que no se me rompa el programa
haciendo click 2 veces en la misma tabla


en el enable_A tengo un if donde pregunto sobre el estado de dicho boton, esto lo hago para no volver a activar un boton que ya tenia
un valor ya que no quiero que se escriba de nuevo
"""


def disable_A():
    for i in range(10):
        for j in range(10):
            b2[i][j].disable()


def enable_A():

    for i in range(10):
        for j in range(10):
            if (b2[i][j].state == 0):
                b2[i][j].enable()


def enable_B():
    for i in range(5):
        b1[i][1].enable()

def disable_B():
    for i in range(5):
        b1[i][1].disable()

ok = True


"""
Dada la forma en la que implemente el Ej tengo que usar el booleano Ok para
Asegurarme de que no se haga click 2 veces en B (porque asigna un valor donde no debe)
o que se haga click en A antes que en B que da error

"""

while True:
    event , values = win.read()   #El values lo deje para que solo para que en event este la tupla de coordenadas (x , y)
    if (event == None):             #Pero esta al pedo... no tiene uso
        break

    disable_A()
    # print("A-")
    if (ok):
        x , y = event
        letra = b1[x][y].getLetra()
        ok = False
        enable_A()
        disable_B()
        # print("B-")
    else:
        x , y = event
        b2[x][y].setLetra(letra)
        ok = True
        enable_B()
