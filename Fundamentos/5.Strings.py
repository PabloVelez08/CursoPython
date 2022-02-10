#String -> str
#Es un dato indexable
#String es un tipo de dato inmutable
#Inmutable quiere decir que no acepta la reasignacion

#Asignacion de una unica linea
x = 'Hola'
y = ' con todos'

#String de varias lineas
texto = '''LibroQuijote
Cervantes
En un pueblo de la mancha .....
Ahi esta mi molino
'''

print(texto)

texto2 = '''
Primera \t linea
Segunda \n linea
Tercera
'''
#print(texto2)

#Operaciones
cadena1 = 'Python'
cadena2 = 'es un lenguaje de programación'
print(type(cadena2))

numero1 = 8.5
print(type(numero1))
print(cadena1, cadena2, ' interpretado', numero1)

# Concatenación de String: es uni dos variables de tipo String en una sola impresion
print(cadena1 + cadena2 + 'y ademas tengo este numero' + str(numero1))

cadena3 = cadena1 + cadena2
print(cadena3)

#Clases
#atributos
#metodos - > funciones
# Las instancias tienen los metodos

#Formated Strings 
nombre = 'Pablo'
edad = 21
ira = 32.5
universidad = 'EPN'
#1. Basado en variables
print(f'1: Hola mi nombre es {nombre} y mi edad es {edad} y tengo un ira de {ira}')
#2. Llama al metodo de la clase String
print('2: Hola mi nombre es {} y mi edad es {} y tengo un ira de {}'.format(nombre, edad, ira))
#3. LLamada al metodo format pero indicando la posicion
print('3: Hola mi nombre es {0} y mi edad es {1} y tengo un ira de {2}'.format(nombre,edad,ira))
# Con repeticion
print('Mi nombre es {0} estudio en la {1} y ademas trabajo en {1}'.format(nombre, universidad))
#4. Formato String con reasignacion de variables
print('4: Hola mi nombre es {variableNombre} y mi edad es {variableEdad} y tengo un ira de {variableIRA}'.format(variableNombre='Alexander', variableEdad=edad, variableIRA=ira))
# Objeto -> str 
# Atributos -> privados

#2. Indexacion
# 'Python'
#  |0|1|2|3|4|5|
cadenaTexto = 'Este es un curso de programacion muy buen curso'
print(cadenaTexto[0])
print(cadenaTexto[2])
#Range -> rango
#print(len('Hola'))
print(len(cadenaTexto))
print(cadenaTexto[0]) #E
print(cadenaTexto[31]) # n
#print(cadenaTexto[32]) # n, error
#print(cadenaTexto[33]) # error
# Cuando yo utilizo los numero negativos, empiezo a contar de atras hacia adelante
#Cuando empiezas desde atras hacia adelante se empieza desde el -1
print(cadenaTexto[-1]) #n
print(cadenaTexto[-2]) #o
print(cadenaTexto[-32]) #E
# Error -> print(cadenaTexto[-33])
print(cadenaTexto[1]+cadenaTexto[8]+cadenaTexto[13])


# Error -> cadenaTexto[0] = 'A'
#Recordemos que el String es inmutable

letra = cadenaTexto[0]
print(letra)
letra = 'A'
print(letra)

# Indexacion en rangos (subStrings)
# [valorIncluido, valorExcluido
# [0,2)
print(cadenaTexto[0:2])
print(cadenaTexto[0:10])
print(cadenaTexto[2:20])
print(cadenaTexto[2:20:3]) #agregar salto
# Indice hasta el final
print(cadenaTexto[2:])
# desde el comienzo hasta el indice
print(cadenaTexto[:3]) #Est
# Necesito todo el contenido
print(cadenaTexto[:])
print(cadenaTexto[::])

# Ejercicio: Invierta toda la varibale cadenaTexto
print(cadenaTexto[::-1])
cadenaInvertida = cadenaTexto[::-1]
print(cadenaInvertida)

# Funciones en python
print(cadenaTexto.upper())
print(cadenaTexto.lower())
print(cadenaTexto.capitalize())
#Encontrar algo en tu cadena de texto
# en caso de encontrar se devuelve el indice de la primera coincidencia
print(cadenaTexto.find('curso'))
print('Animales: tigre'.find('tigre'))
#Si el substring que busco no existe python me devuelve -1
print('Animales: tigre'.find('perro'))
cadenaTexto2 = 'Los niños uegan en el parque'
# Validar si empiezo con...
print(cadenaTexto2.startswith('Los'))
print(cadenaTexto2.startswith('Las'))
#Validar si termina con ...
print(cadenaTexto2.endswith('parque'))
print(cadenaTexto2.endswith('cine'))




