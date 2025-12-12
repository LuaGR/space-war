# 🕊️ La Venganza de la Paloma

> **Space shooter arcade con temática peruana**

---

## 🎮 Descripción

Controla a una valiente paloma defendiendo el Palacio de Gobierno de Lima contra una invasión de Alan Garcías zombies. Esquiva, dispara y sobrevive el mayor tiempo posible mientras la dificultad aumenta progresivamente.

### Características

- 🕹️ Controles fluidos WASD + ESPACIO para disparar
- ❤️ Sistema de 3 vidas con respawn
- 📈 Dificultad dinámica (más enemigos y más veloces con el score)
- ⏸️ Pausa (tecla P) y mute (tecla M)
- 🎨 Assets peruanos con humor local
- 🎵 Música de "Triciclo Perú"

---

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes)

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/LuaGR/space-war.git
   cd space-war
   ```

2. **Crear entorno virtual (recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar:**
   ```bash
   python main.py
   ```

---

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| **W** | Mover arriba |
| **A** | Mover izquierda |
| **S** | Mover abajo |
| **D** | Mover derecha |
| **ESPACIO** | Disparar |
| **P** | Pausar/Reanudar |
| **M** | Silenciar/Activar audio |
| **ENTER** | Reiniciar (después de Game Over) |

---

## 📊 Mecánicas de Juego

### Sistema de Vidas
- Empiezas con 3 vidas (corazones)
- Al ser golpeado, pierdes 1 vida y reapareces en el centro
- Game Over cuando pierdes las 3 vidas

### Dificultad Dinámica

El juego se ajusta automáticamente según tu puntaje:

| Score | Max Enemigos | Spawn (ms) | Velocidad |
|-------|--------------|------------|-----------|
| 0     | 4            | 2000       | 1.0x      |
| 4     | 6            | 1520       | 1.25x     |
| 8     | 8            | 1040       | 1.5x      |
| 12+   | 10           | 600        | 2.0x+     |

Cada punto que sumas:
- Reduce el tiempo entre apariciones de enemigos
- Aumenta la velocidad de movimiento
- Incrementa el número máximo de enemigos simultáneos

---

## 🏗️ Estructura del Proyecto

```
space-war/
│
├── main.py              # Game loop principal
├── constants.py         # Configuración global
├── requirements.txt     # Dependencias
├── ARCHITECTURE.md      # Documentación técnica
│
├── game/                # Clases del juego
│   ├── player.py        # Jugador
│   ├── enemy.py         # Enemigos
│   ├── bullet.py        # Balas
│   ├── score.py         # Puntaje
│   └── healthbar.py     # Vidas
│
└── assets/              # Recursos
    ├── image/           # Sprites PNG
    └── sounds/          # Audio WAV
```

---

## 🐛 Solución de Problemas

### Pygame no se instala
```bash
# macOS
brew install pygame

# Linux (Ubuntu/Debian)
sudo apt-get install python3-pygame

# Windows
pip install pygame --user
```

### Pantalla Retina en macOS
Si el juego se ve pixelado o tiene problemas de rendimiento:
```bash
# Usar Python nativo, no Rosetta
arch -arm64 python3 main.py
```

### Audio Bluetooth tiene delay
El audio puede tener retraso en dispositivos Bluetooth. Para mejor experiencia, usa los altavoces integrados o desactiva el audio con la tecla **M**.

---

## 📚 Más Información

Para detalles técnicos sobre arquitectura, decisiones de diseño y el proceso de desarrollo, consulta [ARCHITECTURE.md](ARCHITECTURE.md).

---

## 📜 Licencia

Proyecto de código abierto. Los assets visuales son memes de dominio público bajo uso legítimo (fair use).

---

**¿Te gustó el juego? Dale una ⭐ al repositorio!** 🇵🇪
