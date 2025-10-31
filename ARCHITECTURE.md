<!-- markdownlint-disable -->
# Documentación de Arquitectura: Space War

## 1. Propósito y Filosofía de Diseño

### 1.1. Propósito

Este documento describe la arquitectura de software, las decisiones técnicas y los estándares de colaboración para el proyecto "Space War". Sirve como la "fuente de verdad" para todos los miembros del equipo.

El objetivo principal no es solo entregar un juego funcional, sino también **facilitar el aprendizaje** de Python, Pygame y Git para todos los miembros.

### 1.2. Filosofía de Diseño

Nuestra arquitectura se basa en tres principios clave:

1.  **Simplicidad sobre Complejidad:** Siempre elegiremos la solución más simple y legible. Es más importante que un miembro novato entienda el código a que este sea el más "eficiente" o "avanzado".
2.  **Modularidad:** Cada "cosa" en el juego debe tener su propio archivo (`player.py`, `enemy.py`). Esto nos permite trabajar en paralelo sin pisarnos.
3.  **Consistencia:** Seguiremos los mismos estándares de nombrado (prefijos, commits en inglés) y el mismo flujo de trabajo (Trello -\> Branch -\> PR) sin excepción.

## 2. Stack Tecnológico y Justificación

### **Python 3.x** - Lenguaje de programación principal
Su sintaxis limpia y fácil lectura lo hacen ideal para un equipo con habilidades mixtas, especialmente para los 2 miembros que están aprendiendo desde cero.

### **Pygame** - Librería para desarrollo de juegos
Es la librería estándar de Python para juegos 2D. Proporciona módulos esenciales listos para usar (ventana, gráficos, sonido, eventos de teclado) que nos permiten enfocarnos en la *lógica* del juego y no en crear un motor gráfico desde cero.

### **Git** - Sistema de control de versiones
Esencial para el trabajo colaborativo. Nos permite rastrear cambios, experimentar en ramas sin romper el juego principal y fusionar el trabajo de 6 personas de forma ordenada.

### **GitHub** - Plataforma de hosting de repositorios
Es el "servidor central" de nuestro código. Su función de **Pull Requests** es la piedra angular de nuestra estrategia de mentoría y revisión de código.

### **Trello** - Gestión de tareas (Kanban)
Proporciona una visión clara y visual de qué hay por hacer, quién lo está haciendo y qué está terminado. Es fundamental para que el Líder Técnico gestione el proyecto y para que los miembros del equipo sepan en qué trabajar.

## 3\. Arquitectura del Código (Estructura)

La estructura de carpetas está diseñada para ser intuitiva y desacoplada.

```
space-war/
│
├── .gitignore          # Ignora archivos temporales (Pycache, venv).
├── README.md           # Instrucciones de cómo instalar y ejecutar.
├── ARCHITECTURE.md     # (Este archivo)
├── requirements.txt    # Lista de dependencias (solo 'pygame').
├── main.py             # PUNTO DE ENTRADA. Orquesta el juego.
│
├── game/               # Lógica principal del juego (nuestro "paquete").
│   ├── __init__.py     # Le dice a Python que 'game/' es un paquete.
│   ├── player.py       # Define la clase 'Player'.
│   ├── enemy.py        # Define la clase 'Enemy'.
│   ├── bullet.py       # Define la clase 'Bullet'.
│   └── ...             # (futuras clases: score.py, screen.py, etc.)
│
└── assets/             # Recursos artísticos. NADA de código aquí.
    ├── images/         # Sprites (.png con transparencia).
    ├── sounds/         # Efectos de sonido (.wav o .ogg).
    └── music/          # Música de fondo (.mp3).
```

### Justificación de `game/` vs. `src/`:

Se eligió el nombre `game/` en lugar del genérico `src/` por **claridad semántica**. Es inmediatamente obvio para un miembro nuevo que la lógica del juego (clases, etc.) vive dentro de esa carpeta.

## 4. Flujo de Datos (El Bucle Principal)

El corazón de `main.py` es el **Game Loop**. Este bucle se ejecuta 60 veces por segundo (60 FPS) y sigue un patrón estricto:

1.  **Manejar Entradas (Input):**

      * Comprueba todos los eventos de Pygame (teclado, ratón, cerrar ventana).
      * Ej: ¿El jugador presionó `ESPACIO`? ¿Presionó `FLECHA IZQUIERDA`?

2.  **Actualizar Estado (Update):**

      * **NO SE DIBUJA NADA AQUÍ.**
      * Mueve al jugador si una tecla está presionada.
      * Mueve a todos los enemigos.
      * Mueve todas las balas.
      * Comprueba colisiones (Balas vs Enemigos, Enemigo vs Jugador).
      * Crea/destruye objetos (ej. crear una bala, destruir un enemigo).
      * Actualiza el puntaje.

