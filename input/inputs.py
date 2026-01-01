from models.enums import Instruction, CompassDirection
from models.the_plateau import PlateauSize
from rover.rover_starting_point import Position

class Input:
    def parse_plateau(user_input=''):
        if user_input == '':
            raise ValueError('Please enter a plateau size. Example 5 5')
        
        coordinates = [int(chr) for chr in user_input if chr.isdigit()]

        if len(coordinates) < 2:
            raise ValueError(f'Invalid input: {coordinates}')
    
        width = coordinates[0]
        height = coordinates[1]
        return PlateauSize(width, height)
    
        
    def parse_rover(user_input=''):
        if user_input == '':
            raise ValueError('Please enter a starting point. Example: 1 4 N')
        
        coord = [item for item in user_input.strip() if item != ' ']
        x = int(coord[0])
        y = int(coord[1])

        try:
            direction = CompassDirection(coord[2])
        except ValueError:
            raise ValueError(f'Invalid direction: {coord[2]}')
        
        return Position(x, y, direction)
    

    def parse_instructions(user_input=''):
        if user_input == '':
            raise ValueError('Please enter instructions. Example: LMLRML')
        
        valid_letters = []
        for chr in user_input:
            try:
                Instruction(chr)
                valid_letters.append(chr)
            except:
                continue
        return valid_letters