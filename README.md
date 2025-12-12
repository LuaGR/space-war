# 🕊️ La Venganza de la Paloma

> **Space shooter arcade con temática peruana**

---

## 🎮 ¿De qué va el juego?

**"La Venganza de la Paloma"** es un shooter arcade vertical donde controlas a una valiente paloma defendiendo el Palacio de Gobierno de Lima contra una invasión de... ¡Alan Garcías zombies! 

Esquiva, dispara y sobrevive el mayor tiempo posible mientras la dificultad aumenta progresivamente. Con música del icónico "Triciclo Perú" y gráficos memeros, este juego es un homenaje humorístico a la cultura peruana.

---

## ✨ Características

- 🕹️ **Controles fluidos**: Movimiento WASD + disparo con ESPACIO
- ❤️ **Sistema de vidas**: 3 vidas con respawn
- 📈 **Dificultad dinámica**: Más enemigos, más veloces, más caos
- ⏸️ **Pausa**: Presiona P para pausar el juego
- 🔇 **Mute**: Presiona M para silenciar el audio
- 🎨 **Assets peruanos**: Paloma, Alan García, Palacio de Gobierno
- 🎵 **Música viral**: "Triciclo Perú" como banda sonora

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/space-war.git
   cd space-war
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el juego:**
   ```bash
   python main.py
   ```

---

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| **W** | Mover hacia arriba |
| **A** | Mover a la izquierda |
| **S** | Mover hacia abajo |
| **D** | Mover a la derecha |
| **ESPACIO** | Disparar |
| **P** | Pausar/Reanudar |
| **M** | Silenciar/Activar audio |
| **ENTER** | Reiniciar juego (en Game Over) |

---

## 🏗️ Arquitectura del Proyecto

```
space-war/
│
├── main.py              # Punto de entrada: game loop principal
├── constants.py         # Configuraciones globales (resolución, FPS)
├── requirements.txt     # Dependencias (pygame)
├── ARCHITECTURE.md      # Decisiones técnicas (ADR)
├── README.md            # Este archivo
│
├── game/                # Lógica del juego (POO)
│   ├── player.py        # Clase Player
│   ├── enemy.py         # Clase Enemy
│   ├── bullet.py        # Clase Bullet
│   ├── score.py         # Clase Score
│   └── healthbar.py     # Clase Health_Bar
│
└── assets/              # Recursos artísticos
    ├── image/           # Sprites
    │   ├── Paloma_meme_1.png
    │   ├── Alan_Garcia_muerto_meme.png
    │   ├── Corazon_healt.png
    │   └── Fondo_meme_palacio_de_gobierno.png
    └── sounds/          # Audio
        ├── Triciclo Perú.wav
        ├── lazer-gun-432285.wav
        ├── explosion-under-snow-sfx-230505.wav
        └── sound-of-collision.wav
```

Para más detalles sobre las decisiones técnicas, consulta el [ARCHITECTURE.md](ARCHITECTURE.md).

---

## 🧠 Decisiones Técnicas Clave

1. **Programación Orientada a Objetos (POO)**: Cada entidad (jugador, enemigo, bala) es una clase independiente.
2. **Game Loop de 60 FPS**: Separación clara entre INPUT → UPDATE → DRAW.
3. **Dificultad Dinámica**: El juego se adapta al score del jugador (más enemigos, más rápidos).
4. **Colisiones Manuales**: Implementadas con `pygame.Rect.colliderect()`.
5. **Assets con Identidad**: Temática peruana para darle personalidad única al proyecto.

---

## 📊 Mecánicas de Dificultad

| Score | Max Enemigos | Intervalo de Spawn (ms) | Velocidad Enemigos |
|-------|--------------|-------------------------|-------------------|
| 0     | 4            | 2000                    | 1.0x              |
| 4     | 6            | 1520                    | 1.25x             |
| 8     | 8            | 1040                    | 1.5x              |
| 12+   | 10           | 600                     | 2.0x+             |

---

## 🤝 Contribución

Flujo de trabajo Git:

1. Crear tarjeta en Trello con la tarea
2. Crear rama: `git checkout -b feature/nombre-tarea`
3. Hacer commits con prefijos: `feat:`, `fix:`, `docs:`, etc.
4. Crear Pull Request hacia `main`
5. Esperar revisión del Líder Técnico
6. Merge a `main`

**Prefijos de commits:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `refactor:` Mejora de código
- `chore:` Tareas menores

---

## 🐛 Problemas Conocidos

- En algunos sistemas macOS, Pygame puede tener problemas con pantallas Retina. Solución: ejecutar con Python nativo (no Rosetta).
- La música puede tener delay al inicio en sistemas con audio Bluetooth.

---

## 📜 Licencia

Proyecto de código abierto. Los assets son memes de dominio público/fair use.

---

**¿Te gustó el juego? Dale una ⭐ al repo!** 🇵🇪
