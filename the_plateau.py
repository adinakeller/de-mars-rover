from dataclasses import dataclass

class Plateau:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        return f'Plateau: {self.grid}'

@dataclass
class PlateauSize:
    width: int
    height: int


