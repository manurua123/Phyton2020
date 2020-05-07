import PySimpleGUI as sg
import time
import json
textos = {'background_color': '#222831', 'font' : ('Arial',12),'justification':'center',}
botones = {'button_color':('#222831','#f0f0f0'),'size':(8,1)}
    #configuracion de la ventana
layout = [
    [sg.Text('Humedad', **textos),sg.InputText ('',key ='humedad'),],
    [sg.Text('Temperatura',**textos),sg.InputText ('', key = 'temperatura') ],

    [sg.Button('Añadir',**botones),sg.Button('Exportar',**botones)],
    [sg.Listbox('',size =(150,12),key='listbox')],
    [sg.Button('SALIR',button_color=('#222831','#f2a365'),size=(8,1))],
]
datos={}
lista=[]
window = sg.Window('Ejercicio4',layout=layout,background_color='#222831',size =(300,350))
while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event in 'Añadir':
        datos={'dia' : time.strftime("%d/%m/%y"),'hora': time.strftime("%H:%M"),'T°' :value['temperatura'],'H':value['humedad']}
        lista.append(datos)
        window.FindElement('listbox').Update(lista);
    if event in 'Exportar':
        archivo = open('ejercicio4.json','w')
        json.dump(lista,archivo)
        archivo.close()
window.Close()
