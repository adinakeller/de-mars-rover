from dataclasses import dataclass

@dataclass
class PlateauSize:
    width: int
    height: int

class Plateau:
    def __init__(self, grid: PlateauSize):
        self.grid = grid
        self.width = grid.width
        self.height = grid.height

    def __str__(self):
        return f'Plateau: {self.grid}'



