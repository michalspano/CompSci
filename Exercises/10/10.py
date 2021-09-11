"""
Michal Špano
10. Creation of Crossword Puzzle 1
11/09/2021
"""

# Import libs
import tkinter as tk
from typing import final

# Initialize canvas
canvas = tk.Canvas(width=500, height=400)
canvas.pack()


# Define constant dimension of the box (d x d)
d: final = 35


# Load crossword data to memory and return type list
def load_crossword_data(path) -> list:
    loaded_data: list = [[int(row.strip().split()[0]), row.strip().split()[1]] for row in open(path)]
    return loaded_data


# Invoke method to load data to memory
cw_data: list = load_crossword_data('crossword.txt')


# Define a function to create individual rows
def draw_row(data, x, y):
    s_idx = data[0] - 1                                             # Regular index from 0
    selected_char = data[1][s_idx]                                  # Middle selected character from the word

    canvas.create_rectangle(x, y, x + d, y + d, fill="gray")         # Show middle char on canvas
    canvas.create_text(x + (d / 2), y + (d / 2), text=selected_char)

    sub_arr1, sub_arr2 = data[1][:s_idx], data[1][s_idx + 1:]       # Split into 2 substrings

    # Define a universal function to draw remaining boxes
    def draw_voided(arg, isLeft):
        for j in range(0, len(arg)):                                # Iterate over the length of the substring
            r = - (j + 1) if isLeft else j + 1                      # Check for inverted index of draw
            s = len(arg) - j - 1 if isLeft else j                   # Check for inverted index of the substring

            # Create objects on the canvas
            canvas.create_rectangle(x + r * d, y, x + r * d + d, y + d)
            canvas.create_text(x + (d / 2) + r * d, y + (d / 2), text=arg[s])

    # Call universal draw function 2 times (for each side)
    draw_voided(sub_arr1, True), draw_voided(sub_arr2, False)


# Call default draw function in a loop (iterate over all words)
for i in range(len(cw_data)):
    draw_row(cw_data[i], int(canvas['width']) / 2, i * d + d)


canvas.mainloop()
