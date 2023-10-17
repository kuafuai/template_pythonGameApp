# Import necessary modules
import pygame
from game import Game

# Initialize the game
def main():
    try:
        pygame.init()
        game = Game()
        game.scan_zombies()
        game.launch_ddos_attack()
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
