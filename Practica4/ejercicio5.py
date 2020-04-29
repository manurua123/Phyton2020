import PySimpleGUI as sg
import json

def modificarArchivo(nombre,**jugada):
    #modifico o agrego al un juegador
    archivo = open('ejercicio5.json','r')
    jugadores = json.load(archivo)
    archivo.close()
    if nombre in jugadores.keys():
        jugadores[nombre] = jugada
    else:
        jugadores.setdefault(nombre,jugada)
    for i in jugadores.items():
        print(i)
    archivo = open('ejercicio5.json','w')
    json.dump(jugadores,archivo)
    archivo.close()

textos = {'background_color': '#222831', 'font' : ('Arial',12),'justification':'center',}
botones = {'button_color':('#222831','#f0f0f0'),'size':(20,2)}
    #configuracion de la ventana
layout = [
    [sg.Text('NOMBRE', **textos),sg.InputText ('',key ='nombre_jugador'),],
    [sg.Text('NIVEL',**textos),sg.InputText ('', key = 'nivel_jugador') ],
    [sg.Text('PUNTAJE',**textos),sg.InputText ('', key = 'puntaje_jugador') ],
    [sg.Text('TIEMPO',**textos),sg.InputText ('', key = 'tiempo_jugador') ],

    [sg.Button('AÑADIR/MODIFICAR',**botones),sg.Button('SALIR',button_color=('#222831','#f2a365'),size=(12,2))],
]
window = sg.Window('Ejercicio4',layout=layout,background_color='#222831',size =(300,180))
while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event in 'AÑADIR/MODIFICAR':
        jugada={'nivel': value['nivel_jugador'], 'puntaje': value['puntaje_jugador'], 'tiempo': value['tiempo_jugador'] }
        modificarArchivo(value['nombre_jugador'],**jugada)
window.Close()
