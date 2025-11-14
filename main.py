import pygame
import sys
from game.bullet import Bullet
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Space War"
FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
bullet = Bullet()
bullets=[]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.shoot(400, 300)
        screen.fill (0, 0, 0)
    for bullet in bullets:
        bullet.update(SCREEN_HEIGHT)
        bullet.draw(screen)
    bullet.draw(screen)    
    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()

