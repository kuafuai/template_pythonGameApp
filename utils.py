import random

def generate_food(window_width, window_height, snake_body):
    # Generate the position of the food on the window
    while True:
        food = (
            random.randint(0, window_width - 10),
            random.randint(0, window_height - 10),
        )
        if not collides_with_snake(food, snake_body):
            return food

def collides_with_snake(position, snake_body):
    # Check if the position collides with the snake's body
    for segment in snake_body:
        if position == segment:
            return True
    return False