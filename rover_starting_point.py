from enums import CompassDirection
from dataclasses import dataclass
from enums import Instruction

# NORTH - WEST - SOUTH - EAST - NORTH

class Rover:
    def __init__(self, position):
        self.position = position

    def rotate_left(self):
        directions_dict = {
            CompassDirection.NORTH: CompassDirection.WEST,
            CompassDirection.WEST: CompassDirection.SOUTH,
            CompassDirection.SOUTH: CompassDirection.EAST, 
            CompassDirection.EAST: CompassDirection.NORTH
        }
        self.position.direction = directions_dict[self.position.direction]
        return self.position.direction

    def rotate_right(self):
        directions_dict = {
            CompassDirection.NORTH: CompassDirection.EAST,
            CompassDirection.EAST: CompassDirection.SOUTH,
            CompassDirection.SOUTH: CompassDirection.WEST, 
            CompassDirection.WEST: CompassDirection.NORTH
        }
        self.position.direction = directions_dict[self.position.direction]
        return self.position.direction
        
    def move_forward(self):
        x = self.position.x 
        y = self.position.y
        coordinates_dict = {
            CompassDirection.NORTH: (x, y + 1),
            CompassDirection.WEST: (x - 1, y),
            CompassDirection.SOUTH: (x, y - 1),
            CompassDirection.EAST: (x + 1, y)
        }
        x, y = coordinates_dict[self.position.direction]
        return x, y

    def __str__(self):
        return f'Rover: {self.position}'
        
@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection