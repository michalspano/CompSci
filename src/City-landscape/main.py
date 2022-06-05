"""
Michal Špano
City landscape in Python
21/09/2021
"""

# Include final
from typing import final


"""
8x8 town dimension
MAX_HEIGHT 10
"""

dimension: final = 8

# Define possible directions to view the img
directions: final = ['N', 'S', 'W', 'E']

"""
BACKGROUND
N - S;
W - E;
will always be symmetrical, i.e. same height present in the views.
"""


# Define main function
def main(*args):
    # Process argument vector from input-line
    src_path, out_path, direction = args[0], args[1], args[2]

    # -> {List of nested lists of size 8x8}
    loaded_data: list = [[int(r) for r in row.strip().split()] for row in open(src_path)]

    # Create bit-map IO
    bit_map = open(f"{out_path}bit_map.txt", "w")

    # Write bit_map header
    header(bit_map)

    # Create a bit-map (view from above 0/1)
    for row in loaded_data:
        for value in row:
            # Hash each int
            bit_map.write(hash_bit(value))

        # Assign new line
        bit_map.write('\n')

    # Check for correct direction
    if direction not in directions:
        exit('Incorrect usage')

    # Temp list container
    temp_data: list = []

    # Transform data when 'North' or 'South' selected
    if direction == 'N' or direction == 'S':
        for i in range(dimension):
            row = []
            for j in range(dimension):
                row.append(loaded_data[j][i])
            temp_data.append(max(row))  # {Assign the max value from the current row}

    # Transform data when 'West' or 'East' selected
    elif direction == 'W' or direction == 'E':
        for row in loaded_data:
            temp_data.append(max(row))  # {Assign the max value from the current row}

    # Formatted output (in a bit map)
    output_map = open(f"{out_path}out_map{direction}.pbm", "w")

    # Write headers
    header(output_map)

    # Write heights to a bit map
    for i in range(dimension):
        for h in temp_data:
            r = dimension - i
            if h < r:
                key = 0
            else:
                key = 1
            output_map.write(str(key))
        output_map.write('\n')

    # Close text file
    bit_map.close()
    output_map.close()


# Create a function to hash bit values
def hash_bit(value: int) -> str:
    if value >= 1:
        value = 1
    elif value <= 0:
        value = 0
    return str(value) + ' '


# Create a function to write bitmap headers
def header(file, d: int = 8):
    file.write(f"P1\n{d} {d}\n")
    return


# Invoke main function in a function call
if __name__ == '__main__':
    main('src/src.txt', 'out/', 'N')
