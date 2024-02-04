import pygame
from game import Game

def main():
    # 创建游戏对象
    game = Game()

    # 初始化Pygame
    pygame.init()

    # 设置窗口标题
    pygame.display.set_caption("My Game")

    # 设置窗口尺寸
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 游戏主循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 渲染画面
        screen.fill((255, 255, 255))
        game.draw(screen)
        pygame.display.flip()

    # 退出Pygame
    pygame.quit()

def add_clicker(self):
    # 添加连点器功能的代码
    pass

if __name__ == "__main__":
    main()
