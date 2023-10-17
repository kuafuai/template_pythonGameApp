import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.zombies = []
        self.ip_file = "ip.txt"

    def scan_zombies(self):
        with open(self.ip_file, "r") as file:
            for line in file:
                self.zombies.append(line.strip())

    def launch_ddos_attack(self):
        for zombie in self.zombies:
            # TODO: Implement DDoS attack logic for each zombie
            pass

game = Game()
game.scan_zombies()
game.launch_ddos_attack()