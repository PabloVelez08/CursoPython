from googletrans import Translator
import pyttsx3

motorVoz = pyttsx3.init()
traductor = Translator()
motorVoz.setProperty('rate',120)

try:
    with open('Proyectos/Traductor/libro.txt', mode='r') as miArchivo:
        # Realizar traduccion
        texto = miArchivo.read()
        textoTraducido = traductor.translate(text=texto).text
        # Escribir la traduccion en un txt
        txtSalida = open('Proyectos/Traductor/libroTraducido.txt', 'w')
        txtSalida.write(textoTraducido)
        # Lee el audiolibro
        motorVoz.say('Audiolibro traducido de 100 años de soledad')
        motorVoz.say(textoTraducido)
        motorVoz.runAndWait()
except FileNotFoundError as error:
    print('Error: ', error)

