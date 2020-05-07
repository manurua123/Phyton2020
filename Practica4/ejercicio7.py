
import PySimpleGUI as sg
import random
def abrir_archivo(archivo_leer):
    archivo = open(archivo_leer,'r')
    valores = archivo.read(-1)
    archivo.close()
    return valores

def dibujar (arch_colores,arc_cordenadas,grafico):
    colores = abrir_archivo(arch_colores).split()
    cordenadas = abrir_archivo(arc_cordenadas).split()
    for i,j in zip(colores,cordenadas):
        cord = eval(j)
        print(cord)
        point = graph.draw_point(cord ,10 , color=i)
        print( i,j )


layout = [
          [sg.Text('Colores'), sg.Input(key='arch_color'), sg.FileBrowse()],
          [sg.Text('Cordenadas'), sg.Input(key='arc_cordenada'), sg.FileBrowse()],
          [sg.Button('Dibujar'),sg.Button('SALIR')],
          [sg.Graph(canvas_size=(100, 100),graph_bottom_left=(0, 0), graph_top_right=(100, 100),background_color='#FFFFFF', enable_events=True, key = 'grafico')],
         ]

window = sg.Window('Ejercicio 7 Practica 4', layout, text_justification='center')
graph = window['grafico']
while True:     # Event Loop
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event == 'Dibujar':
        dibujar(value['arch_color'],value['arc_cordenada'],graph)



window.close()
