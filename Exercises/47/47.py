#!/usr/bin/env python3

"""
Michal Špano
47. Barcode
04/11/2021
"""

import random as r
import tkinter as tk
from sys import argv

# Define graphical canvas
c_dim: int = 80
canvas = tk.Canvas(width=c_dim, height=c_dim, bg='white')
canvas.pack()


# Define main function
def main(path: str = 'input.txt'):
    # Load generated barcode (2 possible ways)
    gen_barcode: [int] = create_code() if len(argv) == 1 else load_barcode(path)

    # Check None-type -> Error
    if gen_barcode is None:
        exit('Invalid source.')

    # Out
    print(f"Loaded barcode: {' '.join([str(b_c) for b_c in gen_barcode])}")
    display_barcode(gen_barcode)


# Create a function to randomly generate a barcode
def create_code(MAX: int = 8) -> [int]:
    return [r.randrange(0, 10) if i != 0 else r.randrange(1, 10) for i in range(MAX)]


# Function to display barcodes graphically
def display_barcode(code_src: [int], s: int = 10) -> None:
    for i in range(len(code_src)):
        # The first and last lines are prolonged
        floor: int = 0 if i == 0 or i == len(code_src) - 1 else -20

        # Canvas objects (lines and code itself)
        canvas.create_rectangle(i * s + 5, 0, i * s + code_src[i] + 5, c_dim + floor,
                                fill='black', outline='')
        canvas.create_text(7.5 * (i + 1) + 10, c_dim - 10, text=str(code_src[i]),
                           fill='black', font='Arial 12')


# Optional - function to load barcode data to memory
def load_barcode(PATH: str) -> [int] or None:
    # Check existing file and handle possible error
    try:
        _ = open(PATH).close()
    except FileNotFoundError:
        return

    # Parse data
    data: list = [int(val) for sublist in open(PATH) for val in sublist]
    return data if len(data) == 8 else None  # {Check valid input else return None}


# Invoke main function
if __name__ == '__main__':
    main()
    canvas.mainloop()
