import pygame

class Game:
    def __init__(self):
        # 初始化游戏状态和设置
        pygame.init()
        self.is_running = True
        self.is_paused = False

    def start_game(self):
        # 开始游戏的方法，初始化玩家与AI的状态
        print("Game started.")
        self.is_running = True
        self.is_paused = False
        # 其他初始化代码，例如初始化玩家、AI等

    def pause_game(self):
        # 暂停游戏的方法，更新游戏状态
        if self.is_running and not self.is_paused:
            print("Game paused.")
            self.is_paused = True

    def end_game(self):
        # 结束游戏方法，清理资源和更新统计信息
        print("Game ended.")
        self.is_running = False
        pygame.quit()
