# 🏓 Ping Pong Game

A classic Ping Pong (Pong) game built with Python and Pygame, featuring smooth gameplay, AI opponent, sound effects, and multiple game modes.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Modes](#game-modes)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Sound Setup](#sound-setup)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## ✨ Features

- **Classic Pong Gameplay** - Smooth, responsive controls with realistic ball physics
- **AI Opponent** - Challenging computer player with intelligent tracking
- **Enhanced Collision Detection** - No more ball-through-paddle issues at high speeds
- **Multiple Game Modes** - Choose from Best of 3, 5, or 7
- **Sound Effects** - Audio feedback for paddle hits, wall bounces, and scoring
- **Dynamic Ball Physics** - Ball angle changes based on where it hits the paddle
- **Game Over System** - Winner announcements with replay options
- **Score Display** - Real-time score tracking with winning target indicator

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download the project**
   ```bash
   git clone <your-repo-url>
   cd ping-pong-game
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Set up the project structure**
   ```
   ping-pong-game/
   ├── game/
   │   ├── __init__.py
   │   ├── ball.py
   │   ├── paddle.py
   │   ├── game_engine.py
   │   └── sound_manager.py
   ├── sounds/              (optional - see Sound Setup)
   │   ├── paddle_hit.wav
   │   ├── wall_bounce.wav
   │   └── score.wav
   └── main.py
   ```

4. **Run the game**
   ```bash
   python main.py
   ```

## 🎮 How to Play

### Controls

| Key | Action |
|-----|--------|
| **W** | Move paddle up |
| **S** | Move paddle down |
| **3** | Start Best of 3 (on replay menu) |
| **5** | Start Best of 5 (on replay menu) |
| **7** | Start Best of 7 (on replay menu) |
| **ESC** | Exit game (on replay menu) |

### Objective

- Use your paddle (left side) to hit the ball back to the AI opponent
- Score points when the ball passes your opponent's paddle
- First player to reach the target score wins
- The ball's angle changes based on where it hits your paddle

### Gameplay Tips

- **Top/Bottom Hits**: Hit the ball with the top or bottom of your paddle to change its angle
- **Center Hits**: Hit with the center for a straighter shot
- **Defensive Play**: Stay centered and react to the ball's direction
- **Offensive Play**: Aim for sharp angles to make it harder for the AI

## 🏆 Game Modes

After each match, choose your next game mode:

| Mode | Target Score | Description |
|------|--------------|-------------|
| **Best of 3** | First to 2 | Quick matches - perfect for beginners |
| **Best of 5** | First to 3 | Standard mode - balanced gameplay |
| **Best of 7** | First to 4 | Extended matches - for competitive play |

## 📁 Project Structure

```
ping-pong-game/
│
├── game/                      # Game package directory
│   ├── __init__.py           # Makes 'game' a Python package
│   ├── ball.py               # Ball class with physics and collision
│   ├── paddle.py             # Paddle class with movement and AI
│   ├── game_engine.py        # Main game logic and state management
│   └── sound_manager.py      # Audio system and sound effects
│
├── sounds/                    # Sound effects directory (optional)
│   ├── paddle_hit.wav        # Ball hitting paddle sound
│   ├── wall_bounce.wav       # Ball hitting wall sound
│   └── score.wav             # Scoring sound effect
│
└── main.py                    # Entry point - runs the game
```

### File Descriptions

#### `main.py`
- Application entry point
- Initializes Pygame and game window
- Manages main game loop
- Handles high-level event processing

#### `game/ball.py`
- `Ball` class for ball object
- Movement physics and velocity management
- **Continuous collision detection** to prevent tunneling
- Wall bounce detection
- Dynamic angle adjustment on paddle hits

#### `game/paddle.py`
- `Paddle` class for player and AI paddles
- Smooth movement with boundary checking
- AI auto-tracking algorithm
- Collision rectangle management

#### `game/game_engine.py`
- `GameEngine` class - central game controller
- Score tracking and game state management
- Input handling for gameplay and menus
- Rendering system for all game screens
- Game over detection and replay system

#### `game/sound_manager.py`
- `SoundManager` class for audio
- Loads and plays sound effects
- Volume control and balancing
- Graceful fallback when sounds are missing

## 🔧 Technical Details

### Collision Detection System

The game uses **continuous collision detection** to prevent the ball from passing through paddles at high speeds:

1. **Directional Checking**: Only checks the paddle the ball is moving toward
2. **Position Validation**: Verifies ball is on correct side before registering collision
3. **Position Correction**: Immediately pushes ball out of paddle after collision
4. **Single-Frame Resolution**: Ensures collision is handled in one frame

### AI Algorithm

The AI paddle uses a simple but effective tracking algorithm:
- Compares ball Y-position with paddle center
- Moves toward the ball at a constant speed
- Has the same movement constraints as the player

### Physics System

- **Ball Velocity**: Separate X and Y components for realistic movement
- **Bounce Mechanics**: Velocity reversal on collision
- **Dynamic Angles**: Ball trajectory changes based on paddle hit location
- **Speed Consistency**: Maintains consistent ball speed throughout the game

### Rendering Pipeline

1. Clear screen (black background)
2. Render gameplay elements OR menu screens
3. Update display buffer
4. Maintain 60 FPS with clock tick

## 🔊 Sound Setup

### Quick Start (No Sounds)

The game works perfectly **without sound files**. You'll see console warnings but gameplay is unaffected.

### Adding Sound Effects

1. **Create sounds directory**
   ```bash
   mkdir sounds
   ```

2. **Add three WAV files**:
   - `paddle_hit.wav` - Short, sharp sound (100-200ms)
   - `wall_bounce.wav` - Softer bounce sound (80-150ms)
   - `score.wav` - Celebratory beep (200-400ms)

3. **Where to find sounds**:
   - **Generate**: Use [BFXR](https://www.bfxr.net/) or [ChipTone](https://sfbgames.itch.io/chiptone)
   - **Download**: Try [Freesound.org](https://freesound.org/) or [Mixkit](https://mixkit.co/)
   - **Create**: Use Audacity to generate simple tone beeps

### Volume Control

Adjust volume in `game_engine.py`:

```python
# In __init__ method, after sound_manager creation
self.sound_manager.set_volume(0.7)  # 70% volume
```

## 🎨 Customization

### Change Game Speed

In `main.py`, adjust the FPS:
```python
FPS = 60  # Change to 30 for slower, 120 for faster
```

### Modify Ball Speed

In `ball.py`, change initial velocities:
```python
self.velocity_x = random.choice([-5, 5])  # Increase for faster
self.velocity_y = random.choice([-3, 3])
```

### Adjust Paddle Speed

In `paddle.py`, modify the speed:
```python
self.speed = 7  # Increase for faster paddles
```

In `game_engine.py`, change player movement:
```python
if keys[pygame.K_w]:
    self.player.move(-10, self.height)  # Change -10 to adjust speed
```

### Change Colors

In `game_engine.py`, modify the color constants:
```python
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
```

### Window Size

In `main.py`, adjust dimensions:
```python
WIDTH, HEIGHT = 800, 600  # Change to your preferred size
```

### Default Game Mode

In `game_engine.py`, change initial winning score:
```python
self.winning_score = 3  # Default best of 5 (was 5 for best of 9)
```

## 🐛 Troubleshooting

### Game Won't Start

**Problem**: Import errors or module not found
```
Solution: Ensure you have __init__.py in the game/ directory
```

**Problem**: Pygame not installed
```bash
Solution: pip install pygame
```

### No Sound Playing

**Problem**: Sound files not found
```
Solution: Check that WAV files are in sounds/ directory with exact names
- The game will still work without sounds
```

**Problem**: Sound too quiet
```python
Solution: Increase volume in game_engine.py
self.sound_manager.set_volume(1.0)  # Maximum volume
```

### Ball Passes Through Paddle

**Problem**: Should be fixed with current collision system
```
If it still happens:
1. Check your monitor's refresh rate
2. Lower FPS if needed
3. Reduce ball velocity
```

### Game Runs Too Fast/Slow

**Problem**: Frame rate issues
```python
Solution: Adjust FPS in main.py
clock.tick(60)  # Change 60 to desired FPS
```

### AI Too Easy/Hard

**Problem**: AI difficulty
```python
Solution: Adjust AI speed in paddle.py
self.speed = 5  # Lower = easier, higher = harder
```

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- Add difficulty levels (Easy, Medium, Hard)
- Implement power-ups (speed boost, paddle size change)
- Add two-player mode
- Create a pause menu
- Add particle effects
- Implement a tournament mode
- Add achievements system
- Create custom themes

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by the classic Pong (1972)
- Sound effects from various open-source libraries

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Technical Details](#technical-details)
3. Open an issue on the repository

---

**Enjoy the game!** 🏓

Made with ❤️ using Python and Pygame