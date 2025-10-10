from the_plateau import Input

def test_changes_grid_input_to_int_tuple():
    string_input = Input()
    output = string_input.plateau_grid("5 5")
    assert output == (5, 5)

    string_input2 = Input()
    output = string_input2.plateau_grid("PLATEAU5x5")
    assert output == (5, 5)

def test_converts_starting_input_to_tuple():
    string_input = Input()
    output = string_input.rover_start("5 5 N")
    assert output == (5, 5, 'N')



