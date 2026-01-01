from input.inputs import Input
from rover.rover_starting_point import Rover, Position
from models.the_plateau import Plateau

print("Welcome to Mars Rover!")
print("To end the program enter 'exit'")

def main():
    grid = Input.parse_plateau(input("Plateau Size (e.g 5 5): "))
    plateau = Plateau(grid) 
        
    position = Input.parse_rover(input("Rover Position (e.g 1 4 N): "))
    rover = Rover(position)
  
    print('\nStarting points:')
    print(plateau)
    print(rover)
  
    instructions = Input.parse_instructions(input("\nInstructions (e.g LMRML): ")) 
    for inst in instructions:
        new_position = rover.instruction(inst)
    print(f'\nRover moved to {new_position}')

if __name__ == "__main__":
    main()
    