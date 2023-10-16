import pygame
from utils import generate_food

class Game:
    def __init__(self, window_width, window_height):
        # Initialize game variables
        self.window_width = window_width
        self.window_height = window_height
        self.snake = Snake()
        self.food = generate_food(self.window_width, self.window_height)
        self.score = 0
        self.game_over_flag = False

    def handle_events(self, key):
        # Handle keyboard events to update snake direction
        if key == pygame.K_UP:
            self.snake.change_direction("up")
        elif key == pygame.K_DOWN:
            self.snake.change_direction("down")
        elif key == pygame.K_LEFT:
            self.snake.change_direction("left")
        elif key == pygame.K_RIGHT:
            self.snake.change_direction("right")

    def update(self):
        # Update game state
        if not self.game_over_flag:
            self.snake.move()
            if self.snake.collides_with_food(self.food):
                self.snake.grow()
                self.score += 1
                self.food = generate_food(self.window_width, self.window_height)
            if self.snake.collides_with_boundary(self.window_width, self.window_height):
                self.game_over()

    def draw(self, window):
        # Draw game objects on the window
        window.fill((0, 0, 0))
        self.snake.draw(window)
        pygame.draw.rect(window, (255, 0, 0), (self.food[0], self.food[1], 10, 10))
        self.draw_score(window)
        if self.game_over_flag:
            self.draw_game_over(window)

    def draw_score(self, window):
        # Draw the player's score on the window
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        window.blit(text, (10, 10))

    def draw_game_over(self, window):
        # Draw the game over screen
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.window_width/2, self.window_height/2))
        window.blit(text, text_rect)

    def game_over(self):
        # Set the game over flag
        self.game_over_flag = True

class Snake:
    def __init__(self):
        # Initialize snake variables
        self.direction = "right"
        self.body = [(100, 100), (90, 100), (80, 100)]

    def change_direction(self, direction):
        # Change snake direction
        self.direction = direction

    def move(self):
        # Move the snake in the current direction
        head = self.body[0]
        if self.direction == "up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "down":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "right":
            new_head = (head[0] + 10, head[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def collides_with_food(self, food):
        # Check if the snake collides with the food
        head = self.body[0]
        return head[0] == food[0] and head[1] == food[1]

    def grow(self):
        # Increase the length of the snake
        tail = self.body[-1]
        self.body.append(tail)

    def collides_with_boundary(self, window_width, window_height):
        # Check if the snake collides with the boundaries of the window
        head = self.body[0]
        return (
            head[0] < 0
            or head[0] >= window_width
            or head[1] < 0
            or head[1] >= window_height
        )

    def draw(self, window):
        # Draw the snake on the window
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), (segment[0], segment[1], 10, 10))