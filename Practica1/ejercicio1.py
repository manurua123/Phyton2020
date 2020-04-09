frase = "si trabajmos mucho con computadora, eventualmente encontraras que te gustaria automatizar altguna tarea. Por ejemplo, porias desear reliazar una busqueda y remplazo en una gran numero de archivos de texto, o renombrrar y reoganizar un monton de arhvos con fotos de una manera compleja. tal vez quieras escribir alguna pequeña base de datos perzonalizada, o una aplicacion especializada con interfaza grafica, o un juego siemple."
frase_mod = frase.split (" ")
cant = 0
for n in frase_mod:
    print(n)
    cant = cant + 1
print("-------------------------------------")
print ("la cantidad de palabras es: " + format(cant))
print("--------------------------------------")
frase_2 = ""
for n in frase_mod:
    print(n.upper())
    frase_2 = frase_2 + " " + n.upper()
print (frase_2.strip())
