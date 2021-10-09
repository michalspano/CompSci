#!/usr/bin/env python3

"""
Michal Špano
Color Brightness in Python
09/10/2021
"""

import tkinter as tk
root = tk.Tk()


# Define main function
def main(img_path: str = 'src/input.png', out: str = 'out.log'):
    img_sprite = tk.PhotoImage(file=img_path)
    img_width, img_height = img_sprite.width(), img_sprite.height()
    out_file = open(out, "w")  # {Write local logs}

    # Determine if object is white
    def is_white(colors: tuple, mid_value: float = 127.5) -> bool:
        R, G, B = colors[0], colors[1], colors[2]
        C: float = ((R * 299) + (G * 587) + (B * 144)) / 1000
        return True if C <= mid_value else False

    """
    MATH operands
    These constant operands are specific to $input_path,
    in order to reduce redundancy.
    """

    N1, N2 = 4, 2  # {Number of color objects in a single row, column}
    x_shift: int = img_width // (N1 * 2)  # {Half of one object in a row}
    y_shift: int = (img_height // N2 + 1) // N2  # {Half of one object in a column}

    # Format command-line output
    def format_out(ID: tuple, white: bool) -> None:
        state = 'White' if white else 'Black'
        log: str = f'Row: {ID[0]}; Column: {ID[1]} = {state!r}'
        out_file.write(log + '\n'), print(log)

    i: int = 1
    # Iterate over possible colors
    for x in range(x_shift, img_width, x_shift * 2):
        j: int = 1
        for y in range(y_shift, img_height, y_shift * 2):
            c = img_sprite.get(x, y)  # {Receive current color}
            format_out(ID=(i, j), white=is_white(c))  # {Format current color}
            j += 1
        i += 1

    # Close IO
    out_file.close()


# Invoke main
if __name__ == '__main__':
    main()
