import PySimpleGUI as sg
import time
import json
textos = {'background_color': '#202040', 'font' : ('Arial',12),'justification':'center'}

layout = [
    [sg.Text('Humedad', **textos),sg.InputText ('',key ='humedad'),],
    [sg.Text('Temperatura',**textos),sg.InputText ('', key = 'temperatura') ],

    [sg.Button('Añadir',button_color=('black','#ffbd69')),sg.Button('Exportar',button_color=('black','#ffbd69')),sg.Button('SALIR',button_color=('black','#ff6363'))],
    [sg.Listbox('',size =(200,30),key='listbox')],
]
datos={}
lista=[]
window = sg.Window('Ejercicio4',layout=layout,background_color='#202040',size =(300,350))
while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event in 'Añadir':
        datos={
        'dia' : time.strftime("%d/%m/%y"),
        'hora': time.strftime("%H:%M"),
        'T°' :value['temperatura'],
        'H':value['humedad']
        }
        lista.append(datos)
        window.FindElement('listbox').Update(lista);
    if event in 'Exportar':
        archivo = open('ejercicio4.txt','w')
        json.dump(lista,archivo)
        archivo.close()
window.Close()
