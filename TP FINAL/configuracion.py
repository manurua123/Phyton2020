import random
import PySimpleGUI as sg


letras_puntos={'a':1,'b':3,'c':2,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':6,'k':8,'l':1,'m':3,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':8,'x':8,'y':4,'z':10}
letras_cantidad={'a':11,'b':3,'c':4,'d':4,'e':11,'f':2,'g':2,'h':2,'i':6,'j':2,'k':1,'l':4,'m':3,'n':5,'o':8,'p':2,'q':1,'r':4,'s':7,'t':4,'u':6,'v':2,'w':2,'x':1,'y':1,'z':1}

def nivel_facil(letrasPuntos,letrasCantidad):
    for i in letrasPuntos.keys():
        letrasPuntos[i] = letrasPuntos[i] *3
        letrasCantidad[i] = letrasCantidad[i]*3
    tipoPalabra = ['/NM','/VB','/JJ']
    return {'PuntajeLetra':letrasPuntos,'CantidadLetras':letrasCantidad,'TipoPalabre':tipoPalabra}

def nivel_medio(letrasPuntos,letrasCantidad):
    for i in letrasPuntos.keys():
        letrasPuntos[i] = letrasPuntos[i] *2
        letrasCantidad[i] = letrasCantidad[i]*2
    tipoPalabra = ['/NM','/VB']
    return {'PuntajeLetra':letrasPuntos,'CantidadLetras':letrasCantidad,'TipoPalabre':tipoPalabra}

def nivel_dificil(letrasPuntos,letrasCantidad):
    for i in letrasPuntos.keys():
        letrasPuntos[i] = letrasPuntos[i] *2
        letrasCantidad[i] = letrasCantidad[i]*2
    tipos= ['/NM','/VB','/JJ']
    tipoPalabra=list(random.choice(tipos))
    return {'PuntajeLetra':letrasPuntos,'CantidadLetras':letrasCantidad,'TipoPalabre':tipoPalabra}

layout = [
    [sg.Text('Duracion del turno'), sg.Slider(range = (10, 120),orientation = 'h', size = (10,20), default_value = 60, key = 'tiempo',tooltip='Duracion de cad turno. 60seg por defecto')],
    [sg.Text('Nivel de dificultad'),
    sg.Button('Facil',tooltip='Fichas: Muchas\nPuntos: Muchos\nCategorias: Sustantivos | Adjetivos | Verbos'),
    sg.Button('Medio',tooltip='Fichas: Algunas\nPuntos: Normal\nCategorias: Sustantivos | Adjetivos '),
    sg.Button('Dificil',tooltip='Fichas: Pocas\nPuntos: Pocos\nCategorias:Aleatoria')],
    [sg.Button('Confirmar',disabled=True),sg.Button('Cancelar')],
]
def main():
    window = sg.Window('', layout)
    while True:
        event, value = window.read()
        if event is None or event == 'Cancelar':
            listaConfiguracion = nivel_medio(letras_puntos,letras_cantidad)
            listaConfiguracion['Tiempo'] = 60
            break
        if event == 'Facil':
            listaConfiguracion = nivel_facil(letras_puntos,letras_cantidad)
            window['Facil'].update(disabled=True)
            window['Medio'].update(disabled=False)
            window['Dificil'].update(disabled=False)
            window['Confirmar'].update(disabled=False)
        if event == 'Medio':
            listaConfiguracion = nivel_medio(letras_puntos,letras_cantidad)
            window['Facil'].update(disabled=False)
            window['Medio'].update(disabled=True)
            window['Dificil'].update(disabled=False)
            window['Confirmar'].update(disabled=False)
        if event == 'Dificil':
            listaConfiguracion = nivel_dificil(letras_puntos,letras_cantidad)
            window['Facil'].update(disabled=False)
            window['Medio'].update(disabled=False)
            window['Dificil'].update(disabled=True)
            window['Confirmar'].update(disabled=False)
        if event == 'Confirmar':
            listaConfiguracion['Tiempo'] = value['tiempo']
            break
    window.close()
    return listaConfiguracion

if __name__ == '__main__':
    main()
