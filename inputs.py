from enums import Instruction, CompassDirection
from the_plateau import PlateauSize
from rover_starting_point import Position

class Input:
    def parse_plateau(input):
        if input == '':
            return 'Please enter a plateau size'
        
        nums = '0123456789'
        list = [chr for chr in input]
        coordinates = [int(chr) for chr in list if chr in nums]
    
        width = coordinates[0]
        height = coordinates[1]
        return PlateauSize(width, height)
    
        
    def parse_rover(input):
        if input == '':
            return 'Please enter a starting point'
        
        coord = input.split()
        x = int(coord[0])
        y = int(coord[1])

        try:
            CompassDirection(coord[2])
            direction = coord[2]
        except ValueError:
            raise ValueError(f'Invalid direction: {coord[2]}')
        
        return Position(x, y, direction)
    

    def parse_instructions(input):
        valid_letters = []
        if input == '':
            return 'Please enter instructions'
        
        for chr in input:
            try:
                Instruction(chr)
                valid_letters.append(chr)
            except:
                continue
        return f'Instructions: {valid_letters}'