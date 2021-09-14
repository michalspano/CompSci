"""
Michal Špano
Personal cards in Python
14/09/2021
"""

# Include libs to be used
import json
import random as r
from typing import final

# Time module (optional)
from datetime import datetime

# Include modules to manipulate images
from PIL import Image, ImageDraw

# Define colors
c: final = ['red', 'green', 'blue']
            
# Open logs src
logs = open('logs/check.log', 'w')


# Define main function
def main():

    # Initialize time
    begin = datetime.now()

    # Get the default dimensions from a json file
    dimensions: tuple = load_config('config/config.json')

    # Load the names' database to a list
    db_names: list = load_database('src/names.csv')

    # Iterate over all elements in the database and assign its index value
    for i in range(len(db_names)):
        create_card(db_names[i], i + 1, dimensions)

    # *** OPTIONAL - EXECUTION TIME ***
    end = datetime.now()
    print(f'Execution time: {end - begin}s')


def load_config(PATH) -> tuple:
    # Load the specified path
    with open(PATH, ) as input_file:
        # Convert to json
        config = json.load(input_file)

    # Return type tuple (from nested JSON)
    return config['dimensions']['width'], config['dimensions']['height']


def load_database(PATH) -> list:
    # Return type list from the database
    return [name.strip() for name in open(PATH)]


# Create a function to create individual cards
def create_card(name: str, index: int, d):

    # Receive img dims
    m_width, m_height = d[0], d[1]

    # Create a local img using PIL
    local_image = Image.new('RGB', (m_width, m_height), 'white')

    # Create a draw method from PIL
    draw = ImageDraw.Draw(local_image)

    # Create a function to draw individual graphics (fixed dimension by default of 10)
    def create_graphics(fix_d: int = 10, max_g: int = 5):

        # Create an empty list to store coords of a single card (i.e., its elements)
        coords: list = []

        # Create graphics in a randomised loop (max 5)
        for _ in range(r.randint(1, max_g)):

            # Create an inner function to return random location from specified range
            def randomised_location(dim_par: int) -> int:
                return r.randint(fix_d * 2, dim_par - fix_d * 2)

            """
            NOTE: Only partial collision implemented;
            Single collision will be detected.
            """

            # Avoid collision detection if no objects were drawn
            if len(coords) == 0:
                coords.append(randomised_location(m_width)), coords.append(m_height)

            # Check for collision
            else:
                start: bool = True

                # Load current coords from the drawn objects
                c_x, c_y = coords[::2], coords[1::2]
                while start:
                    # Generate random coords
                    r_x, r_y = randomised_location(m_width), randomised_location(m_height)

                    # Iterate over the loop of drawn objects
                    for j in range(len(c_x)):

                        # Detect non-conflicting coords
                        """
                        'fix_d' represents the fixed radius of each oval;
                        we need to take the radius multiplied by 2 in the condition to prevent any possible overlapping.
                        """
                        if ((c_x[j] - fix_d * 2 >= r_x) or (r_x >= c_x[j] + fix_d * 2)) and \
                                ((c_y[j] - fix_d * 2 >= r_y) or (r_y >= c_y[j] + fix_d * 2)):

                            # *** LOGS (OPTIONAL ***
                            logs.write(f"{c_x[j]=}: {r_x=}; {abs(c_x[j] - r_x)}")
                            logs.write(f"{c_y[j]=}: {r_y=}; {abs(c_y[j] - r_y)}\n")

                            # Break out of the loop and append valid coords
                            start = False
                            coords.append(r_x), coords.append(r_y)  # -> Valid coords

            # Access a random color from the predefined list of available colors
            r_color = r.choice(c)

            # Draw an object
            shape = [(coords[-2] - fix_d, coords[-1] - fix_d), (coords[-2] + fix_d, coords[-1] + fix_d)]
            draw.ellipse(shape, fill=r_color)

    # Call the nested function
    create_graphics()

    # Draw the name from the database
    draw.text((m_width / 2 - 25, m_height / 2), text=name, fill='black')

    # Specify the filename
    filename: str = 'dist/card'

    # Save the img at specified path (locally)
    local_image.save(f'{filename}{index}.jpg')


# Invoke the main function
if __name__ == '__main__':
    main()

    # Close logs file
    logs.close()
