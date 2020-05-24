import configuracion
import PySimpleGUI as sg
layout = [
    [sg.Text('ScrabbleAR',size= (20,2),font = ('Arial', 12, 'bold'),)],
    [sg.Button('Jugar',size= (20,2))],
    [sg.Button('Configurar',size= (20,2))],
    [sg.Button('Salir',size= (20,2))]
]

window = sg.Window('', layout, text_justification='center',size= (200,200),)
while True:
    event, value = window.read()
    if event is None or event == 'Salir':
        break
    if event == 'Configurar':
        listaConfiguracion= configuracion.main()
        print(listaConfiguracion)
    if event == 'Jugar':
        print('estamos en eso')
window.close()
