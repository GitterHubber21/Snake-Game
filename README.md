# 🐍 Snake Game with Pixel-Art Apple 🍎

Welcome to the **Snake Game** project! This is a classic snake game built with Python and Pygame, featuring a pixel-art **apple** 🍏 and support for both **arrow keys** and **WASD controls** 🎮. 


---
## 🎮 Controls

You can control the snake using either the **Arrow Keys** or the **WASD Keys**.

| Key            | Action                   |
|----------------|--------------------------|
| **Up Arrow** | Move the snake up            |
| **Down Arrow** | Move the snake down         |
| **Left Arrow** |  Move the snake left          |
| **Right Arrow** |  Move the snake right          |
| **W Key**       | Move the snake up         |
| **A Key**       | Move the snake left       |
| **S Key**       | Move the snake down       |
| **D Key**       | Move the snake right      |

## 🛠️ How It Works

### 1. **Snake Movement** 🐍
- The snake moves in a grid-like fashion, where each move corresponds to a fixed block size.
- You control the snake's direction using the **Arrow Keys** or **WASD Keys**. 
- The snake cannot reverse direction, so it will only move in the direction it’s currently heading (e.g., you can't turn around immediately from left to right).

### 2. **Pixel-Art Apple** 🍏
- The apple is drawn using a grid of **red** and **green** squares to create a simple retro look.
- The snake must "eat" the apple by moving to the same position as the apple.
- Every time the snake eats an apple, it grows in size, making the game harder to control.

### 3. **Win and Lose Conditions** 🎯
- **Win Condition**: The game ends with a victory message when the snake reaches a length of **20 blocks**. 🎉
- **Lose Condition**: The game ends with a game-over message if the snake collides with the wall. 💥

### 4. **Background Color Change** 🎨
- When the player wins or loses, the background color changes to **black** for a dramatic effect. 
- A message like **"You won!"** or **"You lost!"** is displayed on the screen in a contrasting color (green for win, red for loss).

### 5. **Game Over and Restart** ⚠️
- After a game over, the game automatically displays a message (e.g., "You lost") and waits for a few seconds before closing.
- You can always restart the game by running the script again.

### 6. **Game Loop** 🔄
- The game continuously checks for user input (key presses) to change the snake's direction.
- The snake is drawn on the screen with each frame, updating its position based on the direction it’s moving.
- The game runs in a loop until the player either wins or loses.



