from dataclasses import dataclass

class Plateau:
    def __init__(self, grid):
        self.grid = grid

@dataclass
class PlateauSize:
    width = int
    height = int


