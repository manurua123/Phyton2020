import configuracion
import PySimpleGUI as sg
import juego
layout = [
    [sg.Text('ScrabbleAR',size= (20,2),font = ('Arial', 12, 'bold'),)],
    [sg.Button('Jugar',size= (20,2))],
    [sg.Button('Configurar',size= (20,2))],
    [sg.Button('Salir',size= (20,2))]
]
listaConfiguracion={'PuntajeLetra':{'a':1,'b':3,'c':2,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':6,'k':8,'l':1,'m':3,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':8,'x':8,'y':4,'z':10},'CantidadLetras':{'a':11,'b':3,'c':4,'d':4,'e':11,'f':2,'g':2,'h':2,'i':6,'j':2,'k':1,'l':4,'m':3,'n':5,'o':8,'p':2,'q':1,'r':4,'s':7,'t':4,'u':6,'v':2,'w':2,'x':1,'y':1,'z':1},'TipoPalabre':['/NM','/VB','/JJ'],'Tiempo': 60}

window = sg.Window('', layout, text_justification='center',size= (200,200),)
while True:
    event, value = window.read()
    if event is None or event == 'Salir':
        break
    if event == 'Configurar':
        listaConfiguracion= configuracion.main()
        print(listaConfiguracion)
    if event == 'Jugar':
        juego.main(listaConfiguracion)
window.close()
