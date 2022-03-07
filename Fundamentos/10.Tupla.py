# Tupla -> tuple
# Inutable

tupla1 = (3,4,5,6,6)
print(tupla1)
print(type(tupla1))

#Accediendo a los elementos de la tupla
print(tupla1[0])

#Tupka con diferentes tipos de datos
tupla2 = (True,25,'Hola')
print(tupla2)

#Averiguar si un elemento se encuentr o no en una lista
print(False in tupla2)
print('python' in tupla2)
print(25 in tupla2)
print(100 not in tupla2)

# Metodos de la tupla
print(tupla1.index(3))
# print(tupla1.index(100)) en caso de no estar incluid devuleve un error
print('Tamaño de una tupla', len(tupla1))
print('¿cuantos numero 6 estan en la tupla 1?', tupla1.count(6))

#Descomprecion
dimensiones = (500,600)
dimensionX, dimensionY = dimensiones
print(dimensionX)
print(dimensionY)