# Creating a JSON parser in Python
import json
from sys import exit


# Create parser instance
def parser(PATH):
    # Receive user input (in a list)
    user_coords: list = [input(f'{ip} [in binary]: ') for ip in ['Latitude', 'Longitude']]
    directions: list = [input(f'Direction {i + 1}: ') for i in range(2)]  # {Receive map directions}

    # Check for type float
    for i in range(len(user_coords)):
        try:
            float(user_coords[i])
            user_coords[i] = float(user_coords[i])  # {Convert to type float}
        except ValueError:  # {Exit program if not convertible to float}
            exit('Value error')

    # Transform coords to a dict
    coords_dict: dict = {'coordinates': {'latitude': user_coords[0], 'longitude': user_coords[1]},
                         'directions': [directions[0], directions[1]]}

    with open(PATH, "w") as f:  # {Open specified path}
        json_write = json.dumps(coords_dict, indent=4, separators=(', ', ': '))  # {Define json dump}
        f.write(json_write)  # {Write to json}
