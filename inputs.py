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
    print(parse_plateau("PLATEAU0x0"))
    print(parse_plateau("5 5"))   
        

    def parse_rover(input):
        list = input.split()
        x = int(list[0])
        y = int(list[1])
        compass = list[2]
        return x, y, compass
    print(parse_rover('5 5 N'))

    def parse_instructions(input):
        input.strip()
        return [chr for chr in input]
    print(parse_instructions('LMLRMLM'))