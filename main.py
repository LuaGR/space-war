import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy

TITLE = "Space War"
FPS = 60
enemy_spawn_interval = 2000

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
bullet = Bullet()
bullets=[]

running = True

player = Player()

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
        player.handle_movement(event)

    player.update()
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()
