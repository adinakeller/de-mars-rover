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
  
    print('\nStarting points:')
    print(plateau)
    print(rover)
  
    instructions = Input.parse_instructions(input("\nInstructions (e.g LMRML): ")) 
    move_rover = rover.instruction(instructions)
    print(f'\nRover moved to {move_rover}')

if __name__ == "__main__":
    main()
    