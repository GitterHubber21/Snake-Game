import pygame
import random
import time

pygame.init()

DIS_WIDTH = 800
DIS_HEIGHT = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (50, 153, 213)
BLACK = (0, 0, 0)

snake_block = 10
snake_speed = 30

apple_size = 20
apple_pixel_size = 4

x1 = DIS_WIDTH / 2
y1 = DIS_HEIGHT / 2
x1_change = 0
y1_change = 0
snake_body = [(x1, y1)]
max_snake_length = 20

font_style = pygame.font.SysFont("Arial", 50)


def message(msg, color):
    dis.fill(BLACK)
    text = font_style.render(msg, True, color)
    dis.blit(text, [DIS_WIDTH / 2 - 100, DIS_HEIGHT / 2 - 25])


def draw_apple(x, y):
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
            if color:
                pygame.draw.rect(dis, color, [
                    x + col * apple_pixel_size,
                    y + row * apple_pixel_size,
                    apple_pixel_size,
                    apple_pixel_size
                ])


dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

last_spawn_time = time.time()
apple_x = random.randint(0, DIS_WIDTH - apple_size)
apple_y = random.randint(0, DIS_HEIGHT - apple_size)

game_over = False
you_won = False

while not game_over and not you_won:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                x1_change = -snake_block
                y1_change = 0
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                x1_change = snake_block
                y1_change = 0
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                x1_change = 0
                y1_change = snake_block
            elif event.key in [pygame.K_UP, pygame.K_w]:
                x1_change = 0
                y1_change = -snake_block

    current_time = time.time()
    if current_time - last_spawn_time >= 3:
        apple_x = random.randint(0, DIS_WIDTH - apple_size)
        apple_y = random.randint(0, DIS_HEIGHT - apple_size)
        last_spawn_time = current_time

    if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    snake_head = (x1, y1)
    snake_body.append(snake_head)

    if apple_x <= x1 < apple_x + apple_size and apple_y <= y1 < apple_y + apple_size:
        apple_x = random.randint(0, DIS_WIDTH - apple_size)
        apple_y = random.randint(0, DIS_HEIGHT - apple_size)
    else:
        snake_body.pop(0)

    if len(snake_body) > 1 and snake_head in snake_body[:-1]:
        game_over = True

    if len(snake_body) >= max_snake_length:
        you_won = True

    dis.fill(LIGHTBLUE)

    for segment in snake_body:
        pygame.draw.rect(dis, BLUE, [segment[0], segment[1], snake_block, snake_block])

    draw_apple(apple_x, apple_y)

    pygame.display.update()
    clock.tick(snake_speed)

if you_won:
    message("You won", GREEN)
else:
    message("You lost", RED)

pygame.display.update()
time.sleep(1)
pygame.quit()
quit()
