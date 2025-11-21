import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy  # Asegúrate de que Enemy esté correctamente importado

TITLE = "Space War"
FPS = 60
ENEMY_SPAWN_INTERVAL = 2000  # Intervalo de aparición de enemigos (en milisegundos)

pygame.init()
pygame.mixer.init()

# Listas de enemigos y balas
enemies = []
bullets = []
last_spawn_time = pygame.time.get_ticks()

# Inicializar pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Sonidos
try:
    laser_sound = pygame.mixer.Sound("assets/sounds/lazer-gun-432285.wav")
    explosion_sound = pygame.mixer.Sound("assets/sounds/explosion-under-snow-sfx-230505.wav")
except FileNotFoundError as e:
    print(f"Warning: Sound file not found: {e}")
    laser_sound = None
    explosion_sound = None

# Música de fondo
try:
    pygame.mixer.music.load("assets/sounds/game-music-loop-7-145285.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except FileNotFoundError as e:
    print(f"Warning: Music file not found: {e}")

# Reloj para FPS
clock = pygame.time.Clock()

# Jugador
player = Player(shoot_sound=laser_sound)

# Variable para controlar el ciclo del juego
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        player.handle_movement(event)  # Maneja el movimiento del jugador
        
        # Disparo del jugador
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()  # Llamada a la función de disparo del jugador
            bullet = Bullet()  # Crear una nueva bala
            
            # Calcular la posición inicial de la bala
            bullet_x = player.x + player.size // 2 - bullet.image.get_width() // 2
            bullet_y = player.y - bullet.image.get_height()
            
            # Disparar la bala
            bullet.shoot(bullet_x, bullet_y)
            bullets.append(bullet)  # Añadir la bala a la lista de balas

    current_time = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
    if current_time - last_spawn_time > ENEMY_SPAWN_INTERVAL:
        # Crear un nuevo enemigo
        new_enemy = Enemy()
        enemies.append(new_enemy)  # Añadir el nuevo enemigo a la lista
        last_spawn_time = current_time  # Actualizar el tiempo del último spawn

    # Actualizar la posición de los enemigos
    for enemy in enemies:
        enemy.update()

    # Actualizar el jugador
    player.update()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar todos los enemigos
    for enemy in enemies:
        enemy.draw(screen)

    # Actualizar y dibujar todas las balas
    for bullet in bullets[:]:
        bullet.update(SCREEN_HEIGHT)  # Actualizar la posición de la bala
        if not bullet.visible:  # Si la bala ya no es visible, eliminarla
            bullets.remove(bullet)
            continue
        bullet.draw(screen)  # Dibujar la bala

    # Dibujar al jugador
    player.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el FPS
    clock.tick(FPS)

# Finalizar juego
print("Saliendo del juego...")
pygame.quit()
sys.exit()
