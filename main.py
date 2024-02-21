import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    try:
        game.run()
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()