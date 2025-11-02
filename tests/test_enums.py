from enums import Instruction, CompassDirection

def test_enum_instructions_has_correct_value():
    assert Instruction('L') == Instruction.LEFT
    assert Instruction('R') == Instruction.RIGHT
    assert Instruction('M') == Instruction.MOVE

def test_reference_instruction():
    assert Instruction('L') is Instruction.LEFT
    assert Instruction('R') is Instruction.RIGHT
    assert Instruction('M') is Instruction.MOVE

def test_enum_compass_directions_has_correct_value():
    assert CompassDirection('N') == CompassDirection.NORTH
    assert CompassDirection('E') == CompassDirection.EAST
    assert CompassDirection('S') == CompassDirection.SOUTH
    assert CompassDirection('W') == CompassDirection.WEST

def test_reference_direction():
    assert CompassDirection('N') is CompassDirection.NORTH
    assert CompassDirection('E') is CompassDirection.EAST
    assert CompassDirection('S') is CompassDirection.SOUTH
    assert CompassDirection('W') is CompassDirection.WEST