# Creating a JSON parser in Python
from sys import argv, exit
import json


# Create main function {using command-line arguments}
def main():
    if len(argv) != 2:  # {Check for correct command-line usage}
        print("Usage: ./parser $PATH"), exit(1)
    # Path taken from command line
    PATH: str = argv[1]

    # Receive user input (in a list)
    user_coords: list = [input(f'{ip} [in binary]: ') for ip in ['Latitude', 'Longitude']]

    # Check for type float
    for i in range(len(user_coords)):
        try:
            float(user_coords[i])
            user_coords[i] = float(user_coords[i])  # {Convert to type float}
        except ValueError:  # {Exit program if not convertible to float}
            exit('Value error')

    # Transform coords to a dict
    coords_dict: dict = {'coordinates': {'latitude': user_coords[0], 'longitude': user_coords[1]}}
    with open(PATH, "w") as f:  # {Open specified path}
        json_write = json.dumps(coords_dict, indent=4, separators=(', ', ': '))  # {Define json dump}
        f.write(json_write)  # {Write to json}


# Invoke main function
if __name__ == '__main__':
    main()
