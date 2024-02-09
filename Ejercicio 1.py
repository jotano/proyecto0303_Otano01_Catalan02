#Importar módulos
import pygame 
from random import randint

#Inicializar Pygame
pygame.init()

#Configuramos la ventana del juego
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Ejemplo 4")

#Agregamos la imagen de la pelota y obtenemos su rectángulo
ball = pygame.image.load("perro.png")
ballrect = ball.get_rect()

# Establece imagen de fondo
fondo = pygame.image.load("fondo(Sanche).webp")
ventana.blit(fondo, (0,0))

# Transforma el tamaño del objeto ball
ball = pygame.transform.scale(ball, (140, 200))

#Se establece la velocidad de la pelota 
speed = [randint(4,4),randint(4,4)]

#Se mueve la pelota a la posición inicial
ballrect.move_ip(0,0)

#Agregamos la imagen de la barra y obtenemos su rectángulo
barra = pygame.image.load("barra(perro).png")
barrarect = barra.get_rect()

#Mevemos la barra a la posición inicial
barrarect.move_ip(240,450)

# Transforma el tamaño del objeto bate
barra = pygame.transform.scale(barra, (100, 80))

#Configuramos la fuente para mostrar el texto
fuente = pygame.font.Font(None, 36)

#Inicializamos la bandera del bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3,0)

    #Detección de colisiones entre la pelota y la barra 
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    #Mover la pelota y manejar colisiones con los bordes de la ventana
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0: 
        speed[1] = -speed[1]

    #Verificamos si la pelota golpea la parte inerior de la pelota 
    if ballrect.bottom > ventana.get_height():
        #Se muestra el text de "Game Over"
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        #Si el juego se sigue ejecutando se dibuja el fondo, la pelota y la barra 
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(barra, barrarect)
    
    #Se actualiza la pantalla 
    pygame.display.flip()
    pygame.time.Clock().tick(60)
#Se finaliza Pygame al salirse del bucle del juego 
pygame.quit()


