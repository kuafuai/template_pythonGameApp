import pygame

class Tutorial:
    def __init__(self):
        self.intro_text = "Welcome to the tutorial! Press H for help."
        self.help_text = "This is a basic tutorial on how to play the game."
    
    def start_tutorial(self):
        print(self.intro_text)
        # Here you can add code to display the tutorial steps
        
    def display_help(self):
        print(self.help_text)
        # Add additional help information as needed
