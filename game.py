import pygame
import random

# 游戏类
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.is_paused = False
        self.score = 0
        self.high_score = 0
        self.start_button = pygame.Rect(300, 200, 200, 50)
        self.pause_button = pygame.Rect(300, 300, 200, 50)
        self.end_button = pygame.Rect(300, 400, 200, 50)

    def start_game(self):
        self.is_running = True

    def pause_game(self):
        self.is_paused = not self.is_paused

    def end_game(self):
        self.is_running = False

    def update_score(self, score):
        self.score = score
        if score > self.high_score:
            self.high_score = score

# 方块类
class Block:
    def __init__(self):
        self.x = random.randint(0, 9)
        self.y = 0

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def rotate(self):
        pass

# 棋盘类
class Board:
    def __init__(self):
        self.board = [[0] * 10 for _ in range(20)]

    def add_block(self, block):
        self.board[block.y][block.x] = 1

    def remove_block(self, block):
        self.board[block.y][block.x] = 0

    def check_collision(self, block):
        if block.y >= 20:
            return True
        if block.x < 0 or block.x >= 10:
            return True
        if self.board[block.y][block.x] == 1:
            return True
        return False

    def check_complete_lines(self):
        complete_lines = []
        for i in range(20):
            if all(self.board[i]):
                complete_lines.append(i)
        return complete_lines

    def update(self):
        pass

# 界面类
class Interface:
    def __init__(self):
        self.game = Game()
        self.board = Board()

    def draw_board(self):
        self.game.screen.fill((0, 0, 0))
        for y in range(20):
            for x in range(10):
                if self.board.board[y][x] == 1:
                    pygame.draw.rect(self.game.screen, (255, 255, 255), (x * 40, y * 40, 40, 40))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.game.score), True, (255, 255, 255))
        high_score_text = font.render("High Score: " + str(self.game.high_score), True, (255, 255, 255))
        self.game.screen.blit(score_text, (300, 100))
        self.game.screen.blit(high_score_text, (300, 150))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board.current_block.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.board.current_block.move_right()
                elif event.key == pygame.K_DOWN:
                    self.board.current_block.move_down()
                elif event.key == pygame.K_UP:
                    self.board.current_block.rotate()

    def update(self):
        if self.game.is_running:
            if not self.game.is_paused:
                self.board.current_block.move_down()
                if self.board.check_collision(self.board.current_block):
                    self.board.current_block.move_up()
                    self.board.add_block(self.board.current_block)
                    complete_lines = self.board.check_complete_lines()
                    if complete_lines:
                        self.game.update_score(self.game.score + len(complete_lines))
                        for line in complete_lines:
                            self.board.remove_line(line)
                    self.board.current_block = Block()
            self.draw_board()
            self.draw_score()
            pygame.display.flip()
            self.game.clock.tick(30)

interface = Interface()
while interface.game.is_running:
    interface.handle_input()
    interface.update()