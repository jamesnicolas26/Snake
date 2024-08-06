import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = None
        self.direction = 'Right'
        self.running = True

        self.setup_game()
        self.create_food()
        self.move_snake()
        self.root.bind("<KeyPress>", self.change_direction)

    def setup_game(self):
        self.draw_snake()
        self.draw_food()

    def draw_snake(self):
        self.canvas.delete('snake')
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill='green', tags='snake')

    def draw_food(self):
        if self.food:
            self.canvas.delete('food')
        self.food = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill='red', tags='food')

    def move_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]

        if self.direction == 'Right':
            head_x += 10
        elif self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10

        new_head = (head_x, head_y)

        # Check if the snake has eaten the food
        if new_head == self.food:
            self.snake = [new_head] + self.snake
            self.create_food()
        else:
            self.snake = [new_head] + self.snake[:-1]

        # Check for collisions
        if (head_x < 0 or head_x >= 400 or
            head_y < 0 or head_y >= 400 or
            len(self.snake) != len(set(self.snake))):
            self.running = False
            self.canvas.create_text(200, 200, text="Game Over", fill='white', font=('Arial', 24))

        self.draw_snake()
        self.root.after(100, self.move_snake)

    def change_direction(self, event):
        new_direction = event.keysym
        if new_direction in ['Left', 'Right', 'Up', 'Down']:
            # Prevent the snake from reversing direction
            if (self.direction == 'Left' and new_direction != 'Right' or
                self.direction == 'Right' and new_direction != 'Left' or
                self.direction == 'Up' and new_direction != 'Down' or
                self.direction == 'Down' and new_direction != 'Up'):
                self.direction = new_direction

    def create_food(self):
        self.draw_food()

# Create the main window
root = tk.Tk()
app = SnakeGame(root)
root.mainloop()
