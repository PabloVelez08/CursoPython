# Una funcion generica que permita crear una matriz

def crearMatriz():
    matriz = []
    nFilas = int(input('Ingrese el numero de filas: '))
    nColumnas = int(input('Ingrese el numero de columnas: '))
    for i in range(nFilas):
        matriz.append([0]*nColumnas)
    for i in range(0,nFilas):
        for j in range(0,nColumnas):
            mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            matriz[i][j] = int(input(mensaje))
    return matriz 

# UNa funcion generica para imprimir por consola cuaquier matriz
def mostrarMatriz(matriz, shape):
    pass

def main():
    tablero = crearMatriz()
    print(tablero)


main()