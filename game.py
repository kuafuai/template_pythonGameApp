import pygame
import random
import sys

class Snake:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.body = [(x, y)]

    def move(self):
        if self.direction == "UP":
            self.y -= 1
        elif self.direction == "DOWN":
            self.y += 1
        elif self.direction == "LEFT":
            self.x -= 1
        elif self.direction == "RIGHT":
            self.x += 1

        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop(0)

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def eat_food(self):
        self.length += 1

    def check_collision(self):
        if self.x < 0 or self.x >= 20 or self.y < 0 or self.y >= 20:
            return True

        for i in range(len(self.body) - 1):
            if self.body[i] == (self.x, self.y):
                return True

        return False

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (x * 20, y * 20, 20, 20))

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x * 20, self.y * 20, 20, 20))

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x * 20, self.y * 20, 20, 20))

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        self.snake = Snake(10, 10, 1, "RIGHT")
        self.food = Food(5, 5)
        self.score = 0
        self.obstacle = Obstacle(15, 15)

    def start(self):
        running = True
        while running:
            self.clock.tick(10)
            self.handle_events()
            self.update()
            self.draw()

            if self.snake.check_collision():
                self.game_over()
                running = False

    def restart(self):
        self.snake = Snake(10, 10, 1, "RIGHT")
        self.food = Food(5, 5)
        self.score = 0
        self.obstacle = Obstacle(15, 15)

    def update(self):
        self.snake.move()

        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.eat_food()
            self.score += 1
            self.food = Food(random.randint(0, 19), random.randint(0, 19))

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        self.obstacle.draw(self.surface)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def game_over(self):
        print("Game Over")

game = Game()
game.start()