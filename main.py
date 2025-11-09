import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player

TITLE = "Space War"
FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

running = True

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_movement(event)

    player.update()
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()
