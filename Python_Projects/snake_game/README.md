
# Snake Game

A simple Snake Game implemented in Python using the `turtle` graphics library. The player controls a snake that grows longer each time it eats food. The game ends when the snake collides with the wall or with its own tail.

---

## Table of Contents

- [Snake Game](#snake-game)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Code Overview](#code-overview)
    - [`main.py`](#mainpy)
    - [`snake.py`](#snakepy)
    - [`food.py`](#foodpy)
    - [`scoreboard.py`](#scoreboardpy)
  - [Contributing](#contributing)

---

## Prerequisites

- Python 3.13.5 
- The standard library module `turtle` (included with most Python installations)  

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DevOps-Focused/Projects-and-custom-scripts.git
   cd Projects-and-custom-scripts/Python_Projects/snake_game
    ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Run the game**

   ```bash
   python main.py
   ```

---

## Usage

* **Arrow keys** control the movement of the snake:

  * Up → ↑
  * Down → ↓
  * Left → ←
  * Right → →

* Each time the snake's head collides with the food, the snake grows by one segment and the score increases by one.

* The game ends if:

  1. The snake collides with any wall edge.
  2. The snake’s head collides with any part of its own body.

* After **Game Over**, click on the window to exit.

---

## Project Structure

```
snake_game/
│
├── main.py          # Entry point: initializes screen, game loop, collision logic
├── snake.py         # Snake class: handles creation, movement, growth, and direction changes
├── food.py          # Food class: spawns food at random positions
└── scoreboard.py    # Scoreboard class: displays current score and 'Game Over' message
```

---

## Code Overview

### `main.py`

* **Imports**

  * `Screen` from `turtle` for the game window.
  * Custom classes: `Snake`, `Food`, `Scoreboard`.
  * `time` for controlling the animation speed.

* **Screen Setup**

  * Size: 600×600 pixels.
  * Background color: black.
  * Title: “My Snake Game”.
  * Disables automatic screen updates with `screen.tracer(0)` for manual control.

* **Game Objects**

  * `food` — an instance of `Food`.
  * `snake` — an instance of `Snake`.
  * `scoreboard` — an instance of `Scoreboard`.

* **Controls**

  * Binds arrow keys to snake’s movement methods.

* **Game Loop**

  1. Update screen and pause (`0.1` s).
  2. Move the snake forward.
  3. Detect collision with food → reposition food, grow snake, update score.
  4. Detect collision with walls → end game, display “Game Over”.
  5. Detect collision with snake’s own tail → end game, display “Game Over”.

* **Exit**

  * Waits for a click before closing the window.

---

### `snake.py`

* **Constants**

  * `STARTING_POSITIONS` — initial coordinates for the three-segment snake.
  * `MOVE_DISTANCE` — number of pixels moved per step (20).
  * `UP`, `DOWN`, `LEFT`, `RIGHT` — heading angles in degrees.

* **Class `Snake`**

  1. `__init__`

     * Initializes an empty segment list.
     * Calls `create_snake()` to build the initial snake.
     * Sets `self.head` to the first segment.
  2. `create_snake()`

     * Iterates through `STARTING_POSITIONS` and calls `add_segment()`.
  3. `add_segment(position)`

     * Creates a white square `Turtle` at the given position, adds it to `self.segments`.
  4. `move()`

     * Moves each segment to the position of its predecessor (reverse order).
     * Moves the head forward by `MOVE_DISTANCE`.
  5. Direction methods (`up()`, `down()`, `left()`, `right()`)

     * Change the head’s heading if it is not directly opposite the current direction.
  6. `extend()`

     * Adds a new segment at the position of the last segment, increasing the snake’s length.

---

### `food.py`

* **Class `Food` (inherits from `Turtle`)**

  1. `__init__`

     * Sets the shape to a small green circle.
     * Calls `refresh()` to place the food at a random location.
  2. `refresh()`

     * Generates random `x` and `y` coordinates within ±280 pixels.
     * Moves the food to the new location.

---

### `scoreboard.py`

* **Constants**

  * `ALIGNMENT` — text alignment (“center”).
  * `FONT` — font settings (`Arial`, size 20, normal weight).

* **Class `Scoreboard` (inherits from `Turtle`)**

  1. `__init__`

     * Initializes score to zero, sets pen to white and hidden.
     * Moves to the top of the screen (y = 270) and writes the initial score.
  2. `update_scoreboard()`

     * Clears previous text and writes the updated score.
  3. `increase_score()`

     * Increments `self.score` by one, clears old text, and updates display.
  4. `game_over()`

     * Moves to the center (0, 0) and writes “GAME OVER”.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit with clear messages.
4. Push to your fork and open a Pull Request.