import pygame
import adb

class Game:
    def __init__(self):
        self.clicker = None

    def add_clicker(self):
        self.clicker = Clicker()

class Clicker:
    def __init__(self):
        self.delay = 0
        self.timer = None

    def connect(self):
        adb.connect()

    def add_click(self, x, y, count):
        adb.click(x, y, count)

    def add_swipe(self, start_x, start_y, end_x, end_y, duration):
        adb.swipe(start_x, start_y, end_x, end_y, duration)

    def set_delay(self, delay):
        self.delay = delay

    def set_timer(self, start_time, end_time):
        self.timer = (start_time, end_time)
