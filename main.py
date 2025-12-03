import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, game_running, game_over
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy 
from game.score import Score
from game.healthbar import Health_Bar


TITLE = "Space War"
FPS = 60
ENEMY_SPAWN_INTERVAL = 2000

pygame.init()
pygame.mixer.init()
GAME_OVER_FONT = pygame.font.Font(None, 74)
RESTART_FONT = pygame.font.Font(None, 36)
game_state = game_running
enemies = []
bullets = []
last_spawn_time = pygame.time.get_ticks()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
score = Score(screen)
health_bar = Health_Bar(screen)

player = Player(y=SCREEN_HEIGHT - 60, shoot_sound=None, health_bar=health_bar) 
try:
    laser_sound = pygame.mixer.Sound("assets/sounds/lazer-gun-432285.wav")
    explosion_sound = pygame.mixer.Sound("assets/sounds/explosion-under-snow-sfx-230505.wav")
except FileNotFoundError as e:
    print(f"Warning: Sound file not found: {e}")
    laser_sound = None
    explosion_sound = None

try:
    pygame.mixer.music.load("assets/sounds/game-music-loop-7-145285.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except FileNotFoundError as e:
    print(f"Warning: Music file not found: {e}")

clock = pygame.time.Clock()

player.shoot_sound = laser_sound 

def draw_game_over_screen():
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.set_alpha(150)  
    s.fill((0,0,0))     
    screen.blit(s, (0,0))
    game_over_text = GAME_OVER_FONT.render("GAME OVER", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(game_over_text, text_rect)
    restart_text = RESTART_FONT.render("Presiona R para Reiniciar", True, (0, 255, 0))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(restart_text, restart_rect)
    
def reset_game():
    global enemies, bullets, last_spawn_time, game_state
    
    enemies.clear()
    bullets.clear()
    last_spawn_time = pygame.time.get_ticks()
    
    player.reset_position() 
    health_bar.reset_health()
    score.reset_score()
    game_state = game_running 

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == game_running: 
            player.handle_movement(event)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()
                bullet = Bullet()
                
                bullet_x = player.x + player.size // 2 - bullet.image.get_width() // 2
                bullet_y = player.y - bullet.image.get_height()
                
                bullet.shoot(bullet_x, bullet_y)
                bullets.append(bullet)

        elif game_state == game_over: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
    
    if game_state == game_running: 
        current_time = pygame.time.get_ticks()
        
        if current_time - last_spawn_time > ENEMY_SPAWN_INTERVAL:
            new_enemy = Enemy()
            enemies.append(new_enemy)
            last_spawn_time = current_time

        for enemy in enemies:
            enemy.update()
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)

        player.update()

    screen.fill((0, 0, 0)) 

    
    if game_state == game_running:
        for enemy in enemies:
            enemy.draw(screen)
            player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            
            
            if player_rect.colliderect(enemy_rect):
                health_bar.lose_health()
                enemies.remove(enemy)
                
                if explosion_sound:
                    explosion_sound.play()

                
                if not health_bar.is_alive():
                    print("Game Over!")
                    game_state = game_over 
                break

        
        for bullet in bullets[:]:
            bullet.update(SCREEN_HEIGHT)
            if not bullet.visible:
                bullets.remove(bullet)
                continue
            bullet.draw(screen)

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                
                bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                
                if bullet_rect.colliderect(enemy_rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)

                    if explosion_sound:
                        explosion_sound.play()
                    score.add()
                    break

        player.draw(screen)
    
    
    score.draw()
    health_bar.draw()
    
    if game_state == game_over: 
        draw_game_over_screen()
        
    pygame.display.flip()

    clock.tick(FPS) 

print("Saliendo del juego...")
pygame.quit()
sys.exit()