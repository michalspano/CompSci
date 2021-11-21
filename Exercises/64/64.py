#!/usr/bin/env python3

"""
Michal Špano
64. Seating Chart
20/11/2021
"""

import csv
from sys import exit
import tkinter as tk
from typing import Final

# Canvas attributes
c_dim: int = 500
canvas = tk.Canvas(height=c_dim, width=c_dim)
canvas.pack()

# Global variables
file_ext: Final = '.csv'
data: list = []


# Define main function
def main(PATH: str = 'seating_chart.csv') -> None:
    global data
    exit('Invalid file extension') if not check_file_extension(PATH) else print(
        f'Valid file extension at {PATH}.')

    # Populate data list with data from csv file (global reference)
    with open(PATH, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]


# Triggered upon user input
def evaluate_user_input(dims: list) -> None:
    # Transform to int and handle error
    try:
        dims = [int(j) for j in dims]
    except ValueError:
        print('Invalid input, must be an <int>')
        return
    # Evaluate max number of sitting places
    max_dim: int = dims[0] * dims[1]
    exit('Not enough sitting places for students.') if max_dim < len(data) else None

    # Draw canvas objects
    draw_canvas_obj(dims[0], dims[1])


# Draw canvas attributes onto canvas
def draw_canvas_obj(row_num: int, col_num: int) -> None:
    canvas.delete('all')
    # Determine current width and height of each seat
    width, height = c_dim // col_num, c_dim // row_num
    # Draw seats
    person_idx: int = 0
    for j in range(row_num):
        for i in range(col_num):
            # Draw seat place
            canvas.create_rectangle(i * width, j * height, (i + 1) * width, (j + 1) * height,
                                    fill='white', outline='black')
            # Draw student attributes if any left
            if person_idx <= len(data) - 1:
                default_coords: list = [(i * width + (i + 1) * width) // 2,
                                        (j * height + (j + 1) * height) // 2]
                canvas.create_text(default_coords[0], default_coords[1] + height // 2 - 10,
                                   text=data[person_idx]['surname'], fill='red')
                canvas.create_text(default_coords[0], default_coords[1] - height // 2 + 10,
                                   text=data[person_idx]['name'], fill='blue')
                person_idx += 1


# Function to ensure that the input path has file extension .csv
def check_file_extension(PATH: str) -> bool:
    return True if PATH.endswith(file_ext) else False


# Invoke main function
if __name__ == '__main__':
    main()  # Invoke main function
    # Crate canvas attributes
    row_count_label, column_count_label = tk.Label(text='Row count'), tk.Label(text='Column count')
    row_entry, column_entry = tk.Entry(), tk.Entry()
    row_count_label.pack(), row_entry.pack()
    column_count_label.pack(), column_entry.pack()
    eval_button = tk.Button(text='Evaluate',
                            command=lambda: evaluate_user_input([row_entry.get(), column_entry.get()]))
    eval_button.pack()
    canvas.mainloop()
