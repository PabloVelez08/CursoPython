#Funcion entrada y funcion de salida
#Va a buscar las palabras reservadas

#Argumento a la funcion, '' -> string
from cgi import print_environ


print('Formulario')
print('Nombre: ', end='')
#Input -> entrada datos
nombre = input()
print('Apellido: ', end='')
apellido = input()
print('Edad: ', end='')
edad = input()

print('El nombre ingresdo es: ',nombre)
print('El apellido ingresdo es: ',apellido)
print('El edad ingresdo es: ',edad)

#Python es un lenguaje 100% orientado a objetos
