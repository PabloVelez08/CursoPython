import math
import pygame
from pygame import mixer
from Personajes.Personajes import Fantasma, Monstruo
from Personajes.Posicion import Posicion


dimensionesPantalla = (600,500)
colorFondo = (4,9,76)
posicionesIniciales = {
    'monstruo' : Posicion((150,10)),
    'fantasma' : Posicion((100,50))
}
fondo = pygame.image.load('Proyectos/pygame/assets/img/background.jpg')
# Inicializacion de una instancia pygame
pygame.init()

puntos = 0
# Fuentes
fuente1 = pygame.font.Font('freesansbold.ttf',20)
fuente2 = pygame.font.SysFont('Segoe UI.ttf',18)

# Sonido
mixer.music.load('Proyectos/pygame/assets/audio.wav')
mixer.music.play(-1)

def mostrar_textos():
    texto1 = fuente1.render('Puntos: '+str(puntos), True, (255,255,255))
    texto2 = fuente1.render('Python Club de software EPN', True, (255,255,255))
    texto3 = fuente1.render('Pablo Vélez', True, (255,255,255))
    screen.blit(texto1,(25,440))
    screen.blit(texto2,(280,430))
    screen.blit(texto3,(280,455))

# Configuraciones del juego
pygame.display.set_caption('Monstruos')

# Creando una pantalla de juego
screen = pygame.display.set_mode(dimensionesPantalla)

# Bucle principal del juego
finalizado = False

# Inicializacion personajes
fantasma = Fantasma(posicionesIniciales['fantasma'], screen)
monstruo = Monstruo(posicionesIniciales['monstruo'], screen)

moverIzquierda = False
moverDerecha = False
moverArriba = False
moverAbajo = False

while not finalizado:
    # Escenografia básica
    screen.fill(colorFondo)  
    screen.blit(fondo,(0,0))

    # Eventos (gestor de evento de pygame)
    for event in pygame.event.get():
        # Evento cerrar una ventana
        if event.type == pygame.QUIT:
            finalizado = True
        
        # Eventos del teclado
        # Con tecla presionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moverIzquierda = True
            if event.key == pygame.K_RIGHT:
                moverDerecha = True
            if event.key == pygame.K_UP:
                moverArriba = True
            if event.key == pygame.K_DOWN:
                moverAbajo = True
        # Con tecla levantada
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moverIzquierda = False
            if event.key == pygame.K_RIGHT:
                moverDerecha = False
            if event.key == pygame.K_UP:
                moverArriba = False
            if event.key == pygame.K_DOWN:
                moverAbajo = False

    # Efectuar movimiento
    if moverIzquierda:
        fantasma.posicion.setX(fantasma.posicion.obtenerCoordenadas()[0]-1)
    elif moverDerecha:
        fantasma.posicion.setX(fantasma.posicion.obtenerCoordenadas()[0]+1)
    elif moverArriba:
        fantasma.posicion.setY(fantasma.posicion.obtenerCoordenadas()[1]-1)
    elif moverAbajo:
        fantasma.posicion.setY(fantasma.posicion.obtenerCoordenadas()[1]+1)

    coordenadasPersonaje = fantasma.posicion.obtenerCoordenadas()

    # Control de bordes
    if coordenadasPersonaje[0] < 0:
        fantasma.posicion.setX(0)
    elif coordenadasPersonaje[0] > 500:
        fantasma.posicion.setX(500)

    if coordenadasPersonaje[1] < 0:
        fantasma.posicion.setY(0)
    elif coordenadasPersonaje[1] > 320:
        fantasma.posicion.setY(320)

    d = math.sqrt((monstruo.posicion.obtenerCoordenadas()[0] - fantasma.posicion.obtenerCoordenadas()[0])**2+(monstruo.posicion.obtenerCoordenadas()[1] - fantasma.posicion.obtenerCoordenadas()[1])**2)

    print('Distancia: ', d)
    if d < 30:
        puntos += 1
        grito = mixer.Sound('Proyectos/pygame/assets/grito.wav')
        grito.play()
    # Render elementos
    # Elementos dinamicos
    fantasma.dibujar()
    monstruo.dibujar()

    # Actualizar la pantalla
    mostrar_textos()
    pygame.display.update()