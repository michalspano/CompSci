#!/usr/bin/env python3

"""
Michal Špano
56. Level Editor 1
13/11/2021
"""

import os
import tkinter as tk

# Define global dimension of canvas object
c_dim: int = 500
canvas = tk.Canvas(width=c_dim, height=c_dim)
canvas.pack()


# Create a function to generate grid of squares 10x10
def generate_grid(LIMIT: int = 10) -> None:
    square_dim: int = c_dim // LIMIT
    for i in range(LIMIT):
        for j in range(LIMIT):
            canvas.create_rectangle(i * square_dim, j * square_dim,
                                    (i + 1) * square_dim, (j + 1) * square_dim,
                                    fill='#ffffff', outline='black')


# Create a function to pass data from an entry box
def entry_data() -> str:
    return color_entry.get()


# Get user click coordinates pointing to a square
def user_click(event) -> None:
    overlap: tuple = canvas.find_overlapping(event.x, event.y, event.x, event.y)

    # Ignore if not object is clicked
    if not overlap:
        return

    # Change color of the square to a color passed in the entry box (only if valid color is passed)
    entry_color: str = entry_data()
    if is_valid_hex_color(entry_color):
        canvas.itemconfig(overlap[0], fill=entry_color)
    else:
        print('Invalid hexadecimal color')


# Create a function to save the canvas to a file
def save_canvas_attrs(PATH: str = 'out/level_editor1_output.txt') -> bool:
    # Handle the case when directory does not exist
    try:
        output_file = open(PATH, 'w')
    except FileNotFoundError:
        return False

    # Save all objects on the canvas: (canvas type; coordinates; color)
    # Iterate over all objects on the canvas
    for ID in canvas.find_all():
        print(f"{canvas.type(ID)};{' '.join(str(c) for c in canvas.coords(ID))};"
              f"{canvas.itemconfig(ID, 'fill')[-1]}", file=output_file)

    # Close output file
    output_file.close()

    # Display file contents to the console
    os.system(f"cat {PATH}")
    return True


# Function to determine valid hex color
def is_valid_hex_color(color: str) -> bool:
    if len(color) != 7:  # {valid length}
        return False
    if color[0] != '#':  # {valid format}
        return False
    for i in range(1, 7):  # {check valid hex digits; 1-9, a-f}
        if not color[i].isdigit() and not 'a' <= color[i].lower() <= 'f':
            print('a')
            return False
    return True


generate_grid()
color_entry = tk.Entry()
color_entry.pack()

# Save button, process only if returned True
save_button = tk.Button(text='Save', command=lambda: save_canvas_attrs() if save_canvas_attrs() else None)
save_button.pack()

# Bind left click to user_click function
canvas.bind("<Button-1>", user_click)
canvas.mainloop()
