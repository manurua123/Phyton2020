import json
from pattern.es import conjugate
from pattern.es import INFINITIVE, PRESENT, PAST, SG, SUBJUNCTIVE, PERFECTIVE
from pattern.es import parse
import PySimpleGUI as sg


def buscar_verbos(archivo_inicial, acrhivo_final):
    archivo = open(archivo_inicial,'r')
    frase= archivo.read(-1).lower().split()
    archivo.close()
    lista_verbos =[]
    for palabra in frase:
        datos = parse(palabra,tokenize = True,tags = True,chunks = False).replace(palabra,'')
        if(datos == '/VB'):
            print (conjugate(palabra,INFINITIVE))
            lista_verbos.append(conjugate(palabra,INFINITIVE))
    archivo = open('verbos.json','w')
    json.dump(contar_elem_lista(lista_verbos) ,archivo)
    archivo.close()

def contar_elem_lista(lista):
    return{i:lista.count(i) for i in lista}

def ventana_error():
    layout = [[sg.Text('falta declara 1 o \nmas archivos',background_color= '#d8c593',text_color='#222831')],
              [sg.OK(button_color=('#222831','#bb3b0e'),size=(10,1))]
              ]
    window = sg.Window('ERROR', layout,background_color='#d8c593',size =(130,100))
    event, values = window.read()
    window.close()

textos = {'size': (8,1),'background_color':'#d8c593','text_color':'#222831'}
botones ={'size': (8,1),'button_color':('#222831','#dd7631')}
input ={'background_color':'#f6d743'}
layout = [
    [sg.Text('ORIGEN',**textos),sg.InputText ('', key = 'origen',**input),sg.Button('Buscar', key='Buscar Origien',**botones)],
    [sg.Text('DESTINO',**textos),sg.InputText ('', key = 'destino',**input), sg.Button('Buscar',key = 'Buscar Destino',**botones)],
    [sg.Button('GO',size= (10,1),button_color=('#222831','#dd7631')),sg.Button('SALIR',button_color=('#222831','#bb3b0e'),size=(10,1))],
]

window = sg.Window('Ejercicio6',layout=layout,background_color='#d8c593',size =(500,100))

while True:
    event, value = window.read()
    if event is None or event == 'SALIR':
        break
    archivo_origen = value['origen']
    archivo_destino = value['destino']
    if event == 'Buscar Origien':
        archivo_origen = sg.popup_get_file('file to open', no_window=True)
        print(archivo_origen )
    if event == 'Buscar Destino':
        archivo_destino = sg.popup_get_file('file to open', no_window=True)
        print(archivo_destino)
    if (event == 'GO'):
        if(archivo_origen != '')&(archivo_destino != ''):
            buscar_verbos(archivo_origen,archivo_destino)
        else:
            ventana_error()
window.close()




    #texto = "Mirenme, soy feliz entre las hojas que cantan Cuando atraviesa el jardin el viento en monopatin Cuando voy a dormir cierro los ojos y sueno Con el olor de un pais florecido para mi"
    #print(texto)
    #cargartexto('ejercicio6.txt',texto)
    #buscar_verbos('ejercicio6.txt','verbos.json')
