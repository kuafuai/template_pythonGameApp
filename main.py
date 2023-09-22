# Import necessary modules
import pygame
from src.game import Game

# Initialize the game
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Create a new game instance
game = Game(screen)

# Start the game
game.run()

# Quit the game
pygame.quit()
