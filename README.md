# Snake Game

A classic Snake game developed using **Python and the Turtle graphics module**. The game features object-oriented programming, keyboard controls, collision detection, score tracking, and persistent high-score storage.

## Overview

This project is a recreation of the classic Snake game, developed using Python's Turtle graphics module.

The player controls a snake that moves around the game window, collecting food to increase its length and score. The game ends when the snake collides with the walls or its own body, resetting the current score while retaining the highest score achieved.

The project was developed to practise object-oriented programming, working with Python classes, handling keyboard input, and implementing basic game mechanics.

<img width="384" height="240" alt="snakegamegif" src="https://github.com/user-attachments/assets/64984467-6125-4dcd-aafd-e5171dad56d9" />

## Features

- **Snake Movement:** Control the snake using the keyboard arrow keys.
- **Food Collection:** Collect randomly positioned food to increase the snake's length.
- **Score Tracking:** Earn points for every piece of food collected.
- **Collision Detection:** Detect collisions with the game boundaries and the snake's own body.
- **High Score System:** Automatically save and retain the highest score between game sessions using file handling.
- **Game Reset:** Reset the snake and current score after a collision while preserving the high score.

## Technologies Used

- **Python 3**
- **Turtle Graphics:** Used to create the game window, render game objects, and handle graphical movement.
- **Tkinter:** Used internally by Python's Turtle module for the graphical interface.
- **File Handling:** Used to store and retrieve the persistent high score.

## Controls

| Key | Action |
|---|---|
| ↑ Up Arrow | Move Up |
| ↓ Down Arrow | Move Down |
| ← Left Arrow | Move Left |
| → Right Arrow | Move Right |

The snake cannot immediately reverse direction, preventing it from turning directly into itself.

## Project Structure

```text
python-snake-game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main game loop, keyboard input, collision detection, and game coordination. |
| `snake.py` | Snake class, movement, direction controls, and body extension. |
| `food.py` | Food class and random food positioning. |
| `scoreboard.py` | Score tracking and persistent high-score management. |
| `data.txt` | Stores the highest score between game sessions. |

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/python-snake-game.git
```

**2. Navigate into the project directory**

```bash
cd python-snake-game
```

**3. Initialise the high-score file**

Make sure `data.txt` exists in the project directory and contains:

```text
0
```

**4. Run the game**

```bash
python main.py
```

**Note:** Python's Turtle graphics module is included with standard Python installations. No additional third-party libraries are required.

## Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Python Classes and Inheritance
- Lists and Loops
- Keyboard Event Handling
- Collision Detection
- Random Number Generation
- File Reading and Writing
- Game Loops and Screen Updates

## Project Background

This project was developed as a practical exercise in Python programming, focusing on object-oriented design and implementing the mechanics of a simple interactive game.

It provided an opportunity to work with multiple classes, manage game objects, handle user input, and implement a persistent high-score system using file handling.
