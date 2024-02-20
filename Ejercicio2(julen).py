import pygame
from random import randint

pygame.init()
ventana = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("ejercicio 3")

MAX_SPEED = 10.985

# Crea el objeto pelota
ball = pygame.image.load("perro.png")

# Establece imagen de fondo
fondo = pygame.image.load("fondo(Sanche).Webp")
ventana.blit(fondo, (0, 0))

# Transforma el tamaño del objeto ball
ball = pygame.transform.scale(ball, (140, 200))

# Inicializo los valores con los que se van a mover la pelota
speedball = [5, 5]

# Pongo la pelota en el origen de coordenadas
ballrect = ball.get_rect()

# Lugar de inicio de la bola
ballrect.move_ip(0, 0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("barra(perro).png")

# Transforma el tamaño del objeto bate
bate = pygame.transform.scale(bate, (100, 80))

# Transforma el tamaño de la imagen de fondo
fondo = pygame.transform.scale(fondo, (1080, 720))

baterect = bate.get_rect()
print(baterect)
# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(440, 650)

# Crea el objeto ladrillo
ladrillo = pygame.image.load("ladrillo.jpg")
ladrillo = pygame.transform.scale(ladrillo, (100, 40))

# Definir la clase para los ladrillos
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ladrillo
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Crear una lista de ladrillos
ladrillos = [Ladrillo(x * 120, y * 50) for x in range(9) for y in range(2)]

game_over_image = pygame.image.load("gameover(julen).webp")

# Configuramos la fuente para mostrar el texto
fuente = pygame.font.Font("PIXEL8bit.ttf", 80)

# Variables para el contador de golpes y la velocidad de la pelota
contador_golpes = 0

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla, y establece la velocidad del bate
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-10, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(10, 0)

 # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speedball[1] = -speedball[1]
       
        speedball[0] *= 1.3
        speedball[1] *= 1.3

    # Limita la velocidad máxima
        speedball[0] = min(speedball[0], MAX_SPEED)
        speedball[1] = min(speedball[1], MAX_SPEED)

        contador_golpes += 1

        if contador_golpes % 4 == 0:
        # Restablece la velocidad de la pelota
            speedball[0] /= 2.197
            speedball[1] /= 2.197
        # Cada cuarto golpe, restablece la velocidad original

    # Comprobar colisiones con los ladrillos
    for ladrillo in ladrillos:
        if ballrect.colliderect(ladrillo.rect):
            speedball[1] = -speedball[1]
            ladrillos.remove(ladrillo)


    # Muevo la pelota
    ballrect = ballrect.move(speedball)

    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

        if ballrect.bottom >= ventana.get_height():
            # Se muestra la imagen de "Game Over y establece su posicion"
            ventana.blit(game_over_image, ((ventana.get_width() - game_over_image.get_width()) / 2,
                                           (ventana.get_height() - game_over_image.get_height()) / 2))

            pygame.display.flip()
            pygame.time.delay(2000)  # Delay for 2 seconds before closing the game
            jugando = False

    # Establece colision del bate con las paredes de la ventana
    if baterect.left < 0:
        baterect = baterect.move(10, 0)
    if baterect.right > ventana.get_width():
        baterect = baterect.move(-10, 0)

    # Establece el fondo como una imagen, fill evita trazado de la bola
    ventana.fill((0, 0, 0))
    ventana.blit(fondo, (0, 0))

    # Dibujar los ladrillos
    for ladrillo in ladrillos:
        ventana.blit(ladrillo.image, ladrillo.rect)  

    # Dibujo la pelota
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
