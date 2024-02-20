import pygame
from random import randint

pygame.init()
<<<<<<< HEAD
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("ejercicio 3")

# Crea el objeto pelota
ball = pygame.image.load("perro.png")
=======

#Configuramos la ventana del juego
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Ejemplo 4")

#Agregamos la imagen de la pelota y obtenemos su rectángulo
ball = pygame.image.load("perro.png")
ballrect = ball.get_rect()
>>>>>>> 1cc3b4f8b0a9f47ee7f1cc52a2cd98de271597ac

# Establece imagen de fondo
fondo = pygame.image.load("fondo(Sanche).webp")
ventana.blit(fondo, (0,0))

# Transforma el tamaño del objeto ball
<<<<<<< HEAD
ball = pygame.transform.scale(ball, (140, 120))

# Inicializo los valores con los que se van a mover la pelota
speedball = [5,5]

# Pongo la pelota en el origen de coordenadas
ballrect = ball.get_rect()

# Lugar de inicio de la bola
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("barra(perro).png")

# Transforma el tamaño del objeto bate
bate = pygame.transform.scale(bate, (100, 80))

# Transforma el tamaño de la imagen de fondo
fondo = pygame.transform.scale(fondo, (1080, 720))

baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(440,650)

game_over_image = pygame.image.load("gameover(julen).webp")

#Configuramos la fuente para mostrar el texto
fuente = pygame.font.Font("PIXEL8bit.ttf", 80)

=======
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
>>>>>>> 1cc3b4f8b0a9f47ee7f1cc52a2cd98de271597ac
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
<<<<<<< HEAD

    # Compruebo si se ha pulsado alguna tecla, y establece la velocidad del bate
=======
    
>>>>>>> 1cc3b4f8b0a9f47ee7f1cc52a2cd98de271597ac
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-10,0)
    if keys[pygame.K_RIGHT]:
<<<<<<< HEAD
        baterect = baterect.move(10,0)

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speedball[1] = -speedball[1]
    
    # Muevo la pelota
    ballrect = ballrect.move(speedball)
    
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]
        
        if ballrect.bottom >= ventana.get_height():
        #Se muestra la imagen de "Game Over y establece su posicion"
            ventana.blit(game_over_image, ((ventana.get_width() - game_over_image.get_width()) / 2,
                                            (ventana.get_height() - game_over_image.get_height()) / 2))

            pygame.display.flip()
            pygame.time.delay(2000)  # Delay for 2 seconds before closing the game
            jugando = False

    # Establece colision del bate con las paredes de la ventana
    if baterect.left < 0:
       baterect = baterect.move(10,0)
    if baterect.right > ventana.get_width():
        baterect = baterect.move(-10,0)
    
    #establece el fondo como una imagen, fill evita trazado de la bola
    ventana.fill((0, 0, 0))
    ventana.blit(fondo, (0,0))


    # Dibujo la pelota
    ventana.blit(ball, ballrect)
    
    # Dibujo el bate
    ventana.blit(bate, baterect)
    
=======
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
>>>>>>> 1cc3b4f8b0a9f47ee7f1cc52a2cd98de271597ac
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()