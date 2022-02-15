# Listas list()
# Inicializcion []
# Listas no tienen un espacio definido

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(lista1))

# Lista conbinadas
lista2 = ['a','b','c',23,14,True,35.75]
print(lista2)

# Metodos y las operaciones de las listas

# Indexacion
# averiguar largo o numero de elemento que tiene una lista
print(len(lista2))
# Accediendo a los elementos de la lista
print(lista2[0])
print(lista2[6])

#Cambiar los valores de la lista
lista2[5] = False
print(lista2)

#Indexacion entre intervalos
print(lista2[1:3])
print(lista2[::-1])

# Lista alumnos
listaAlumnos = ['Anderson','Pablo','Kevin','Juan','Mario']
#Obtener una nueva lista con las dos ultimas personas
listaAlumnos2 = listaAlumnos[1:]
print(listaAlumnos2)
print(type(listaAlumnos2))

#agregar datos al final de una lista
listaAlumnos2.append('Fernanda')
print(listaAlumnos2)

#agrega datos en una posicion en especifico
#indicamos el indice en el que vamos a insertar y el valor
listaAlumnos2.insert(3, 'Bryan')
print(listaAlumnos2)

#como agregar al final otr lista
listaAlumnos2.extend(['Pablo','Jose'])
print(listaAlumnos2)

#Retirar elementos
#pop recibe el indice que quiero retirar
#pero si no le paso el indice retirara el ultimo elemento
listaAlumnos2.pop()
print(listaAlumnos2)

#remover con un indice en especifico
listaAlumnos2.pop(1)
print(listaAlumnos2)

#retiramos un valor en especifico de la lista
listaAlumnos2.remove('Mario')
print(listaAlumnos2)

#¿Que pasa si hay dos elementos con el mismo nombre?
listaAlumnos2.extend(['Alejandro','Alejandro'])
print(listaAlumnos2)
listaAlumnos2.remove('Alejandro')
print(listaAlumnos2)

#Operador
print('Pablo' in listaAlumnos2)
print('Andres' in listaAlumnos2)

# Hacer una copia
copiaListaAlumnos = listaAlumnos2[::]
print(copiaListaAlumnos)
copiaListaAlumnos2 = listaAlumnos2.copy()
print(copiaListaAlumnos2)

# Invertir la copia
print(copiaListaAlumnos[::-1])
copiaListaAlumnos2.reverse()
print(copiaListaAlumnos2)

# Encontrar indice de un elemento
print(copiaListaAlumnos)
print(copiaListaAlumnos2.index('Bryan'))

#¿Que pasaria si solicito un indice de un elemento que no se encuentra en la lista
#print(copiaListaAlumnos2.index(58))
#Producira un error si el elemento no se encuentra enlistado

# Ordenar
copiaListaAlumnos.sort()
print(copiaListaAlumnos)

lista4 = [85,47,68,25]
lista4.sort(reverse=True)
print(lista4)

# Ordenar una lista condiferentes tipos de datos no es posible
#lista5 = ['A',58,68]
#lista5.sort()
#print(lista5)

# Pueden convertir un string a lista
cadenaTexto = 'Las universidades piensan en retornar a la presencialidad universidades'
listaTexto = list(cadenaTexto)
#print(listaTexto)

# Separar en palabras
listaPalabra = cadenaTexto.split(' ')
print(listaPalabra)

#contar el numero de veces que una palabra esta en la lista
print(listaPalabra.count('universidades'))

#join
saludo = 'Saludo: '
oracion = saludo.join([' buenos dias', 'buenas tardes'])
print(oracion)

lista5 = ['Hola']
lista6 = ['como estas?']
print(type(lista6))
lista5.extend(lista6)
temp = lista5.copy()
print(lista5)
print(temp)

#Declarar una lista vacia
lista7 = []


# Eliminar todos los elementos de la lista
temp.clear()
print(temp)

# Unpacking, desempaquetado de una lista
print(listaAlumnos)
nombre1, nombre2 = listaAlumnos[0:2]
print(nombre1)
print(nombre2)

nombre1, nombre2, *nombres, nombre3 = listaAlumnos
print(nombre1)
print(nombre2)
print(nombres)
print(nombre3)

# Lista de listas
matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]
print(matriz)
print(matriz[2][2])


