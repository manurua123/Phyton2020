import json
import PySimpleGUI as sg

def abrir_archivo(archivo_leer):
    archivo = open(archivo_leer,'r')
    valores = archivo.read(-1)
    archivo.close()
    return valores

def guardar_valores(dato,destino):
    archivo = open(destino,'w')
    json.dump(dato,archivo)
    archivo.close()

colores = abrir_archivo('colores.txt').split()
columna1 = [
    [sg.Text('COLOR',justification='center', size=(10, 1), )],
    [sg.InputCombo(colores, size = (12,10), key = 'color_selec')],
    [sg.Graph(canvas_size=(100, 100),graph_bottom_left=(0, 0), graph_top_right=(100, 100),background_color='#FFFFFF', enable_events=True, key = 'grafico')],

    ]
columna2 = [
    [sg.Text('CORDENADAS',justification='center', size=(15, 1))],
    [sg.Text('X'), sg.Slider(range = (0, 100),orientation = 'h', size = (10,20), default_value = 0, key = 'cord_x'),],
    [sg.Text('Y'), sg.Slider(range = (0, 100),orientation = 'h', size = (10, 20), default_value = 0, key = 'cord_y'),]
    ]
layout = [
    [sg.Column(columna1), sg.Column(columna2)],
    [sg.Listbox('',size =(35,12),key='listbox')],
    [sg.Button('Agregar'), sg.Button('Guardar'),sg.Button('SALIR')],]


window = sg.Window('Ejercicio 9 Practica 4', layout)
graph = window['grafico']
lista = []
while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event == 'Agregar':
        print(value['color_selec'])
        cord = (value['cord_x'],value['cord_y'])
        point = graph.draw_point(cord,3, color= value['color_selec'])
        datos={'cordenada' : cord,'color': value['color_selec']}
        lista.append(datos)
        window.FindElement('listbox').Update(lista);
    if event == 'Guardar':
        archivo_destino = sg.popup_get_file('abrir archivo', no_window=True)
        guardar_valores(lista, archivo_destino)
window.close()
