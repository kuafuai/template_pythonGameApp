import pygame
import random

# Implement all specific logic of the game
class Game:
    def __init__(self):
        pygame.init()
        pass

class SnakeGame(Game):
    def __init__(self):
        super().__init__()
        self.snake = Snake(10, 10)
        self.food = Food(20, 20)
        self.score = Score()
        self.settings = GameSettings()
        self.game_ui = GameUI()

    def start(self):
        while True:
            self.draw()
            self.update_snake()
            self.check_collision()
            self.eat_food()
            self.update_score()
            if self.snake.is_dead:
                self.game_over()
                break

    def draw(self):
        self.game_ui.update()
        self.game_ui.draw_background()
        self.game_ui.draw_border()
        self.game_ui.draw_snake(self.snake)
        self.game_ui.draw_food(self.food)
        self.game_ui.draw_current_score(self.score)

    def update_snake(self):
        self.snake.move()
        self.snake.check_collision()

    def check_collision(self):
        if self.snake.check_collision():
            self.snake.is_dead = True

    def generate_food(self):
        self.food = Food(random.randint(0, self.settings.width - 1), random.randint(0, self.settings.height - 1))

    def eat_food(self):
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.score.increase()
            self.generate_food()

    def update_score(self):
        self.score.draw()

    def game_over(self):
        self.game_ui.draw_game_over()
        self.game_ui.draw_highest_score()

class Snake:
    def __init__(self, x, y):
        self.position = [(x, y)]
        self.direction = "RIGHT"
        self.is_dead = False

    def move(self):
        if self.direction == "UP":
            self.position.insert(0, (self.position[0][0], self.position[0][1] - 1))
        elif self.direction == "DOWN":
            self.position.insert(0, (self.position[0][0], self.position[0][1] + 1))
        elif self.direction == "LEFT":
            self.position.insert(0, (self.position[0][0] - 1, self.position[0][1]))
        elif self.direction == "RIGHT":
            self.position.insert(0, (self.position[0][0] + 1, self.position[0][1]))
        self.position.pop()

    def grow(self):
        self.position.append(self.position[-1])

    def check_collision(self):
        if self.position[0][0] < 0 or self.position[0][0] >= self.settings.width or self.position[0][1] < 0 or self.position[0][1] >= self.settings.height:
            return True
        if self.position[0] in self.position[1:]:
            return True
        return False

class Food:
    def __init__(self, x, y):
        self.position = (x, y)

class Score:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

    def draw(self):
        pass

class GameSettings:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.speed = 1
        self.food_frequency = 5

    def update_speed(self):
        pass

    def update_food_frequency(self):
        pass

class GameUI:
    def __init__(self):
        self.window_size = (800, 600)
        self.background_color = (0, 0, 0)

    def draw_background(self):
        pass

    def draw_border(self):
        pass

    def draw_game_over(self):
        pass

    def draw_highest_score(self):
        pass

    def draw_current_score(self, score):
        pass

    def draw_snake(self, snake):
        pass

    def draw_food(self, food):
        pass

    def update(self):
        pass

class GameController:
    def __init__(self):
        self.game = SnakeGame()
        self.game_ui = GameUI()
        self.game_settings = GameSettings()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)
            self.update_game()
            self.update_game_ui()
            if self.game.snake.is_dead:
                self.game_over()
                break

    def handle_key_event(self, event):
        if event.key == pygame.K_UP:
            self.game.snake.direction = "UP"
        elif event.key == pygame.K_DOWN:
            self.game.snake.direction = "DOWN"
        elif event.key == pygame.K_LEFT:
            self.game.snake.direction = "LEFT"
        elif event.key == pygame.K_RIGHT:
            self.game.snake.direction = "RIGHT"

    def update_game(self):
        self.game.update_snake()
        self.game.check_collision()
        self.game.eat_food()
        self.game.update_score()

    def update_game_ui(self):
        self.game_ui.update()
        self.game_ui.draw_background()
        self.game_ui.draw_border()
        self.game_ui.draw_snake(self.game.snake)
        self.game_ui.draw_food(self.game.food)
        self.game_ui.draw_current_score(self.game.score)

    def game_over(self):
        self.game_ui.draw_game_over()
        self.game_ui.draw_highest_score()

if __name__ == "__main__":
    game_controller = GameController()
    game_controller.start()
