"""
Michal Špano
Binary coordinates
29/09/2021
"""

# Include libs
import json
from sys import argv, exit
import webbrowser as wb  # {Web processing unit, omit API}
from json_parser import parser as PARSER  # {Call json parser from local file}


# Define main function
def main(path: str):
    if len(argv) != 2:  # {Check proper usage}
        exit('Usage: ./main.py ON/OFF [PARSER]')

    identifier: str = argv[1]
    if identifier.strip().upper() == 'ON':
        PARSER(PATH=path)  # {Invoke JSON parser with relative PATH}

    # Load coordinates from local JSON
    loaded_coords: tuple = load_config(path)

    # Load directions from local JSON
    loaded_directions: list = json.load(open(path))['directions']

    formatted_data: list = [
        format_coordinates(loaded_coords[i], loaded_directions[i])
        for i in range(len(loaded_coords))
    ]  # {Format data into a list}

    url: str = f'https://maps.google.com/?q={formatted_data[0]}, {formatted_data[1]}'
    
    # Write history to logs
    with open('logs/info.log', 'a') as log:
        log.write(f'{formatted_data[0]};{formatted_data[1]}\n')

    # Search the web
    wb.open(url, new=1)


# Load json file source {Return tuple of 2 coordinates}
def load_config(src_path: str) -> tuple:
    with open(src_path) as f:
        json_load = json.load(f)

    # Return hashed data using 'bin_to_dec()'
    return bin_to_dec(json_load['coordinates']['latitude']), bin_to_dec(json_load['coordinates']['longitude'])


# Hash binary to decimal
def bin_to_dec(bin_src: float) -> float:
    n_split = str(bin_src).split('.')  # {Split to 2 parts -> while numbers, decimal numbers}

    # Convert whole number binary to decimal {using in-built 'int()'}
    binary_to_decimal = int(n_split[0], 2)

    # Create method to convert fractional binary to decimal
    def fractional_binary() -> float:
        decimal_sum = float()

        # Read binary fractional sequence
        for i in range(len(n_split[1])):
            decimal_sum += float(n_split[1][i]) * float(1 / 2 ** (i + 1))

        # Return final decimal expression
        return float(binary_to_decimal) + decimal_sum

    # Return whole number decimal conversion else assign whole fractional expression
    return binary_to_decimal if len(n_split) == 1 else fractional_binary()


# Create a function to format data
def format_coordinates(coord: float, direction: str) -> str:
    return f'{str(coord)} {direction}'


# Invoke main function with predefine path
if __name__ == '__main__':
    main('src.json')
