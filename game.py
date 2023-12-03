import pygame
import random

# 游戏屏幕的宽度和高度
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 贪吃蛇的移动速度
SNAKE_SPEED = 20

# 贪吃蛇的移动方向
DIRECTION_UP = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT = 3
DIRECTION_RIGHT = 4

# 游戏状态
GAME_STATE_START = 1
GAME_STATE_OVER = 2


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

    def start(self):
        pass


class SnakeGame(Game):
    def __init__(self):
        super().__init__()
        self.snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.food = Food()
        self.score = 0
        self.state = GAME_STATE_START

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != DIRECTION_DOWN:
                        self.snake.direction = DIRECTION_UP
                    elif event.key == pygame.K_DOWN and self.snake.direction != DIRECTION_UP:
                        self.snake.direction = DIRECTION_DOWN
                    elif event.key == pygame.K_LEFT and self.snake.direction != DIRECTION_RIGHT:
                        self.snake.direction = DIRECTION_LEFT
                    elif event.key == pygame.K_RIGHT and self.snake.direction != DIRECTION_LEFT:
                        self.snake.direction = DIRECTION_RIGHT

            if self.state == GAME_STATE_START:
                self.update_snake()
                self.check_collision()
                self.eat_food()
                self.update_screen()
            elif self.state == GAME_STATE_OVER:
                self.game_over()

            self.clock.tick(10)

    def update_snake(self):
        self.snake.move()

    def check_collision(self):
        if self.snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT) or self.snake.check_collision_with_self():
            self.state = GAME_STATE_OVER

    def generate_food(self):
        while True:
            x = random.randint(0, SCREEN_WIDTH // SNAKE_SPEED - 1) * SNAKE_SPEED
            y = random.randint(0, SCREEN_HEIGHT // SNAKE_SPEED - 1) * SNAKE_SPEED
            if not self.snake.check_collision(x, y):
                return x, y

    def eat_food(self):
        if self.snake.get_head() == self.food.get_position():
            self.snake.grow()
            self.score += 1
            self.food.set_position(*self.generate_food())

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.snake.get_body_surface(), (0, 0))
        self.screen.blit(self.food.get_surface(), self.food.get_position())
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()


class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = DIRECTION_UP

    def move(self):
        x, y = self.body[0]
        if self.direction == DIRECTION_UP:
            y -= SNAKE_SPEED
        elif self.direction == DIRECTION_DOWN:
            y += SNAKE_SPEED
        elif self.direction == DIRECTION_LEFT:
            x -= SNAKE_SPEED
        elif self.direction == DIRECTION_RIGHT:
            x += SNAKE_SPEED

        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[0]
        if self.direction == DIRECTION_UP:
            y -= SNAKE_SPEED
        elif self.direction == DIRECTION_DOWN:
            y += SNAKE_SPEED
        elif self.direction == DIRECTION_LEFT:
            x -= SNAKE_SPEED
        elif self.direction == DIRECTION_RIGHT:
            x += SNAKE_SPEED

        self.body.insert(0, (x, y))

    def check_collision(self, x, y):
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            return True

        for body_part in self.body[1:]:
            if body_part == (x, y):
                return True

        return False

    def check_collision_with_self(self):
        return self.check_collision(*self.body[0])

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def get_length(self):
        return len(self.body)

    def get_body_surface(self):
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surface.fill((0, 0, 0))
        for body_part in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (body_part[0], body_part[1], SNAKE_SPEED, SNAKE_SPEED))
        return surface


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, SCREEN_WIDTH // SNAKE_SPEED - 1) * SNAKE_SPEED
        y = random.randint(0, SCREEN_HEIGHT // SNAKE_SPEED - 1) * SNAKE_SPEED
        return x, y

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = x, y

    def get_surface(self):
        surface = pygame.Surface((SNAKE_SPEED, SNAKE_SPEED))
        surface.fill((255, 0, 0))
        return surface


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

    def draw_snake(self, snake):
        self.screen.blit(snake.get_body_surface(), (0, 0))

    def draw_food(self, food):
        self.screen.blit(food.get_surface(), food.get_position())

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        text_rect = text.get_rect(topright=(self.width - 10, 10))
        self.screen.blit(text, text_rect)

    def clear(self):
        self.screen.fill((0, 0, 0))


def main():
    game = SnakeGame()
    game.start()


if __name__ == "__main__":
    main()
