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
        nums = '0123456789'
        list = [chr for chr in input]
        coordinates = []
        for chr in list:
            if chr in nums:
                coordinates.append(int(chr))
        width = coordinates[0]
        height = coordinates[1]
        return width, height
    # print(plateau_grid("PLATEAU5x5"))
    # print(plateau_grid("5 5"))   
        

    def rover_start(self, input):
        list = input.split()
        x = int(list[0])
        y = int(list[1])
        compass = list[2]
        return x, y, compass
    #print(rover_start('5 5 N'))

    