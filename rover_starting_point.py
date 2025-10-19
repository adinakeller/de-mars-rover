from enums import CompassDirection
from dataclasses import dataclass

class Rover:
    def __init__(self, position):
        self.position = position

    def __str__(self):
        return f'Rover: {self.position}'
        
@dataclass
class Position:
    x = int
    y = int
    direction = CompassDirection