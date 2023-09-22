# Utility functions for the game
import pygame

def load_image(image_path):
    image = pygame.image.load(image_path)
    return image.convert_alpha()
