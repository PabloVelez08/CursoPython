# Tres en raya
# Reglas clasicas del tres en linea
# Si tres caracteres son iguales en cualquier sentido se termina el juego
# Van a existir dos jugadores
# Presentacion
# Se pueden asignar nombre a los dos jugadores
# Matriz creada a partir de listas
# Se soliitara que se ingrese la fila y la colmna en la que el jugador quiere marcar su movimiento
# Debera comprobar si se encuentra ocupado perdera el turno
# Se terminara el juego
# Se presentara un menu al inicio en el que se pueda ingresar los nombres de los jugadores
#, y ademas escoger los caacteres, por defecto sera la x y el o
# Y la tercera opcion sera jugar
# Y la cuarta salir
# Ademas los resultados se guardarán en un archivo de texto con fecha y hora.
from random import randint

global nombreJugador1
nombreJugador1 = 'Jugador 1'
global nombreJugador2
nombreJugador2 = 'Jugador 2'
global piezaJugador1
piezaJugador1 = 'X' 
global piezaJugador2
piezaJugador2 = 'O' 

def crearMatriz():
    matriz = []
    nFilas = 3
    nColumnas = 3
    for i in range(nFilas):
        matriz.append(['-']*nColumnas)
    #for i in range(0,nFilas):
     #   for j in range(0,nColumnas):
      #      mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
       #     matriz[i][j] = int(input(mensaje))
    dimensiones = (nFilas, nColumnas)
    return matriz, dimensiones

def mostrarMatriz(matriz, dimensiones):
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end='\t')
        print('')

def llenarMatriz(matriz, caracter):
    fila = int(input('Fila: '))
    columna = int(input('Columna: '))
    matriz[fila-1][columna-1] = caracter

def menu():
    print('\n\tTres en raya\n')
    print('1. Nombres de los jugadores')
    print('2. Cambiar piezas')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opcion: ')
    #print('Desde adentro de la fun menu:',opcion)
    return opcion

def nombreJugadores():
    print('\n\tNombre jugadores')
    print('1. Cambiar el nombre del jugador 1')
    print('2. Cambiar el nombre del jugador 2')
    opcionNombre = input('Cambiar nombre del jugador: ')
    if opcionNombre == '1':
        global nombreJugador1
        nombreJugador1 = input('Nombre del jugador 1: ')   
    elif opcionNombre == '2':
        global nombreJugador2
        nombreJugador2 = input('Nombre del jugador 2: ')
    else:
        print('Ingrese una opcion valida')    

def cambiarPiezas():
    print('\n\tPiezas')
    print('1. Cambiar pieza del jugador 1')
    print('2. Cambiar pieza del jugador 2')
    opcionPieza = input('Cambiar nombre del jugador: ')
    global piezaJugador1
    global  piezaJugador2 
    if opcionPieza == '1':
        auxPieza1 = input('Pieza del jugador 1: ')  
        if auxPieza1 != piezaJugador2:

            piezaJugador1 = auxPieza1
        else:
            print('La pieza ingresada es igual a la del otro jugador')

    elif opcionPieza == '2':
        auxPieza2 = input('Pieza del jugador 2: ')
        if auxPieza2 != piezaJugador1:

            piezaJugador2 = auxPieza2
        else:
            print('La pieza ingresada es igual a la del otro jugador')
    else:
        print('Ingrese una opcion valida')    

def jugar(tablero, dimensiones):
    
    print('Jugando....')
    finalizado = False
    turno = randint(1,2) 
    while finalizado == False: 
        piezaActual = ''
        jugadorActual = ''
        if turno == 1:
            print('Es turno de: ', nombreJugador1)
            piezaActual = piezaJugador1
            jugadorActual = nombreJugador1
            llenarMatriz(tablero, piezaJugador1)
            turno = 2
        else:
            print('Es turno de: ', nombreJugador2)
            piezaActual = piezaJugador2
            jugadorActual = nombreJugador2
            llenarMatriz(tablero, piezaJugador2)
            turno = 1

        # valide cuando se hizo 3 en raya
        # True and False = Flase
            # Horizaontales

        if tablero[0][0] == piezaActual and tablero[0][1] == piezaActual and tablero[0][2] == piezaActual:
            finalizado = True
        if tablero[1][0] == piezaActual and tablero[1][1] == piezaActual and tablero[1][2] == piezaActual:
            finalizado = True  
        if tablero[2][0] == piezaActual and tablero[2][1] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True
            # Verticales
        if tablero[0][0] == piezaActual and tablero[1][0] == piezaActual and tablero[2][0] == piezaActual:
            finalizado = True
        if tablero[0][1] == piezaActual and tablero[1][1] == piezaActual and tablero[2][1] == piezaActual:
            finalizado = True
        if tablero[0][2] == piezaActual and tablero[1][2] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True
            # Diagonales
        if tablero[0][0] == piezaActual and tablero[1][1] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True
        if tablero[2][0] == piezaActual and tablero[1][1] == piezaActual and tablero[0][2] == piezaActual:
            finalizado = True
        
        # En caso se haya llenado el tablero
            # reto
            # if
            # for

        # Validar cuadno se sobreescrieb una posicion ocupada
        # Validar cuando todos los espacios estan llenos

        # validar cuando todos los espacios estan llenos
        mostrarMatriz(tablero, dimensiones)

    print('\tTres en raya!!!')
    print('\tEl ganador es: ', jugadorActual)


def mostrarTablero():
    pass


def main():
    terminarJuego = False
    
    while terminarJuego == False:
        opcionMenu = menu() # Va a ejecutar la funcion menu y tambine va a asignar el retorno a mi variable
        # Condicionales
        if opcionMenu == '1':
            nombreJugadores()
        elif opcionMenu == '2':
            cambiarPiezas()
        elif opcionMenu == '3':
            tablero, dimensiones = crearMatriz()
            jugar(tablero, dimensiones)
        elif opcionMenu == '4':
            print('\tGracias por jugar, te esperamos pronto')
            terminarJuego = True
        else:
            print('Por favor ingrese una opcion valida')
        

main()


