from inputs import Input
from rover_starting_point import Rover
from the_plateau import Plateau

print("Welcome to Mars Rover!")
print("To end the program enter 'exit'")

def main():
    grid = Input.parse_plateau(input("Plateau Size (e.g 5 5): "))
    plateau = Plateau(grid) 
        
    position = Input.parse_rover(input("Rover Position (e.g 1 4 N): "))
    rover = Rover(position)

    instructions = Input.parse_instructions(input("Instructions (e.g LMRML): "))   

    print('\nStarting points:')
    print(plateau)
    print(rover)
    print(instructions)

if __name__ == "__main__":
    main()
    