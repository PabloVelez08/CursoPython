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

#Primer reto curso
ciudad = input('Ingresa tu ciudad: ')

print('El nombre ingresdo es: ',nombre)
print('El apellido ingresdo es: ',apellido)
print('El edad ingresdo es: ',edad)
print('El ciudad ingresdo es: ',ciudad)


#Python es un lenguaje 100% orientado a objetos