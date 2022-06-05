#!/usr/bin/env python3

"""
Michal Špano
31. Black and White Picture
12/10/2021
"""

import os

# Default canvas definition
import tkinter as tk

# Use command-line arguments
from sys import argv

# Import generation method
from utils.generate import GENERATE
canvas = tk.Canvas()
canvas.pack()


# Define main function
def main(input_path: str):
    """
    TODO: Fix for uniform platform
    Now: 1:1 ratio only.
    """

    # Generate new env (check for a valid digit)
    # If no command-line argument is passed, current local input will be parsed
    if len(argv) == 2:
        GENERATE(int(argv[1])) if argv[1].isdigit() and int(argv[1]) > 1 \
            else exit(f'./{os.path.relpath(__file__)} $NUMERIC EXPRESSION (greater than 1).')

    # Do not allocate data to memory
    with open(input_path) as f:

        # Edit canvas preferences
        dimensions: list = f.readline().split(' ')

        # Max canvas size 720 x 720 - 1px
        max_d: int = 720

        # Update canvas
        canvas['width'], canvas['height'] = max_d, max_d

        # Quotient of max to relative pixels
        k: float = max_d / int(dimensions[0])

        # Iterate over all colors
        i: int = 0  # {Row index}
        for row in f.readlines():
            j: int = 0  # {Column index}
            colors: list = [row[i:i + 2] for i in range(0, len(row.strip()), 2)][::-1]
            for c in colors:
                # Transform to valid hex codec
                new_color: str = f'#{c * 3}'

                # Create individual pixels
                create_pixel(k * j, k * i, new_color, k)
                j += 1
            i += 1

    # Define Black-White button
    button1 = tk.Button(text='Black & White', command=black_white)
    button1.pack()
    canvas.mainloop()


# Create individual pixels
def create_pixel(x: float, y: float, c: str, k: float) -> None:
    canvas.create_rectangle(x, y, x + k, y + k, fill=c, outline='')


# Static method to transform pixels to B&W only (without any memory allocation)
def black_white() -> None:
    for ID in canvas.find_all():
        # Receive current trimmed fill in hex
        current_fill: str = f"0x{canvas.itemconfig(ID, 'fill')[-1][1:3]}"

        # Transform to base 10 value
        numeric: int = int(current_fill, 16)

        # Final fill evaluation
        f_fill: str = 'black' if numeric < 127 else 'white'

        # Update canvas objects
        canvas.itemconfig(ID, fill=f_fill)
        canvas.update()


# Invoke main function
if __name__ == '__main__':
    main('in.txt')
