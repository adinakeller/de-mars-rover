from enums import CompassDirection
from dataclasses import dataclass

class Rover:
    def __init__(self, position):
        self.position = position

@dataclass
class Position:
    x = int
    y = int
    direction = CompassDirection