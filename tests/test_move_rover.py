from rover_starting_point import Rover, Position, CompassDirection

def test_rotate_left_from_north():
    starting_point = Position(x=1, y=2, direction=CompassDirection('N'))
    rover = Rover(starting_point)
    output = rover.rotate_left()

    assert output == CompassDirection.WEST

def test_rotate_left_from_west():
    starting_point = Position(x=1, y=2, direction=CompassDirection('W'))
    rover = Rover(starting_point)
    output = rover.rotate_left()

    assert output == CompassDirection.SOUTH

def test_rotate_left_from_south():
    starting_point = Position(x=1, y=2, direction=CompassDirection('S'))
    rover = Rover(starting_point)
    output = rover.rotate_left()

    assert output == CompassDirection.EAST

def test_rotate_left_from_east():
    starting_point = Position(x=1, y=2, direction=CompassDirection('E'))
    rover = Rover(starting_point)
    output = rover.rotate_left()

    assert output == CompassDirection.NORTH
    
    