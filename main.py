import pygame
from game import Game

def main():
    """
    Function to initialize and run the game.
    """
    try:
        pygame.init()
        game = Game()
        game.run()
    except Exception as e:
        print("An error occurred during game execution:", str(e))

if __name__ == "__main__":
    main()