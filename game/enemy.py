import pygame
import random


img_enemigo = pygame.image.load("enemigo.png")


enemigo_X = random.randint(0, 733)
enemigo_y = random.randint(50, 200)
enemigo_X_cambio = 0.3
enemigo_y_cambio = 50

def enemigo(x, y):
    pygame.display.get_surface().blit(img_enemigo, (x, y))


def actualizar_enemigo():
    global enemigo_X, enemigo_y, enemigo_X_cambio, enemigo_y_cambio
    enemigo_X += enemigo_X_cambio

  
    if enemigo_X <= 0:
        enemigo_X_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_X >= 736:
        enemigo_X_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    return enemigo_X, enemigo_y
