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

    """
    Source: https://stackoverflow.com/questions/45782766/color-python-output-given-rrggbb-hex-value/45782972#45782972
    """

    RESET = '\033[0m'  # {Octal backspace default reset}

    # Parse octal backspace from RGB color
    def term_color_escape(r: int, g: int, b: int, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    # Format colored (visual) command line output
    def format_term_color(f: tuple, color: tuple) -> None:
        print(term_color_escape(f[0], f[1], f[2])  # {Text fill color}
              + term_color_escape(color[0], color[1], color[2], background=True)  # {BG color}
              + 'Sample Text'
              + RESET)

    i: int = 1
    # Iterate over possible colors
    for x in range(x_shift, img_width, x_shift * 2):
        j: int = 1
        for y in range(y_shift, img_height, y_shift * 2):
            c = img_sprite.get(x, y)  # {Receive current color}
            text_fill_white: bool = is_white(c)

            # Text fill color (type tuple)
            text_f: tuple = (255, ) * 3 if text_fill_white else (0, ) * 3

            # Print out colored output onto terminal
            format_term_color(text_f, c)
            j += 1
        i += 1

    # Close IO
    out_file.close()


# Invoke main
if __name__ == '__main__':
    main()
