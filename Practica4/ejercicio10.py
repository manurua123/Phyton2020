
import csv
import sys
import PySimpleGUI as sg
from random import randint
import operator

def abrir_archivo(archivo_a_leer):
    with open(archivo_a_leer,'r',encoding='utf8') as archivo:
        columnas = archivo.read().splitlines()
        columnas.pop(0) #salto la primer fila porque son los titulos
    return columnas

def recorrer_archivo(columnas):
    datos = []
    for i in columnas:
        columnas = i.split(',')
        universidad = columnas[2]
        if( columnas[10] != ''): #muchas universidad no tienen alumnos mujeres
            cantidad = columnas[10].replace('"',' ') #algunos valores aparecen como "123" y tira error al intentar pasarlo a integer
            datos.append([universidad,int(cantidad)])
    return datos

def sumar_datos(datos):
    frecuencia ={}      # creo un diccionario
    for i in datos:
        if(i[0] in frecuencia):
            frecuencia[i[0]] = frecuencia[i[0]] + i[1]
        else:
            frecuencia[i[0]] = i[1]
    return frecuencia

def iniciales(cadena):
    nueva_cadena = ''.join([palabra[0] for palabra in cadena.split()])
    return (nueva_cadena.strip('d'))

def dibujar (valores,grafico):
    x= 0
    for i in valores:
        y = i[1]/125

        graph.DrawText(text=iniciales(i[0]), location=(x, y+2))
        grafico.DrawRectangle(top_left=(x,y),bottom_right=(x+1,0), fill_color = '#FF8C00')
        x=x+1.2

botones = {'button_color':('#222831','#f0f0f0'),'size':(20,2)}
layout = [
    [sg.Button('Agregar',**botones),sg.Button('Ordenar',disabled=True,**botones),sg.Button('Salir',**botones)],
    [sg.Graph(canvas_size=(1900 , 900),graph_bottom_left=(0, 0), graph_top_right=(100, 100),background_color='#FFFFFF', enable_events=True, key = 'grafico')],
    ]
window = sg.Window('Ejercicio 10 Practica 4', layout)
graph = window['grafico']

while True:
    event, value = window.read()
    if event is None or event == 'Salir':
        break
    if event == 'Agregar':
        graph.Erase()
        archivo_origen = sg.popup_get_file('abrir archivo', no_window=True)
        diccionario = sumar_datos(recorrer_archivo(abrir_archivo(archivo_origen)))
        dibujar(diccionario.items(),graph)
        window['Ordenar'].update(disabled=False)
    if event == 'Ordenar':
        graph.Erase()
        dibujar(sorted(diccionario.items(), key=operator.itemgetter(1)),graph)
window.close()
