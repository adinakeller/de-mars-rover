from models.the_plateau import PlateauSize
from rover.rover_starting_point import Position
from models.enums import CompassDirection

def test_plateau_has_correct_grid_numbers():
    grid = PlateauSize(width=1, height=2)

    assert grid.width == 1
    assert grid.height == 2

def test_plateau_values_are_int():
    grid = PlateauSize(width=1, height=2)

    assert isinstance(grid.width, int)
    assert isinstance(grid.height, int)

def test_position_has_correct_numbers_and_direction():
    compass_direction = CompassDirection('N')
    position = Position(x=1, y=2, direction=compass_direction)

    assert position.x == 1
    assert position.y == 2
    assert position.direction == CompassDirection.NORTH

def test_position_data_types_are_correct():
    compass_direction = CompassDirection('N')
    position = Position(x=1, y=2, direction=compass_direction)

    assert isinstance(position.x, int)
    assert isinstance(position.y, int)
    assert isinstance(position.direction, CompassDirection)