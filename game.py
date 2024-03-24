import pygame
import random

# 游戏类，用于管理游戏的整个过程
class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.cell_size = 20
        self.direction = "RIGHT"
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    # 开始游戏的方法，包括初始化地图、蛇和食物，以及进入游戏循环
    def start(self):
        self.init_map()
        self.init_snake()
        self.init_food()

        while not self.game_over:
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)

    # 初始化地图的方法，创建一个N行M列的二维数组表示地图
    def init_map(self):
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.map = [[0] * self.cols for _ in range(self.rows)]

    # 初始化蛇的方法，创建一个初始长度为1的蛇，并随机放置在地图上的某个位置
    def init_snake(self):
        self.snake = [(self.cols // 2, self.rows // 2)]
        self.map[self.rows // 2][self.cols // 2] = 1

    # 初始化食物的方法，随机在地图上的一个空白方格上放置食物
    def init_food(self):
        while True:
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            if self.map[y][x] == 0:
                self.food = (x, y)
                self.map[y][x] = -1
                break

    # 更新游戏状态的方法，包括蛇的移动、吃食物、判断游戏失败等
    def update(self):
        self.move_snake()
        self.eat_food()
        self.check_collision()

    # 绘制游戏界面的方法，包括地图、蛇和食物的绘制
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_map()
        self.draw_snake()
        self.draw_food()
        self.draw_score()

    # 检查蛇是否与墙壁或自身发生碰撞的方法
    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= self.cols or head[1] < 0 or head[1] >= self.rows:
            self.game_over = True
        elif self.map[head[1]][head[0]] == 1:
            self.game_over = True

    # 游戏失败后的处理方法，弹出游戏失败窗口并提供重新开始和退出游戏的选项
    def game_over(self):
        self.game_over = True
        self.draw_game_over()
        pygame.display.flip()
        while self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        self.quit_game()

    # 重新开始游戏的方法，重新初始化地图、蛇和食物，并进入游戏循环
    def restart_game(self):
        self.init_map()
        self.init_snake()
        self.init_food()
        self.game_over = False
        self.start()

    # 退出游戏的方法，关闭程序
    def quit_game(self):
        pygame.quit()

    # 处理键盘事件的方法，根据按下的方向键来改变蛇的移动方向
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != "DOWN":
                self.direction = "UP"
            elif event.key == pygame.K_DOWN and self.direction != "UP":
                self.direction = "DOWN"
            elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                self.direction = "RIGHT"

    # 移动蛇的方法，根据当前的移动方向来更新蛇的位置
    def move_snake(self):
        head = self.snake[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "LEFT":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 1, head[1])
        self.snake.insert(0, new_head)
        self.map[new_head[1]][new_head[0]] = 1
        if not self.eat_food():
            tail = self.snake.pop()
            self.map[tail[1]][tail[0]] = 0

    # 吃食物的方法，判断蛇是否与食物发生碰撞，如果是则增加蛇的长度并重新放置食物
    def eat_food(self):
        head = self.snake[0]
        if head == self.food:
            self.score += 1
            self.init_food()
            return True
        return False

    # 绘制地图的方法，根据地图数组来绘制地图的方格
    def draw_map(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.map[row][col] == 0:
                    color = (255, 255, 255)
                elif self.map[row][col] == 1:
                    color = (0, 255, 0)
                elif self.map[row][col] == -1:
                    color = (255, 0, 0)
                pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    # 绘制蛇的方法，根据蛇的位置来绘制蛇的身体
    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0] * self.cell_size, segment[1] * self.cell_size, self.cell_size, self.cell_size))

    # 绘制食物的方法，根据食物的位置来绘制食物的图标
    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0] * self.cell_size, self.food[1] * self.cell_size, self.cell_size, self.cell_size))

    # 绘制游戏失败窗口的方法，显示游戏失败的原因，并提供重新开始和退出游戏的选项
    def draw_game_over(self):
        text = self.font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        text = self.font.render("Press R to restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(text, text_rect)
        text = self.font.render("Press Q to quit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 100))
        self.screen.blit(text, text_rect)

    # 绘制分数的方法
    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

# 创建游戏对象并开始游戏
game = Game()
game.start()
