
import pygame
from main import* 
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 30 
bullet_y_mov = 1 
bullet_visible = False

def shoot(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 8, y + 8))

if bullet_visible:
    shoot(jugador_x, bullet_y)
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_SPACE:
            shoot(jugador_x, bullet_y)
            bullet_y -= bullet_y_mov