# Tres en raya
# Reglas clasicas del tres en linea
# Si tres caracteres son iguales en cualquier sentido se termina el juego
# Gana existir dos jugadores
# Presentacion
# Se pueden asignar nombre a los dos jugadores
# Matriz creada a partir de listas
# Se soliitara que se ingrese la fila y la colmna en la que el jugador quiere marcar su movimiento
# Debera comprobar si se encuentra ocupado perdera el turno
# Se terminara el juego
# Se presentara un menu al inicio en el que se pueda ingresar los nombres de los jugadore
#, y ademas escoger los caacteres, por defecto sera la x y el o
# Y la tercera opcion sera jugar
# Y la cuarta salir

global nombreJugador1
nombreJugador1 = 'Jugador 1'
global nombreJugador2
nombreJugador2 = 'Jugador 2'
global piezaJugador1
piezaJugador1 = 'X' 
global piezaJugador2
piezaJugador2 = 'O' 



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

def jugar():
    print('Jugando....')
    print('Es turno del jugador 1: ', nombreJugador1)
    print('Es turno del jugador 2: ', nombreJugador2)
    print('Pieza 1: ', piezaJugador1)
    print('Pieza 2: ', piezaJugador2)

def mostrarTablero():
    pass


def main():
    
    opcionMenu = menu() # Va a ejecutar la funcion menu y tambine va a asignar el retorno a mi variable

    # Condicionales
    if opcionMenu == '1':
        nombreJugadores()
    elif opcionMenu == '2':
        cambiarPiezas()
    elif opcionMenu == '3':
        jugar()
    elif opcionMenu == '4':
        print('Saliendo')
    else:
        print('Por favor ingrese una opcion valida')

    jugar()

main()


