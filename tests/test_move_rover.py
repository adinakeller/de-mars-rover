from rover_starting_point import Rover, Position, CompassDirection, Instruction
from the_plateau import Plateau, PlateauSize
import pytest

class TestRotateLeft:
    def test_rotate_left_from_north(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('N'))
        rover = Rover(starting_point)
        output = rover.rotate_left()

        assert output == CompassDirection.WEST

    def test_rotate_left_from_west(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('W'))
        rover = Rover(starting_point)
        output = rover.rotate_left()

        assert output == CompassDirection.SOUTH

    def test_rotate_left_from_south(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('S'))
        rover = Rover(starting_point)
        output = rover.rotate_left()

        assert output == CompassDirection.EAST

    def test_rotate_left_from_east(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('E'))
        rover = Rover(starting_point)
        output = rover.rotate_left()

        assert output == CompassDirection.NORTH
    
class TestRotateRight: 
    def test_rotate_right_from_north(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('N'))
        rover = Rover(starting_point)
        output = rover.rotate_right()

        assert output == CompassDirection.EAST

    def test_rotate_right_from_east(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('E'))
        rover = Rover(starting_point)
        output = rover.rotate_right()

        assert output == CompassDirection.SOUTH

    def test_rotate_right_from_south(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('S'))
        rover = Rover(starting_point)
        output = rover.rotate_right()

        assert output == CompassDirection.WEST

    def test_rotate_right_from_west(self):
        starting_point = Position(x=1, y=2, direction=CompassDirection('W'))
        rover = Rover(starting_point)
        output = rover.rotate_right()

        assert output == CompassDirection.NORTH

class TestMoveForward:
    def test_move_forward_north(self):
        starting_point = Position(x=2, y=4, direction=CompassDirection('N'))
        rover = Rover(starting_point)
        output = rover.move_forward()

        assert output == (2, 5)

    def test_move_forward_west(self):
        starting_point = Position(x=2, y=4, direction=CompassDirection('W'))
        rover = Rover(starting_point)
        output = rover.move_forward()

        assert output == (1, 4)

    def test_move_forward_south(self):
        starting_point = Position(x=2, y=4, direction=CompassDirection('S'))
        rover = Rover(starting_point)
        output = rover.move_forward()

        assert output == (2, 3)

    def test_move_forward_east(self):
        starting_point = Position(x=2, y=4, direction=CompassDirection('E'))
        rover = Rover(starting_point)
        output = rover.move_forward()

        assert output == (3, 4)

    def test_raises_error_when_movement_exceeds_grid(self):
        p = Plateau(PlateauSize(5, 5))
        starting_point = Position(x=6, y=6, direction=CompassDirection('E'))
        rover = Rover(starting_point)
        rover.is_plateau(p)
    
        with pytest.raises(ValueError, match="coordinates exceed plateau bounds"):
            rover.move_forward()


class TestInstructions:
    def test_instruction_L(self):
        starting_point = Position(x=3, y=3, direction=CompassDirection('E'))
        rover = Rover(starting_point)
        output = rover.instruction(Instruction('L'))

        assert output == (3, 3, 'N')

    def test_instruction_R(self):
        starting_point = Position(x=3, y=3, direction=CompassDirection('S'))
        rover = Rover(starting_point)
        output = rover.instruction(Instruction('R'))

        assert output == (3, 3, 'W')

    def test_instruction_M(self):
        starting_point = Position(x=3, y=3, direction=CompassDirection('S'))
        rover = Rover(starting_point)
        output = rover.instruction(Instruction('M'))

        assert output == (3, 2, 'S')