3.  **Dibujar en Pantalla (Draw / Render):**

      * **NO SE TOMA NINGUNA DECISIÓN LÓGICA AQUÍ.**
      * Rellena la pantalla con el color de fondo (negro).
      * Dibuja al jugador en su nueva posición (`.blit()`).
      * Dibuja a cada enemigo en su nueva posición.
      * Dibuja cada bala en su nueva posición.
      * Dibuja el puntaje.
      * Finalmente, le dice a Pygame que muestre todo lo dibujado (`pygame.display.flip()`).

## 5. Componentes Clave (Clases Principales)

  * `main.py` (**El Orquestador**):

      * **Responsabilidad:** Inicializar Pygame, crear la ventana, cargar assets, crear instancias de objetos (un `Player`, una lista de `Enemies`) y ejecutar el Game Loop.
      * **No debe** contener la lógica *interna* del jugador (ej. `player.move_left()` es correcto, `player.x = player.x - 5` es incorrecto).

  * `game/player.py` (Clase `Player`):

      * **Responsabilidad:** Contiene todo sobre el jugador.
      * **Atributos:** Su imagen (`.image`), su posición (`.rect`), su velocidad, su vida.
      * **Métodos:** `move(dx, dy)`, `shoot()`, `draw(screen)`.

  * `game/enemy.py` (Clase `Enemy`):

      * **Responsabilidad:** Contiene todo sobre un *único* enemigo.
      * **Atributos:** Su imagen, posición (`.rect`), velocidad, tipo.
      * **Métodos:** `update()`, `draw(screen)`.

  * `game/bullet.py` (Clase `Bullet`):

      * **Responsabilidad:** Contiene todo sobre una *única* bala.
      * **Atributos:** Su imagen, posición (`.rect`), velocidad.
      * **Métodos:** `update()` (moverse hacia arriba), `draw(screen)`.

## 6. Flujo de Colaboración (Arquitectura de Repositorio)

Nuestra arquitectura de repositorio (Git) es tan importante como nuestra arquitectura de código.

1.  **Rama `main`:** Es la rama principal. **Está protegida.** Nadie puede hacer `push` directamente a ella. Todo el código en `main` debe ser funcional.
2.  **Ramas de Tarea:** Todo el trabajo se realiza en ramas separadas. El nombre de la rama **debe** corresponder a una tarjeta de Trello.
      * **Formato:** `[prefijo]/[nombre-tarea]` (ej. `feature/player-movement`, `assets/add-sounds`).
      * Ver la tarjeta de Trello `Guía de Prefijos` para los prefijos.
3.  **Commits:** Se hacen en inglés, usando prefijos (ej. `feat:`, `fix:`, `docs:`).
4.  **Pull Requests (PRs):** Cuando una tarea está terminada, el miembro crea un Pull Request en GitHub de su rama hacia `main`.
5.  **Revisión de Código:** El Líder Técnico es asignado automáticamente para revisar el PR. Esta es nuestra principal herramienta de mentoría. Aquí se revisa que el código funcione y que siga los estándares.
6.  **Merge (Fusión):** Solo el Líder Técnico puede aprobar y fusionar un PR. Una vez fusionado, la tarjeta de Trello se mueve a `¡Hecho!`.

## 7. Definición de "Hecho" (Definition of Done)

Una tarea (y su tarjeta de Trello) solo se considera **"Hecha"** si cumple TODO lo siguiente:

1.  El código cumple con todos los requisitos de la tarea.
2.  El código no "rompe" ninguna funcionalidad existente.
3.  El código sigue los estándares (prefijos de commit, estilo de código).
4.  El código ha sido revisado y aprobado por el Líder Técnico.
5.  La rama ha sido fusionada (`merged`) a `main`.

## 8. Riesgos y Decisiones de Mitigación

  * **Riesgo:** Nivel de habilidad mixto (3 Juniors, 2 Novatos).

      * **Mitigación:**
        1.  **Mentoría Activa:** Los PRs son la herramienta principal.
        2.  **Tareas Claras:** Las tarjetas de Trello tienen checklists detalladas.
        3.  **Tareas Paralelas:** Los Novatos contribuyen con Assets y Documentación mientras aprenden Python, para que siempre estén integrados al equipo.

  * **Decisión Arquitectónica:** No se usarán `pygame.sprite.Group` al inicio.

      * **Motivo:** Aunque son más eficientes, la lógica de `Group` es abstracta. Para fines de aprendizaje, es mejor que los Juniors implementen la gestión de listas (ej. `for bullet in bullets_list:`) y la detección de colisiones (`bullet.rect.colliderect(enemy.rect)`) manualmente.
      * **Plan:** Se puede **refactorizar** el código para usar `sprite.Group` en el Sprint 5 o 6, una vez que el equipo entienda la lógica fundamental.
