from enums import CompassDirection, Instruction
from dataclasses import dataclass
from the_plateau import Plateau, PlateauSize

# NORTH - WEST - SOUTH - EAST - NORTH

class Rover:
    def __init__(self, position):
        self.position = position
        self.plateau = None

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
        
    def is_plateau(self, plateau):
        self.plateau = Plateau(PlateauSize(width=0, height=0))

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

        if self.plateau:
            if x > self.plateau.width or y > self.plateau.height:
                raise ValueError('coordinates exceed plateau bounds')
        return x, y

    def instruction(self, instruction: Instruction):
        if instruction == Instruction.LEFT:
            return self.rotate_left()
        elif instruction == Instruction.RIGHT:
            return self.rotate_right()
        elif instruction == Instruction.MOVE:
            return self.move_forward()


    def __str__(self):
        return f'Rover: {self.position}'
        
@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection

# where to check that x, y doesnt exceed grid size?