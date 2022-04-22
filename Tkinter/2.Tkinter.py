import tkinter as tk
from tkinter import GROOVE, SUNKEN
from turtle import color

colorVerde = '#25AD1E'
colorAzul ='#231E96'
colorNegro = '#000000'
colorBlanco = '#FFFFFF'
fuenteTitulos = ('Courie',14,'bold')
fuenteGeneral = ('Courie',11,'normal')

class Ventana:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Ejemplo 2')
        self.root.resizable(True, True)
        self.root.geometry('600x500')
        self.root.configure(bg=colorVerde)

    def guardarInfromacion(self, nombre: str, apellido: str, edad: int):
        print(f'Informacion {nombre} {apellido} {edad}')

    def saludar(self,texto):
        print('Dices', texto)

    def dibujar(self):
        # Agregar widgets
        # Primer widgets, Label
        # metodos place es relativo al padre
        titulo = tk.Label(self.root,text='Formulario', bg=colorVerde, font=fuenteTitulos)
        titulo.place(x=200,y=20)

        texto1 = tk.Label(self.root, text='Ingresa los datos a continuacion', bg=colorVerde, font=fuenteGeneral, 
                    fg=colorAzul)
        texto1.place(x=20,y=50)

        lblNombre = tk.Label(self.root, text='Nombre:', bg=colorVerde, font=fuenteGeneral)
        lblNombre.place(x=20,y=110)

        lblApellido = tk.Label(self.root, text='Apellido:', bg=colorVerde, font=fuenteGeneral)
        lblApellido.place(x=20,y=150)

        lblEdad = tk.Label(self.root, text='Edad:', bg=colorVerde, font=fuenteGeneral)
        lblEdad.place(x=20,y=190)

        # Input
        inputNombre = tk.Entry(self.root, width=20)
        inputNombre.place(x=100,y=110)

        inputApellido = tk.Entry(self.root)
        inputApellido.place(x=100,y=150)

        inputEdad = tk.Entry(self.root)
        inputEdad.place(x=100,y=190)
        # Combobox

        def guardarInformacion2():
            print(f'Información {inputNombre.get()} {inputApellido.get()} {inputEdad.get()}')

        # Boton
        # width de los botones es un numero de cara
        btnGuardar = tk.Button(self.root, text='Guargar\nInformacion', font=fuenteGeneral,
                    command=guardarInformacion2, width=15, height=2, bd=2,
                    bg=colorNegro, fg=colorBlanco, highlightbackground=colorVerde,
                    relief=SUNKEN)
        btnGuardar.place(x=250,y=300)
        

        #Main loop
        self.root.mainloop()

ventana = Ventana()
ventana.dibujar()

