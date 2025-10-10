from the_plateau import Input

def test_changes_input_to_int_type():
    string_input = Input()
    output = string_input.plateau_grid("5 5")
    assert output == (5, 5)

def test_decimal_inputs_rounded_to_nearest_int():
    decimal_input = Input()
    output = decimal_input.plateau_grid('6 5.5')
    assert output == (6, 6)

