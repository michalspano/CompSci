#!/usr/bin/env python3

"""
Michal Špano
34. Image Decompression
13/10/2021
"""

import os.path as os


# Create the main function
def main(PATH: str = 'input.txt'):
    """
    Abstract:
    Each line from the input represents a row of an image.
    Image type: bitmap of 0/1.
    Schema: Wn Bn Wn ... (alternating values for blacks [1] and whites [0])
    """

    # Load input file
    with open(PATH) as f:
        dim: list[str] = f.readline().split()
        file_dimensions(dim)

        # Hold parsed sequence in a list
        bin_data: list = []
        for row in f:
            formatted_row: str = process_line(row.strip().split(' '))
            bin_data.append(formatted_row)

    # Create visual output
    create_bitmap('out.pbm', dim, bin_data)

        
# Process input file dimensions
def file_dimensions(d: list[str]):
    print(f'File dimensions: {d[0]}x{d[1]}')


# Create a function to process current line
def process_line(r: list, isBlack: bool = False, parsed_line: str = '') -> str:
    for val in r:  # {Iterate over all colors}
        parsed_line += '1' * int(val) if isBlack else '0' * int(val)  # {Evaluate binary}
        isBlack = False if isBlack else True  # {Switch bool}
    return parsed_line


# Create bitmap from the parsed data
def create_bitmap(out_PATH: str, d: list, data: list[str]):
    with open(out_PATH, 'w') as OUT:
        OUT.write('P1\n')  # Define standard header
        OUT.write(f'{d[0]} {d[1]}\n')  # Define dimensions

        # Write individual rows
        [OUT.write(f'{data[i]}\n') for i in range(len(data))]
    print(f'Bitmap saved at {out_PATH}\nSource: {os.relpath(__file__)!r}')


# Invoke the main function
if __name__ == '__main__':
    main()
