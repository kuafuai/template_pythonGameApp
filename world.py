class World:
    def __init__(self):
        self.map_size = (10, 10)
        self.terrain = [['grass' for _ in range(self.map_size[1])] for _ in range(self.map_size[0])]
        self.buildings = [['none' for _ in range(self.map_size[1])] for _ in range(self.map_size[0])]

    def get_terrain(self, x, y):
        return self.terrain[x][y]

    def get_building(self, x, y):
        return self.buildings[x][y]

    def set_terrain(self, x, y, terrain):
        self.terrain[x][y] = terrain

    def set_building(self, x, y, building):
        self.buildings[x][y] = building
