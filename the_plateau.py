class Plateau:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rover:
    def __init__(self, x, y, compass_points):
        self.across = x
        self.up = y
        self.compass_points = compass_points

class Input:
    def plateau_grid(self, input):
        list = input.split()
        width = int(list[0])
        height = int(list[1])
        return width, height
    #print(plateau_grid('5 5'))