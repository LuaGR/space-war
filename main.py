import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Space War"
FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()

