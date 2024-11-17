import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions and colors
DIS_WIDTH = 800
DIS_HEIGHT = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Snake settings
snake_block = 10
snake_speed = 30

# Apple settings
apple_size = 20
apple_pixel_size = 4  # Each "pixel" in the apple is 4x4 pixels (5x5 grid)

# Initialize variables
x1 = DIS_WIDTH / 2
y1 = DIS_HEIGHT / 2
x1_change = 0
y1_change = 0
snake_body = [(x1, y1)]  # Snake starts with one block
max_snake_length = 20  # Length required to win

# Font setup
font_style = pygame.font.SysFont("Arial", 50)


# Function to display a message on the screen
def message(msg, color):
    dis.fill(BLACK)  # Change the background to black
    text = font_style.render(msg, True, color)
    dis.blit(text, [DIS_WIDTH / 2 - 100, DIS_HEIGHT / 2 - 25])


# Function to draw the apple as pixel art
def draw_apple(x, y):
    # Define the apple design using a grid of colors
    apple_design = [
        [0, 0, GREEN, 0, 0],
        [0, 0, GREEN, 0, 0],
        [0, RED, RED, RED, 0],
        [0, RED, RED, RED, 0],
        [0, RED, RED, RED, 0],
    ]

    for row in range(5):
        for col in range(5):
            color = apple_design[row][col]
            if color:  # Only draw if the color is not 0
                pygame.draw.rect(dis, color, [
                    x + col * apple_pixel_size,
                    y + row * apple_pixel_size,
                    apple_pixel_size,
                    apple_pixel_size
                ])


# Initialize game screen
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Timer for spawning the apple
last_spawn_time = time.time()
apple_x = random.randint(0, DIS_WIDTH - apple_size)
apple_y = random.randint(0, DIS_HEIGHT - apple_size)

# Game loop
game_over = False
you_won = False

while not game_over and not you_won:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # Allow movement with both arrow keys and WASD keys
            if event.key in [pygame.K_LEFT, pygame.K_a] and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key in [pygame.K_RIGHT, pygame.K_d] and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key in [pygame.K_DOWN, pygame.K_s] and y1_change == 0:
                x1_change = 0
                y1_change = snake_block
            elif event.key in [pygame.K_UP, pygame.K_w] and y1_change == 0:
                x1_change = 0
                y1_change = -snake_block

    # Check if it's time to spawn a new apple
    current_time = time.time()
    if current_time - last_spawn_time >= 3:
        apple_x = random.randint(0, DIS_WIDTH - apple_size)
        apple_y = random.randint(0, DIS_HEIGHT - apple_size)
        last_spawn_time = current_time

    # Check for collisions with walls
    if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
        game_over = True

    # Update the snake's position
    x1 += x1_change
    y1 += y1_change
    snake_head = (x1, y1)
    snake_body.append(snake_head)

    # Check if the snake eats the apple
    if apple_x <= x1 < apple_x + apple_size and apple_y <= y1 < apple_y + apple_size:
        apple_x = random.randint(0, DIS_WIDTH - apple_size)
        apple_y = random.randint(0, DIS_HEIGHT - apple_size)
    else:
        # Remove the last block of the snake's tail if no collision
        snake_body.pop(0)

    # Check for collision with itself
    if len(snake_body) > 1 and snake_head in snake_body[:-1]:
        game_over = True

    # Check for win condition
    if len(snake_body) >= max_snake_length:
        you_won = True

    # Render everything
    dis.fill(LIGHTBLUE)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(dis, BLUE, [segment[0], segment[1], snake_block, snake_block])

    # Draw the apple
    draw_apple(apple_x, apple_y)

    pygame.display.update()
    clock.tick(snake_speed)

# Display win or lose message
if you_won:
    message("You won", GREEN)
else:
    message("You lost", RED)

pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
