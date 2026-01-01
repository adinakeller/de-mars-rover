import pytest # type: ignore
from input.inputs import Input
from models.the_plateau import PlateauSize
from rover.rover_starting_point import Position, CompassDirection

def test_returns_error_message_if_any_input_is_empty():
    with pytest.raises(ValueError, match="Please enter a plateau size. Example 5 5"):
        Input.parse_plateau("")

    with pytest.raises(ValueError, match="Please enter a starting point. Example: 1 4 N"):
        Input.parse_rover("")

    with pytest.raises(ValueError, match="Please enter instructions. Example: LMLRML"):
        Input.parse_instructions("")


def test_changes_grid_input_to_int_tuple():
    assert Input.parse_plateau("5 5") == PlateauSize(5, 5)
    assert Input.parse_plateau("PLATEAU0x0") == PlateauSize(0, 0)

def test_converts_starting_input_to_tuple():
    position = Input.parse_rover("5 5 N") 
    assert position == Position(5, 5, CompassDirection('N'))

def test_raises_error_if_invalid_compass_point():
    with pytest.raises(ValueError, match="Invalid direction: Q"):
        Input.parse_rover("1 2 Q")


def test_converts_input_to_instructions_list():
    assert Input.parse_instructions('LMLMR') == ['L', 'M', 'L', 'M', 'R']
    assert Input.parse_instructions('LTRBM') == ['L', 'R', 'M']
    
