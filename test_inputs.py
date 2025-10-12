import pytest # type: ignore
from inputs import Input

def test_returns_message_if_any_input_is_empty():
    assert Input.parse_plateau('') == 'Please enter a plateau size'
    assert Input.parse_rover('') == 'Please enter a starting point'
    assert Input.parse_instructions('') == 'Please enter instructions'


def test_changes_grid_input_to_int_tuple():
    assert Input.parse_plateau("5 5") == (5, 5)
    assert Input.parse_plateau("PLATEAU0x0") == (0, 0)

def test_converts_starting_input_to_tuple():
    assert Input.parse_rover("5 5 N") == (5, 5, 'N')

def test_raises_error_if_invalid_compass_point():
    with pytest.raises(ValueError, match="Invalid direction: Q"):
        Input.parse_rover("1 2 Q")


def test_converts_input_to_instructions_list():
    assert Input.parse_instructions('LMLMR') == ['L', 'M', 'L', 'M', 'R']
    assert Input.parse_instructions('LTRBM') == ['L', 'R', 'M']
    
