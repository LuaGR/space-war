import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet

TITLE = "Space War"
FPS = 60

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

try:
    laser_sound = pygame.mixer.Sound("assets/sounds/lazer-gun-432285.wav")
    explosion_sound = pygame.mixer.Sound("assets/sounds/explosion-under-snow-sfx-230505.wav")
except FileNotFoundError as e:
    print(f"Warning: Sound file not found: {e}")
    laser_sound = None
    explosion_sound = None

clock = pygame.time.Clock()

running = True

player = Player(shoot_sound=laser_sound)
bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_movement(event)
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()
            bullet = Bullet()
            
            bullet_x = player.x + player.size // 2 - bullet.image.get_width() // 2
            bullet_y = player.y - bullet.image.get_height()
            bullet.shoot(bullet_x, bullet_y)
            bullets.append(bullet)

    player.update()

    screen.fill((0, 0, 0))

    for bullet in bullets[:]:
        bullet.update(SCREEN_HEIGHT)
        if not bullet.visible:
            bullets.remove(bullet)
            continue
        bullet.draw(screen)

    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()
