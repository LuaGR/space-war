# Documentación Técnica
## La Venganza de la Paloma

> **Proyecto educativo:** Space shooter arcade con temática peruana  
> **Curso:** Introducción a las TIC 
> **Fecha:** Diciembre 2025

---

## 👥 Equipo de Desarrollo

### Líder Técnico
- **Renato Lua Aguirre Gonzáles**

### Trainees
- **Sergio Ramses Contreras Bernaola**
- **Juan Rogger Chillet Uribe**
- **Diego Steeven Chavarría Quijano**

### Novato
- **Yeniffer Emily Gamboa López**

---

## 📖 Índice

1. [¿Qué es este proyecto?](#qué-es-este-proyecto)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Arquitectura del juego](#arquitectura-del-juego)
4. [Decisiones técnicas clave](#decisiones-técnicas-clave)
5. [Estructura del código](#estructura-del-código)
6. [Flujo de trabajo en equipo](#flujo-de-trabajo-en-equipo)
7. [Desafíos enfrentados](#desafíos-enfrentados)
8. [Métricas del proyecto](#métricas-del-proyecto)

---

## 🎮 ¿Qué es este proyecto?

**"La Venganza de la Paloma"** es un shooter arcade vertical desarrollado en equipo como proyecto educativo. El objetivo era aprender:

- Programación en Python desde cero
- Desarrollo de videojuegos con Pygame
- Trabajo colaborativo con Git y GitHub
- Arquitectura de software y buenas prácticas

El juego utiliza **memes y referencias peruanas** (Paloma, Alan García, Palacio de Gobierno, "Triciclo Perú") para darle una identidad cultural única.

### Características Principales
- Sistema de vidas (3 corazones)
- Dificultad dinámica que aumenta con el puntaje
- Sistema de pausa y mute
- Colisiones entre balas-enemigos y enemigos-jugador
- Reinicio del juego tras Game Over

---

## 🛠️ Tecnologías Utilizadas

### Python 3.x
**¿Por qué Python?**
- Sintaxis clara y fácil de leer
- Ideal para aprender programación desde cero
- Gran cantidad de librerías disponibles

### Pygame 2.x
**¿Por qué Pygame?**
- Librería estándar para juegos 2D en Python
- Maneja gráficos, sonidos, eventos y colisiones
- Documentación abundante en español
- No requiere conocimientos de motores complejos (Unity, Godot)

**Alternativas consideradas:**
- **Arcade**: Más moderna pero menos documentación
- **Godot**: Muy completo pero curva de aprendizaje alta

### Git y GitHub
**¿Por qué Git?**
- Permite que 5 personas trabajen sin pisarse
- Historial de cambios y control de versiones
- Pull Requests como herramienta de revisión de código

### Trello
**¿Por qué Trello?**
- Visualización clara de tareas pendientes/en progreso/terminadas
- Facilita la organización del Líder Técnico
- Cada miembro sabe qué hacer sin preguntar constantemente

---

## 🏗️ Arquitectura del Juego

### Paradigma: Programación Orientada a Objetos (POO)

El juego está construido usando **clases** que representan entidades del juego:

```python
class Player:
    # Atributos: x, y, speed, size_width, size_height, move_left, move_right, move_up, move_down
    # Métodos: handle_movement(), update(), draw(), shoot(), reset_position()

class Enemy:
    # Atributos: x, y, width, height, x_speed, y_step, speed_factor
    # Métodos: update(), draw(), reset_position()

class Bullet:
    # Atributos: x, y, speed, visible
    # Métodos: shoot(), update(), draw()

class Health_Bar:
    # Atributos: current_health, max_health, size, spacing
    # Métodos: lose_health(), is_alive(), reset_health(), draw()

class Score:
    # Atributos: score, font, text
    # Métodos: add(), reset_score(), write(), draw()
```

**Ventaja de POO:** Cada miembro del equipo puede trabajar en una clase independiente sin conflictos.

---

### El Game Loop (Corazón del Juego)

El juego funciona como un **bucle infinito** que se ejecuta 60 veces por segundo:

```python
while running:
    # 1. INPUT: Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_movement(event)
        if event.key == pygame.K_SPACE:
            player.shoot()
            bullet = Bullet()
            bullets.append(bullet)
    
    # 2. UPDATE: Update game state (if not paused)
    if not paused and not game_over:
        player.update()
        for enemy in enemies:
            enemy.update()
        for bullet in bullets:
            bullet.update(SCREEN_HEIGHT)
        # Collision detection...
    
    # 3. DRAW: Render everything
    screen.blit(background_img, (0, 0))
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    score.draw()
    health_bar.draw()
    pygame.display.flip()
    clock.tick(60)
```

**Regla de Oro:**
- En UPDATE: **NO se dibuja nada**, solo se calculan posiciones y colisiones
- En DRAW: **NO se toma ninguna decisión**, solo se dibuja lo que ya existe

---

## 🧠 Decisiones Técnicas Clave

### 1. Clases Independientes vs. Todo en un Archivo

**Decisión:** Cada entidad es un archivo separado (`player.py`, `enemy.py`, etc.)

**¿Por qué?**
- ✅ Permite trabajo en paralelo sin conflictos
- ✅ Más fácil encontrar y corregir errores
- ✅ Pull Requests más pequeños y fáciles de revisar

**Desventaja aceptada:**
- ⚠️ Más archivos para manejar (pero mejor organizados)

---

### 2. Colisiones Manuales vs. Sistema Automático de Pygame

**Decisión:** Detectamos colisiones manualmente con `rect.colliderect()`

```python
# Collision detection: bullet vs enemy
for bullet in bullets[:]:
    bullet_rect = pygame.Rect(int(bullet.x), int(bullet.y),
                              bullet.image.get_width(), bullet.image.get_height())
    for enemy in enemies[:]:
        enemy_rect = pygame.Rect(int(enemy.x), int(enemy.y),
                                enemy.width, enemy.height)
        if bullet_rect.colliderect(enemy_rect):
            bullets.remove(bullet)
            enemies.remove(enemy)
            score.add()
            break
```

**¿Por qué?**
- ✅ Control total de qué pasa cuando dos objetos chocan
- ✅ Más fácil de entender para principiantes
- ✅ No hay "magia" oculta de Pygame

**Desventaja aceptada:**
- ⚠️ Código más largo (pero más claro)

---

### 3. Dificultad Fija vs. Dificultad Dinámica

**Decisión:** La dificultad aumenta automáticamente según el puntaje

```python
# Dynamic difficulty based on score
puntos = score.score

# More points = more enemies on screen
max_enemigos = min(10, 4 + puntos // 2)

# More points = faster spawn rate
current_interval = max(600, ENEMY_SPAWN_INTERVAL - puntos * 120)

# More points = faster enemy movement
speed_factor = 1.0 + (puntos // 3) * 0.25
enemies.append(Enemy(speed_factor=speed_factor))
```

**¿Por qué?**
- ✅ El juego siempre es desafiante
- ✅ Sensación de progresión sin necesidad de niveles
- ✅ Cada partida es diferente

---

### 4. Sistema de Vidas vs. Un Solo Golpe

**Decisión:** El jugador tiene 3 vidas y reaparece en el centro al recibir daño

**¿Por qué?**
- ✅ Más permisivo para jugadores nuevos
- ✅ Feedback visual claro (corazones que desaparecen)
- ✅ Permite errores sin penalización inmediata

---

### 5. Assets Genéricos vs. Temática Peruana

**Decisión:** Usar memes peruanos (Paloma, Alan García, Palacio de Gobierno)

**¿Por qué?**
- ✅ Da personalidad única al proyecto
- ✅ Más memorable y divertido de presentar
- ✅ Fácil de reconocer en portfolios

---

## 📂 Estructura del Código

```
space-war/
│
├── main.py              # Orquestador: inicializa Pygame y ejecuta el game loop
├── constants.py         # Configuraciones globales (ancho/alto de pantalla)
├── requirements.txt     # Lista de dependencias (solo 'pygame')
│
├── game/                # Paquete con la lógica del juego
│   ├── __init__.py      # Marca 'game/' como paquete de Python
│   ├── player.py        # Clase Player (movimiento WASD + disparo)
│   ├── enemy.py         # Clase Enemy (movimiento horizontal + descenso)
│   ├── bullet.py        # Clase Bullet (movimiento vertical hacia arriba)
│   ├── score.py         # Clase Score (contador y renderizado)
│   └── healthbar.py     # Clase HealthBar (corazones visuales)
│
└── assets/              # Recursos artísticos (imágenes y sonidos)
    ├── image/
    │   ├── Paloma_meme_1.png        # Sprite del jugador
    │   ├── Alan_Garcia_muerto_meme.png  # Sprite del enemigo
    │   ├── Corazon_healt.png        # Icono de vida
    │   └── Fondo_meme_palacio_de_gobierno.png  # Fondo
    └── sounds/
        ├── Triciclo Perú.wav        # Música de fondo
        ├── lazer-gun-432285.wav     # Sonido de disparo
        ├── explosion-under-snow-sfx-230505.wav  # Explosión
        └── sound-of-collision.wav   # Sonido de puntaje
```

### Separación de Responsabilidades

| Archivo | Responsabilidad |
|---------|----------------|
| **main.py** | Game loop, crear objetos, detectar colisiones |
| **player.py** | Todo sobre el jugador (movimiento, disparo) |
| **enemy.py** | Todo sobre un enemigo (movimiento, colisiones de borde) |
| **bullet.py** | Todo sobre una bala (movimiento hacia arriba) |
| **score.py** | Mostrar y actualizar puntaje |
| **healthbar.py** | Mostrar y manejar vidas del jugador |
| **constants.py** | Variables que no cambian (tamaño de pantalla) |

---

## 🔄 Flujo de Trabajo en Equipo

### Protección de la Rama Principal

**Regla:** Nadie puede hacer `push` directo a `main`. Todo cambio pasa por **Pull Request**.

### Proceso de Desarrollo

```
1. Crear tarea en Trello
   ↓
2. Crear rama local
   git checkout -b feature/nombre-tarea
   ↓
3. Hacer cambios y commits
   git commit -m "feat: add player movement"
   ↓
4. Subir rama a GitHub
   git push origin feature/nombre-tarea
   ↓
5. Crear Pull Request
   ↓
6. Líder Técnico revisa el código
   ↓
7. Si está bien → Merge a main
   Si hay errores → Comentarios y correcciones
   ↓
8. Mover tarjeta de Trello a "Hecho"
```

### Prefijos de Commits

Para mantener un historial ordenado, usamos prefijos:

- `feat:` Nueva funcionalidad (ej. `feat: add pause system`)
- `fix:` Corrección de bug (ej. `fix: player movement out of bounds`)
- `docs:` Documentación (ej. `docs: update README with controls`)
- `refactor:` Mejora de código sin cambiar funcionalidad
- `chore:` Tareas menores (ej. `chore: update .gitignore`)

### Ventajas de Este Flujo

- ✅ La rama `main` siempre funciona
- ✅ Code reviews = mentoría del Líder Técnico
- ✅ Historial de Git es legible y útil
- ✅ Se evitan conflictos entre miembros

---

## 💪 Desafíos Enfrentados

### Desafío 1: Trabajo en Paralelo

**Problema:** 5 personas trabajando al mismo tiempo pueden sobrescribir el código de otros.

**Solución:** Git con ramas independientes. Cada miembro trabaja en su rama y el Líder Técnico integra.

---

### Desafío 2: Colisiones No Funcionaban

**Problema:** Las balas atravesaban a los enemigos sin eliminarlos.

**Solución:** Usar `pygame.Rect` para crear rectángulos invisibles alrededor de cada objeto y detectar superposición con `colliderect()`.

---

### Desafío 3: El Juego Era Demasiado Fácil

**Problema:** Después de 30 segundos, el juego se volvía monótono.

**Solución:** Implementar dificultad dinámica basada en el score (más enemigos, más rápidos, menos tiempo entre apariciones).

---

### Desafío 4: Bug de Movimiento Tras Game Over

**Problema:** Al reiniciar el juego, el jugador se movía solo porque las flags de movimiento (`move_left`, `move_right`) no se reseteaban.

**Solución:** Al reiniciar, resetear manualmente todas las flags de movimiento a `False`.

---

### Desafío 5: Niveles Mixtos de Experiencia

**Problema:** 3 Trainees con conocimientos básicos y 1 Novato aprendiendo desde cero.

**Solución:**
- Tareas diferenciadas: los Trainees programaban clases, el Novato manejaba assets
- Code reviews detallados con explicaciones
- Pair programming en momentos críticos

---

## 📊 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Líneas de código** | ~500 LOC |
| **Archivos Python** | 8 archivos |
| **Clases implementadas** | 5 clases |
| **Commits totales** | 49 |
| **Pull Requests** | 29 |
| **Duración del proyecto** | 8 semanas |
| **FPS del juego** | 60 constantes |
| **Max enemigos simultáneos** | 10 |
| **Vidas del jugador** | 3 |

---

## 🎯 Aprendizajes Clave

### Técnicos
- ✅ Programación Orientada a Objetos (clases, métodos, atributos)
- ✅ Game loops y lógica de tiempo real
- ✅ Detección de colisiones con rectángulos
- ✅ Manejo de eventos de teclado
- ✅ Integración de assets (imágenes y sonidos)

### Blandos
- ✅ Trabajo en equipo con Git/GitHub
- ✅ Code reviews y feedback constructivo
- ✅ Gestión de tareas con Trello
- ✅ Resolución de conflictos de código
- ✅ Comunicación técnica efectiva

---

## 📚 Referencias y Recursos

- [Documentación oficial de Pygame](https://www.pygame.org/docs/)
- [Tutorial de Git en español](https://git-scm.com/book/es/v2)
- [PEP 8 - Guía de estilo de Python](https://peps.python.org/pep-0008/)

---

**Este proyecto demuestra que con buena organización, herramientas adecuadas y trabajo en equipo, un grupo de estudiantes puede crear un producto funcional y divertido.**
