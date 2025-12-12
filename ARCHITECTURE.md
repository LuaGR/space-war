# Architecture Decision Records (ADR)
## La Venganza de la Paloma

> **Proyecto:** Space shooter arcade con temática peruana  
> **Stack:** Python 3.x + Pygame  
> **Última actualización:** Diciembre 2025

---

## Tabla de Contenidos

1. [ADR-001: Paradigma de Programación Orientado a Objetos](#adr-001-paradigma-de-programación-orientado-a-objetos)
2. [ADR-002: Uso de Pygame como Motor de Juego](#adr-002-uso-de-pygame-como-motor-de-juego)
3. [ADR-003: Arquitectura Modular por Entidades](#adr-003-arquitectura-modular-por-entidades)
4. [ADR-004: Game Loop Imperativo con 60 FPS](#adr-004-game-loop-imperativo-con-60-fps)
5. [ADR-005: Sistema de Manejo de Eventos Sin Estado Global](#adr-005-sistema-de-manejo-de-eventos-sin-estado-global)
6. [ADR-006: Sistema de Vidas con Respawn](#adr-006-sistema-de-vidas-con-respawn)
7. [ADR-007: Dificultad Dinámica Basada en Score](#adr-007-dificultad-dinámica-basada-en-score)
8. [ADR-008: Sistema de Pausa y Mute](#adr-008-sistema-de-pausa-y-mute)
9. [ADR-009: Assets con Identidad Cultural Peruana](#adr-009-assets-con-identidad-cultural-peruana)
10. [ADR-010: Gestión de Colisiones Manual](#adr-010-gestión-de-colisiones-manual)
11. [ADR-011: Flujo de Trabajo Git con PRs](#adr-011-flujo-de-trabajo-git-con-prs)

---

## ADR-001: Paradigma de Programación Orientado a Objetos

### Estado
✅ **Aceptado** e implementado

### Contexto
El equipo tiene niveles mixtos de experiencia (3 Trainees, 1 Novato, 1 Líder Técnico). Necesitamos una arquitectura que sea:
- Fácil de entender para quienes están aprendiendo Python desde cero
- Escalable para agregar nuevas entidades (power-ups, jefes, etc.)
- Mantenible para trabajo en paralelo sin conflictos

### Decisión
Usaremos **Programación Orientada a Objetos (POO)** como paradigma principal:
- Cada entidad del juego (Player, Enemy, Bullet, Score, HealthBar) es una **clase independiente**
- Cada clase encapsula sus propios atributos (posición, velocidad, vida) y comportamientos (update, draw, shoot)
- Las instancias se gestionan mediante listas de Python simples (`enemies = []`, `bullets = []`)

### Consecuencias

**Positivas:**
- ✅ Código altamente modular: cada miembro puede trabajar en su propia clase sin conflictos
- ✅ Fácil de entender: "un enemigo es un objeto Enemy con posición X/Y y velocidad"
- ✅ Facilita el debugging: si las balas fallan, el problema está en `bullet.py`

**Negativas:**
- ⚠️ Más verboso que un enfoque funcional o ECS (Entity-Component-System)
- ⚠️ Potencial duplicación de código (todos los objetos tienen `.draw()` y `.update()`)

**Mitigaciones:**
- Se evitó usar herencia compleja o patrones avanzados (decorators, mixins) para mantener simplicidad

---

## ADR-002: Uso de Pygame como Motor de Juego

### Estado
✅ **Aceptado** e implementado

### Contexto
Necesitamos una librería de Python que:
- Maneje gráficos 2D, sonidos, colisiones y eventos de teclado
- Sea lo suficientemente simple para que principiantes puedan leer su código
- No requiera conocimientos previos de OpenGL, DirectX o motores complejos como Unity/Godot

### Decisión
Usaremos **Pygame 2.x** como motor de juego.

### Alternativas Consideradas

| Librería | Pros | Contras | Decisión |
|----------|------|---------|----------|
| **Pygame** | ✅ Simple, documentada, comunidad grande | Poco performante para juegos complejos | ✅ **ELEGIDA** |
| **Arcade** | Más moderna, mejor performance | Menos documentación en español | ❌ Rechazada |
| **Godot (GDScript)** | Motor completo con editor visual | Curva de aprendizaje muy alta | ❌ Rechazada |
| **Ren'Py** | Excelente para visual novels | No es para shooters | ❌ Rechazada |

### Consecuencias

**Positivas:**
- ✅ Instalación trivial: `pip install pygame`
- ✅ Código Python puro, sin sintaxis especial
- ✅ Abundancia de tutoriales en español

**Negativas:**
- ⚠️ Performance limitada (no es viable para juegos con 10,000+ objetos en pantalla)
- ⚠️ API algo antigua (usa conceptos de SDL 1.2)

**Mitigaciones:**
- El scope del juego es pequeño (máx. 10 enemigos simultáneos), por lo que la performance es suficiente

---

## ADR-003: Arquitectura Modular por Entidades

### Estado
✅ **Aceptado** e implementado

### Contexto
Necesitamos una estructura de archivos que permita:
- Trabajo en paralelo (5 personas sin pisarse)
- Que sea intuitivo para nuevos miembros encontrar el código que buscan
- Facilitar code reviews en Pull Requests (cambios concentrados en 1-2 archivos)

### Decisión
La estructura de carpetas es:

```
space-war/
│
├── main.py              # Orquestador: game loop, lógica de alto nivel
├── constants.py         # Configuraciones globales (SCREEN_WIDTH, SCREEN_HEIGHT)
├── requirements.txt     # Dependencias (solo 'pygame')
├── ARCHITECTURE.md      # Este documento (ADR)
├── README.md            # Instrucciones de instalación y contexto
│
├── game/                # Paquete Python con la lógica del juego
│   ├── __init__.py      # Marca 'game/' como paquete
│   ├── player.py        # Clase Player (movimiento WASD, disparo)
│   ├── enemy.py         # Clase Enemy (movimiento horizontal + descenso)
│   ├── bullet.py        # Clase Bullet (movimiento vertical hacia arriba)
│   ├── score.py         # Clase Score (contador + renderizado)
│   └── healthbar.py     # Clase Health_Bar (corazones visuales)
│
└── assets/              # Recursos artísticos (NO hay código aquí)
    ├── image/           # Sprites (.png con transparencia)
    │   ├── Paloma_meme_1.png        # Jugador
    │   ├── Alan_Garcia_muerto_meme.png  # Enemigo
    │   ├── Corazon_healt.png        # Vida
    │   └── Fondo_meme_palacio_de_gobierno.png  # Background
    └── sounds/          # Audio (.wav, .mp3)
        ├── Triciclo Perú.wav        # Música de fondo
        ├── lazer-gun-432285.wav     # Sonido de disparo
        ├── explosion-under-snow-sfx-230505.wav  # Sonido de explosión
        └── sound-of-collision.wav   # Sonido de score
```

### Justificación de `game/` vs. `src/`
Se eligió el nombre **`game/`** en lugar del genérico `src/` por **claridad semántica**. Un nuevo miembro sabe inmediatamente que la lógica del juego vive ahí.

### Consecuencias

**Positivas:**
- ✅ Separación de responsabilidades: cada archivo tiene un único propósito
- ✅ PRs pequeños y fáciles de revisar (generalmente 1 archivo modificado)
- ✅ Facilita testing: puedes probar `Bullet` sin instanciar `Player` o `Enemy`

**Negativas:**
- ⚠️ Más archivos = más imports en `main.py`
- ⚠️ Potencial para "over-engineering" si se crean archivos para cosas triviales

**Mitigaciones:**
- Solo se crea un archivo nuevo si la clase tiene más de 50 líneas o responsabilidades claramente diferenciadas

---

## ADR-004: Game Loop Imperativo con 60 FPS

### Estado
✅ **Aceptado** e implementado

### Contexto
Todos los juegos de acción necesitan un **bucle principal** que se ejecute constantemente. Necesitamos decidir:
- ¿Cuántas veces por segundo debe ejecutarse? (FPS)
- ¿Qué orden de operaciones seguimos? (input → update → render)
- ¿Cómo manejamos la pausa y el game over?

### Decisión
Implementamos un **Game Loop imperativo** en `main.py` con 3 fases claras:

```python
while running:
    # 1. INPUT: Manejar eventos (teclado, cerrar ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_movement(event)
        if event.key == pygame.K_SPACE:
            bullets.append(Bullet())

    # 2. UPDATE: Cambiar el estado del juego (NO DIBUJAR)
    if not paused and not game_over:
        player.update()
        for enemy in enemies:
            enemy.update()
        for bullet in bullets:
            bullet.update()
        # Detectar colisiones...

    # 3. DRAW: Dibujar en pantalla (NO TOMAR DECISIONES)
    screen.blit(background_img, (0, 0))
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    score.draw()
    health_bar.draw()
    pygame.display.flip()

    clock.tick(60)  # Limitar a 60 FPS
```

**Regla de Oro:** 
- En la fase `UPDATE`, **NO SE DIBUJA NADA**.
- En la fase `DRAW`, **NO SE TOMA NINGUNA DECISIÓN LÓGICA**.

### Consecuencias

**Positivas:**
- ✅ Fácil de seguir: el flujo es lineal y predecible
- ✅ Debugging simplificado: si algo no se mueve, el problema está en `UPDATE`. Si no se ve, está en `DRAW`.
- ✅ 60 FPS constantes aseguran jugabilidad fluida

**Negativas:**
- ⚠️ El código de `main.py` puede crecer mucho (actualmente ~265 líneas)
- ⚠️ Lógica de colisiones está mezclada con el game loop

**Mitigaciones:**
- Se aceptó el crecimiento de `main.py` como trade-off por mantener la lógica centralizada y fácil de entender

---

## ADR-005: Sistema de Manejo de Eventos Sin Estado Global

### Estado
✅ **Aceptado** e implementado

### Contexto
El jugador se mueve con **teclas WASD**. Necesitamos decidir cómo detectar cuando una tecla está presionada:
- ¿Verificamos `pygame.key.get_pressed()` en cada frame?
- ¿O usamos eventos `KEYDOWN` y `KEYUP` para trackear el estado?

### Decisión
Usamos **eventos de Pygame** (`KEYDOWN`/`KEYUP`) combinados con **flags booleanos** en la clase `Player`:

```python
class Player:
    def __init__(self):
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: self.move_left = True
            if event.key == pygame.K_d: self.move_right = True
            # ...
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a: self.move_left = False
            if event.key == pygame.K_d: self.move_right = False

    def update(self):
        if self.move_left: self.x -= self.speed
        if self.move_right: self.x += self.speed
        # ...
```

**Ventaja:** El jugador solo se mueve mientras la tecla esté presionada. Al soltar, el movimiento se detiene inmediatamente.

### Alternativa Rechazada
Usar `pygame.key.get_pressed()` directamente en `main.py`:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_a]:
    player.x -= 5
```

**Por qué fue rechazada:**
- ❌ Viola el principio de encapsulación (la lógica del jugador estaría en `main.py`)
- ❌ Más difícil de testear

### Consecuencias

**Positivas:**
- ✅ La clase `Player` es autosuficiente
- ✅ Fácil de extender (podemos agregar doble tap para dash, por ejemplo)

**Negativas:**
- ⚠️ Más código boilerplate (4 flags por cada dirección)

---

## ADR-006: Sistema de Vidas con Respawn

### Estado
✅ **Aceptado** e implementado

### Contexto
Queríamos un juego más permisivo que el clásico "1 hit = game over". Decidimos implementar:
- 3 vidas (representadas por corazones)
- Al recibir daño, el jugador reaparece en el centro y pierde 1 vida
- Game over solo cuando las 3 vidas se agoten

### Decisión
Creamos la clase `Health_Bar` que:
- Maneja el estado de vida actual (`current_health`)
- Dibuja corazones visuales en la esquina superior derecha
- Expone métodos `lose_health()`, `is_alive()`, `reset_health()`

Cuando un enemigo colisiona con el jugador:

```python
if enemy_rect.colliderect(player_rect):
    health_bar.lose_health()
    enemies.remove(enemy)
    if not health_bar.is_alive():
        game_over = True
    else:
        player.reset_position()  # Vuelve al centro
```

### Consecuencias

**Positivas:**
- ✅ Juego más accesible para principiantes
- ✅ Feedback visual claro (corazones desaparecen)
- ✅ Permite errores sin penalización inmediata

**Negativas:**
- ⚠️ Puede hacer el juego demasiado fácil al inicio

**Mitigaciones:**
- Se implementó dificultad dinámica para compensar (ver ADR-007)

---

## ADR-007: Dificultad Dinámica Basada en Score

### Estado
✅ **Aceptado** e implementado

### Contexto
El juego se volvía monótono después de 30 segundos. Necesitábamos un sistema que aumentara la dificultad progresivamente sin hacer cambios manuales.

### Decisión
Implementamos **dificultad dinámica** basada en el `score` del jugador:

```python
puntos = score.score

# 1. Máximo de enemigos simultáneos aumenta con el score
max_enemigos = min(10, 4 + puntos // 2)

# 2. Intervalo de spawn disminuye (más enemigos aparecen)
current_interval = max(600, ENEMY_SPAWN_INTERVAL - puntos * 120)

# 3. Velocidad de enemigos aumenta
speed_factor = 1.0 + (puntos // 3) * 0.25
enemies.append(Enemy(speed_factor=speed_factor))
```

**Ejemplo de progresión:**
| Score | Max Enemigos | Spawn Interval (ms) | Speed Factor |
|-------|--------------|---------------------|--------------|
| 0     | 4            | 2000                | 1.0x         |
| 4     | 6            | 1520                | 1.25x        |
| 8     | 8            | 1040                | 1.5x         |
| 12    | 10           | 600                 | 2.0x         |

### Consecuencias

**Positivas:**
- ✅ Juego escalable: siempre hay un desafío nuevo
- ✅ Replayability: cada partida es única
- ✅ Sensación de progresión sin niveles explícitos

**Negativas:**
- ⚠️ Puede volverse imposible después de cierto score
- ⚠️ No hay "jefes" ni cambios de escenario

**Mejoras Futuras:**
- Agregar power-ups cuando el score sea múltiplo de 10
- Cambiar color del fondo cada 20 puntos

---

## ADR-008: Sistema de Pausa y Mute

### Estado
✅ **Aceptado** e implementado

### Contexto
Durante las pruebas, los testers pedían poder pausar el juego sin cerrarlo. También, algunos encuentran la música repetitiva.

### Decisión
Implementamos dos funcionalidades adicionales:

**1. Pausa (tecla P):**
```python
if event.key == pygame.K_p:
    paused = not paused
    if paused:
        pygame.mixer.music.pause()
        pause_start_tick = pygame.time.get_ticks()
    else:
        pygame.mixer.music.unpause()
        total_paused_time += (pygame.time.get_ticks() - pause_start_tick)
```

- Detiene el UPDATE loop
- Pausa la música
- Muestra overlay "PAUSA" en pantalla
- Ajusta el tiempo total para que el timer no cuente el tiempo pausado

**2. Mute (tecla M):**
```python
if event.key == pygame.K_m:
    muted = not muted
    if muted:
        pygame.mixer.music.set_volume(0)
        laser_sound.set_volume(0)
        explosion_sound.set_volume(0)
    else:
        pygame.mixer.music.set_volume(0.5)
        laser_sound.set_volume(1.0)
        explosion_sound.set_volume(1.0)
```

- Silencia todos los sonidos sin detener el juego
- Muestra indicador "MUTE" en esquina superior derecha

### Consecuencias

**Positivas:**
- ✅ Mejora la UX significativamente
- ✅ Permite jugar en entornos donde el sonido no es apropiado

**Negativas:**
- ⚠️ Agrega complejidad al game loop (muchos flags: `paused`, `muted`, `game_over`)

---

## ADR-009: Assets con Identidad Cultural Peruana

### Estado
✅ **Aceptado** e implementado

### Contexto
Inicialmente, el proyecto se llamaba "Space War" genérico. Durante el desarrollo, el equipo decidió darle una identidad única usando **memes y referencias peruanas**.

### Decisión
Los assets son:
- **Jugador:** Paloma (ave símbolo de Perú)
- **Enemigo:** Alan García (expresidente fallecido, convertido en meme)
- **Fondo:** Palacio de Gobierno de Lima
- **Música:** "Triciclo Perú" (audio viral peruano)

**Nombre del juego:** **"La Venganza de la Paloma"**

### Justificación
- ✅ Da personalidad única al proyecto
- ✅ Facilita la identificación del juego en portfolios
- ✅ Promueve la cultura peruana de forma humorística

### Consecuencias

**Positivas:**
- ✅ Memorable: nadie más tiene un juego así
- ✅ Potencial de viralización en redes sociales peruanas

**Negativas:**
- ⚠️ Puede ser culturalmente sensible (Alan García es figura política)
- ⚠️ Audiencia limitada a público peruano o latinoamericano

**Mitigaciones:**
- Los assets son intercambiables (están en `assets/`, no hardcodeados)
- Se puede crear un "reskin" con assets genéricos si es necesario

---

## ADR-010: Gestión de Colisiones Manual

### Estado
✅ **Aceptado** (con plan de refactor futuro)

### Contexto
Pygame ofrece `pygame.sprite.Group` para gestionar colisiones automáticamente. Sin embargo, decidimos implementar colisiones manualmente al inicio.

### Decisión
Las colisiones se detectan usando `pygame.Rect.colliderect()` en el game loop de `main.py`:

```python
# Colisión bala-enemigo
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

### Justificación
- ✅ **Pedagógica:** Los miembros novatos entienden exactamente cómo funcionan las colisiones
- ✅ **Control total:** Podemos decidir qué hacer exactamente cuando dos objetos colisionan
- ✅ **Sin abstracciones:** No hay "magia" de Pygame que oculte la lógica

### Alternativa: `pygame.sprite.Group`
```python
# Con sprite.Group (más eficiente, menos claro)
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

collisions = pygame.sprite.groupcollide(bullets_group, enemies_group, True, True)
for bullet, enemies_hit in collisions.items():
    score.add()
```

**Por qué NO lo usamos:**
- ❌ Menor claridad sobre qué hace `groupcollide()` internamente
- ❌ Requiere que todas las clases hereden de `pygame.sprite.Sprite`
- ❌ Más difícil de debuggear

### Consecuencias

**Positivas:**
- ✅ Código transparente
- ✅ Control total de la lógica de colisiones

**Negativas:**
- ⚠️ Código más verboso (muchos loops anidados)
- ⚠️ Performance O(n²) cuando hay muchos objetos

---

## ADR-011: Flujo de Trabajo Git con PRs

### Estado
✅ **Aceptado** e implementado

### Contexto
Equipo de 5 personas con niveles mixtos de experiencia (3 Trainees, 1 Novato, 1 Líder Técnico). Necesitamos:
- Evitar que alguien rompa `main` accidentalmente
- Facilitar mentoría y code reviews
- Mantener historial limpio de commits

### Decisión

**Estructura de ramas:**
- `main`: Rama protegida. Solo el Líder Técnico puede hacer merge.
- `feature/[nombre]`: Para nuevas funcionalidades
- `fix/[nombre]`: Para corrección de bugs
- `assets/[nombre]`: Para agregar/modificar assets
- `docs/[nombre]`: Para documentación

**Flujo de trabajo:**
1. Crear tarjeta en Trello con la tarea
2. Crear rama local: `git checkout -b feature/player-movement`
3. Hacer commits en inglés con prefijos: `feat: add WASD movement to Player`
4. Hacer push: `git push origin feature/player-movement`
5. Abrir Pull Request en GitHub hacia `main`
6. Asignar al Líder Técnico para review
7. Líder Técnico revisa, comenta y aprueba
8. Merge a `main`
9. Mover tarjeta de Trello a "Hecho"

**Prefijos de commits:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `refactor:` Mejora de código sin cambiar funcionalidad
- `test:` Tests
- `chore:` Tareas menores (actualizar .gitignore, etc.)

### Consecuencias

**Positivas:**
- ✅ `main` siempre es funcional
- ✅ Code reviews son la principal herramienta de mentoría
- ✅ Historial de Git es legible y útil

**Negativas:**
- ⚠️ Puede ralentizar el desarrollo (hay que esperar aprobación)
- ⚠️ Requiere disciplina del equipo

**Mitigaciones:**
- El Líder Técnico se compromete a revisar PRs en máximo 24 horas
- PRs pequeños (1-2 archivos) se priorizan

---

## Definición de "Hecho" (Definition of Done)

Una tarea solo se considera **"Hecha"** si cumple TODO lo siguiente:

1. ✅ El código cumple con todos los requisitos de la tarea
2. ✅ El código no "rompe" ninguna funcionalidad existente
3. ✅ El código sigue los estándares (prefijos de commit, estilo de código)
4. ✅ El código ha sido revisado y aprobado por el Líder Técnico
5. ✅ La rama ha sido fusionada (`merged`) a `main`
6. ✅ La tarjeta de Trello está en la columna "¡Hecho!"

---

## Stack Tecnológico

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.x | Lenguaje principal |
| **Pygame** | 2.x | Motor de juego 2D |
| **Git** | 2.x | Control de versiones |
| **GitHub** | - | Hosting de repositorio y PRs |
| **Trello** | - | Gestión de tareas (Kanban) |

---

## Métricas del Proyecto

| Métrica | Valor Actual |
|---------|--------------|
| Líneas de código | ~500 LOC |
| Archivos Python | 8 archivos |
| Clases implementadas | 5 clases |
| FPS | 60 constantes |
| Max enemigos simultáneos | 10 |
| Vidas del jugador | 3 |
| Features core | 100% completas |

---

**Este documento es la fuente de verdad para el proyecto. Cualquier decisión técnica importante debe registrarse aquí.**
