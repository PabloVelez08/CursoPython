# Iteraciones
#for es una instruccion que permite recorrer un iterable

listaFrutas = ['Pera','Manzana','Banano']

for fruta in listaFrutas:
    print(fruta)

# Utilizar tangos numericos
for item in range(0,5):
    print('Elemento {}'.format(item))

matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]

for fila in matriz:
    for columna in matriz:
        print(fila)
        print(columna)

# Anidados basados en indices
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        #print(matriz[fila][column])
        print('valor de la posicion i:{} - j:{} es:{}'.format(i,j,matriz[i][j]))
        if matriz[i][j] == 2:
            matriz[i][j] = 10

print(matriz)

# While

