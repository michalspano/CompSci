#!/usr/bin/env python3

"""
Michal Špano
59. Bus Capacity Analysis
13/11/2021
"""

import tkinter as tk
c_dim: int = 500
canvas = tk.Canvas(height=c_dim, width=c_dim)
canvas.pack()

# Global object counter
obj_count: int = 0


# Create a function to load data to memory
def load_data(path: str) -> (int, dict):
    data: dict = {}
    current_capacity: int = 0

    # Open file
    with open(path) as f:
        try:
            capacity: int = int(f.readline().strip())
        except ValueError:
            raise ValueError('Capacity must be an integer')
        temp_data: list = [row.strip().split() for row in f]

    # Iterate over passed stations
    for st in temp_data:
        try:
            current_capacity += int(st[0])
            current_capacity -= int(st[1])
        except ValueError:
            raise ValueError('Must be an integer')

        # Populate dict
        data[' '.join([f for f in st[2:]])] = current_capacity

    # Return data (capacity, dict)
    return capacity, data


# Global loaded data
print(f'\u001b[31mPress any key to start.\033[0m')
instance: tuple = load_data('bus_util_extent.txt')
max_capacity: int = instance[0]
loaded_data: dict = instance[1]
station_count: int = len(loaded_data)


# Create a function to display data onto canvas
def display_data(_max: int, data: dict, idx: int) -> None:
    # Base case
    if idx > len(data):
        return

    # Delete all previous stats
    canvas.delete('all')

    i: int = 0
    # Slice dict to display only the first 'idx' items
    for key in dict(list(data.items())[:idx]):
        # Display name
        canvas.create_text(100, i * (c_dim // len(data)) + 20, text=key)

        # Create a 'struct' with default values
        coords_struct: list = [c_dim // 2, i * (c_dim // len(data)) + 10, None,
                               i * (c_dim // len(data)) + 30]

        # Display max capacity
        coords_struct[2] = c_dim // 2 + _max * 3
        canvas.create_rectangle(coords_struct)

        # Fil in current capacity
        coords_struct[2] = c_dim // 2 + data[key] * 3
        canvas.create_rectangle(coords_struct,
                                fill='green')
        i += 1


# Create a global object counter
def obj_counter() -> None:
    global obj_count
    if obj_count < station_count:
        obj_count += 1
        print(f'Displaying {obj_count}/{station_count} stations.')
        display_data(max_capacity, loaded_data, obj_count)


# Bind to any key press
canvas.bind_all('<Key>', lambda event: obj_counter())
canvas.mainloop()
