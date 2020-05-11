import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json



def guardar(ruta,entrada):
	base_datos=[]
	archivo=open(ruta,'r')
	dato=archivo.read()
	archivo.close()
	if (len(dato) == 0):
		print('entre por es vacio ',len(base_datos))
		dato=base_datos
		archivo=open(ruta,'w')
		json.dump(dato,archivo)
		archivo.close()

	archivo=open(ruta,'r')
	base_datos=json.load(archivo)
	archivo.close()
	base_datos.append(entrada)
	archivo=open(ruta,'w')
	json.dump(base_datos,archivo)
	archivo.close()



def elegir_juego(eleccion):
    if eleccion == 'Ahorcado':
        hangman.main()
    elif eleccion == 'Ta-Te-Ti':
        tictactoeModificado.main()
    elif eleccion == 'Otello':
        reversegam.main()

def ventana_error():
    layout = [[sg.Text('Falta nombre del jugador o juego que desea iniciar',**textos)],[sg.OK(**botones),]]
    window = sg.Window('ERROR', layout,background_color='#222831')
    event, values = window.read()
    window.close()

juegos= ['Ahorcado','Ta-Te-Ti','Otello']
botones = {'button_color':('#222831','#f4a548'),'size':(7,1)}
textos ={'background_color':'#222831', 'text_color':'#f0f0f0','justification':'centre'}
input = {'background_color':'#222831','size' :(20,10),'text_color':'#f0f0f0'}
columna1= [
    [sg.Text('Nombre',**textos,),sg.Input(key='nombre_jugador',**input)]
    ]
columna2=[
    [sg.Text('Juego',**textos),sg.InputCombo(juegos,key = 'juego_selec',**input)],
    ]
layout = [
    [sg.Column(columna1,background_color='#222831'), sg.Column(columna2,background_color='#222831')],
    [sg.Button('Jugar',**botones),sg.Button('Salir',**botones,)],
    ]

window = sg.Window('Fernández | Rúa', layout,background_color='#222831')
while True:
    event, value = window.read()
    if event is None or event == 'Salir':
        break
    if event == 'Jugar':
        if(value['nombre_jugador'] != '')&(value['juego_selec'] != ''):
            valor_a_guardar = {'Nombre': value['nombre_jugador'],'Juego': value['juego_selec']}
            guardar('jugadores.txt',valor_a_guardar)
            elegir_juego(value['juego_selec'])
        else:
            ventana_error()
window.close()

##muestra los elementos guardados en el archivo json
