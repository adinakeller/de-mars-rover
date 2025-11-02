from enums import CompassDirection
from dataclasses import dataclass

# NORTH - WEST - SOUTH - EAST - NORTH

class Rover:
    def __init__(self, position):
        self.position = position

    def rotate_left(self):
            if self.position.direction == CompassDirection.NORTH:
                self.position.direction = CompassDirection.WEST
            elif self.position.direction == CompassDirection.WEST:
                self.position.direction = CompassDirection.SOUTH
            elif self.position.direction == CompassDirection.SOUTH:
                self.position.direction = CompassDirection.EAST
            else:
                self.position.direction = CompassDirection.NORTH
            return self.position.direction
# refactor!! dont want so manual
    
        
    def __str__(self):
        return f'Rover: {self.position}'
        
@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection