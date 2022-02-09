#String -> str
#Es un dato indexable
#String es un tipo de dato inmutable
#Asignaciones de una unica linea
from cgitb import text


x = 'Hola'
y = ' con todos'

#String de varias lineas
texto = '''LibroQuijote
Cervantes
En un pueblo de la mancha .....
Ahi esta mi molino
'''

print(texto)

text2 = '''
Primera \t linea
Segunda \n linea
Tercera
'''
#print(texto2)

#Operaciones
cadena1 = 'Python'
cadena2 = 'es un lenguaje de programación'

numero1 = 8.5
print(type(numero1))
print(cadena1, ' - ', cadena2, ' interpretado', numero1)

# Concatenación de String: es uni dos variables de tipo String en una sola impresion
print(cadena1 + cadena2 + 'y ademas tengo este numero' + str(numero1))

