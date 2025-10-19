from enums import Instruction, CompassDirection

class Input:
    def parse_plateau(input):
        if input == '':
            return 'Please enter a plateau size'
        
        nums = '0123456789'
        list = [chr for chr in input]
        coordinates = [int(chr) for chr in list if chr in nums]
    
        width = coordinates[0]
        height = coordinates[1]
        return width, height
    
        
    def parse_rover(input):
        if input == '':
            return 'Please enter a starting point'
        
        list = input.split()
        x = int(list[0])
        y = int(list[1])

        try:
            CompassDirection(list[2])
            direction = list[2]
        except ValueError:
            raise ValueError(f'Invalid direction: {list[2]}')
        
        return x, y, direction
    

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
            

# create func that handles all inputs being empty??
# what if rover inputs exceeds grid size??