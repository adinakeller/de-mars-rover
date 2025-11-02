# Mars Rover
The surface of Mars is represented by a Plateau, which is a square/rectangular grid.
Rovers on the surface of Mars navigate the Plateau by following a sequence of commands.

- users will define the plateau size and input commands to start and move the rover to certain positions
- each rover has a starting position of (x, y) coordinates and a direction, which is North, South, West or East
- the rover can turn left or right and move forward depending on its commands

# Set Up
1. clone the repository
2. create a virtual environment
3. install dependencies in the requirements.txt file
4. define plateau size and rover starting point in main.py

# Files
- inputs.py: handles user input validation
- enums.py: handles instruction and direction validation
- tests: uses pytest to test inputs, enums and dataclasses
