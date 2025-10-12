from inputs import Input
from rover_starting_point import Rover
from the_plateau import Plateau


def main():
    grid = Input.parse_plateau("5 5")
    poisition = Input.parse_rover("1 2 N")
    instructions = Input.parse_instructions("LMLMLMLMM")

    rover = Rover(poisition)
    plateau = Plateau(grid)

    print(plateau)
    print(rover)
    print(instructions)

if __name__ == "__main__":
    main()
    