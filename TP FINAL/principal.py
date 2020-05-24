import configuracion
import PySimpleGUI as sg
layout = [
    [sg.Text('ScrabbleAR')],
    [sg.Button('Jugar',)],
    [sg.Button('Configurar')],
    [sg.Button('Salir')]
]

window = sg.Window('', layout)
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
