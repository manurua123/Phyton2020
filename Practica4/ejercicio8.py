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

def guardar_archivo(archivo_guardar,valor):
    archivo = open(archivo_guardar,'w')
    archivo.write(valor)
    archivo.close()

def guardar_valores(arch_colores,arc_cordenadas,destino):
    colores = abrir_archivo(arch_colores).split()
    cordenadas = abrir_archivo(arc_cordenadas).split()
    texto = ''
    for i,j in zip(colores,cordenadas):
        texto = texto + ' {} {} \n'.format(j,i)
    guardar_archivo(destino,texto)

layout = [
          [sg.Text('Colores'), sg.Input(key='arch_color'), sg.FileBrowse()],
          [sg.Text('Cordenadas'), sg.Input(key='arc_cordenada'), sg.FileBrowse()],
          [sg.Button('Dibujar'), sg.Button('Guardar'),sg.Button('SALIR')],
          [sg.Graph(canvas_size=(100, 100),graph_bottom_left=(0, 0), graph_top_right=(100, 100),background_color='#FFFFFF', enable_events=True, key = 'grafico')],
         ]

window = sg.Window('Ejercicio 8 Paractica 4', layout, text_justification='center')
graph = window['grafico']
while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    if event == 'Dibujar':
        dibujar(value['arch_color'],value['arc_cordenada'],graph)
    if event == 'Guardar':
        archivo_destino = sg.popup_get_file('abrir archivo', no_window=True)
        guardar_valores(value['arch_color'],value['arc_cordenada'],archivo_destino)

window.close()
