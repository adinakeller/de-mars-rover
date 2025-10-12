from enums import Instruction, CompassDirection

class Input:
    def parse_plateau(input):
        nums = '0123456789'
        list = [chr for chr in input]
        coordinates = []
        for chr in list:
            if chr in nums:
                coordinates.append(int(chr))
        width = coordinates[0]
        height = coordinates[1]
        return width, height
    #print(parse_plateau("PLATEAU0x0"))
    #print(parse_plateau("5 5"))   
        

    def parse_rover(input):
        list = input.split()
        x = int(list[0])
        y = int(list[1])

        try:
            CompassDirection(list[2])
            direction = list[2]
        except ValueError:
            raise ValueError(f'Invalid direction: {list[2]}')
        return x, y, direction
    #print(parse_rover('5 5 N'))
    #print(parse_rover('5 5 P'))

    def parse_instructions(input):
        valid_letters = []
        for chr in input:
            try:
                Instruction(chr)
                valid_letters.append(chr)
            except:
                continue
        return valid_letters
            
        #return [chr for chr in input if Instruction(chr)]
    #print(parse_instructions('LMLRMBM'))