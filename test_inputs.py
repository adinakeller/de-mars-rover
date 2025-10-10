from inputs import Input

def test_changes_grid_input_to_int_tuple():
    assert Input.parse_plateau("5 5") == (5, 5)
    assert Input.parse_plateau("PLATEAU0x0") == (0, 0)

def test_converts_starting_input_to_tuple():
    assert Input.parse_rover("5 5 N") == (5, 5, 'N')

def test_converts_input_to_instructions_list():
    assert Input.parse_instructions('LMLMR') == ['L', 'M', 'L', 'M', 'R']

