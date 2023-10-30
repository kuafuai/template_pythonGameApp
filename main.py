# Import necessary modules
import pygame
from game import Game

# Initialize the game
def main():
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
