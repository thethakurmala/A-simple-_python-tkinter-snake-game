import tkinter as tk
import random

WIDTH = 1000
HEIGHT = 800
SNAKE_SIZE = 20
SPEED = 100

def create_food():
    x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    return x, y

def create_snake():
    x = WIDTH // 2
    y = HEIGHT // 2
    return [(x, y), (x - SNAKE_SIZE, y), (x - 2 * SNAKE_SIZE, y)]

def move_snake():
    global snake, food, direction

    head_x, head_y = snake[0]

    if direction == "right":
        new_head = (head_x + SNAKE_SIZE, head_y)
    elif direction == "left":
        new_head = (head_x - SNAKE_SIZE, head_y)
    elif direction == "up":
        new_head = (head_x, head_y - SNAKE_SIZE)
    elif direction == "down":
        new_head = (head_x, head_y + SNAKE_SIZE)
    else:
        return # if no direction, do nothing.

    # Check for collisions with walls
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        game_over()
        return

    # Check for collisions with itself
    if new_head in snake[1:]:
        game_over()
        return

    snake.insert(0, new_head)

    if new_head == food:
        food = create_food()
    else:
        snake.pop()

    canvas.delete(tk.ALL)
    canvas.create_rectangle(food[0], food[1], food[0] + SNAKE_SIZE, food[1] + SNAKE_SIZE, fill="red")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="green")

    window.after(SPEED, move_snake)

def change_direction(new_direction):
    global direction
    if (new_direction == "right" and direction != "left") or \
       (new_direction == "left" and direction != "right") or \
       (new_direction == "up" and direction != "down") or \
       (new_direction == "down" and direction != "up"):
        direction = new_direction

def game_over():
    global snake, food, direction
    canvas.delete(tk.ALL)
    canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over!", fill="white", font=("Helvetica", 20))
    snake = create_snake()
    food = create_food()
    direction = "right"
    window.after(2000, start_new_game)

def start_new_game():
    move_snake()

window = tk.Tk()
window.title("Snake Game")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = create_snake()
food = create_food()
direction = "right"

move_snake()

window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

window.mainloop()