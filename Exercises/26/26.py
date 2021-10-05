#!/usr/bin/env python3

"""
Michal Špano
25. Lottery
29/09/2021
"""

# Import libs
import random as r
import tkinter as tk
from time import sleep
from sys import argv

t_counter, c_dim = 0, 500
canvas = tk.Canvas(height=c_dim, width=c_dim, bg='#40bad9')
canvas.pack()


def main():
    # Parse command-line arguments
    if len(argv) != 2:
        exit('Usage: ./[].py $RANGE')

    # User invoked
    print('Press <space> to start!')

    # Bind creation to space event
    canvas.bind_all('<space>', create)
    canvas.mainloop()


# Randomly choose between mountain / valley
def terrain_type() -> bool:
    return r.choice([True, False])


def terrain_prebuilt() -> list:
    return [[0, c_dim], [0, c_dim // 2 + r.randint(-100, 100)], [c_dim] * 2]


# Define main function
def create(event):
    global t_counter

    # Iterate n times (from command-line arguments)
    for _ in range(int(argv[1])):
        t_counter += 1

        # Receive random terrain type
        _type: bool = terrain_type()

        # LOG
        print(f"Number of canvas objects: {t_counter}\n"
              f"Type: {'Mountain' if _type else 'Valley'}")

        # Generate formation and insert into a polygon
        form: list = generate(is_mount=_type)
        canvas.create_polygon(form, fill=format_color(), outline='')

        # Delay
        sleep(1)
        canvas.update()


# Function to create random color of green (as HEX)
def format_color(_min: int = 75) -> str:
    return "#{:02x}{:02x}{:02x}".format(0, r.randint(_min, 255), 0)


# Function to generated the terrain
def generate(N: int = 10, is_mount: bool = True) -> list:
    formation = terrain_prebuilt()  # {Load randomly edited terrain}

    # Create method to change height
    def mount(increase: bool, b1: int = 2, b2: int = 10) -> int:
        return r.randint(-b2, -b1) if increase else r.randint(b1, b2)

    j: int = 0
    for i in range(10, c_dim + 10, N):  # {Change every N pixels [default = 10]}
        if i <= c_dim // 2:  # {Vertex}
            shift = mount(increase=True) if is_mount else mount(increase=False)
        else:
            shift = mount(increase=True) if not is_mount else mount(increase=False)

        # Parse new height
        new_height: int = formation[j + 1][1] + shift

        # Prevent leaking heights
        if new_height >= c_dim:
            new_height = c_dim

        # Insert to polygon's list
        formation.insert(j + 1 + 1, [i, new_height])
        j += 1

    # Return parsed formation
    return formation


# Invoke main function
if __name__ == '__main__':
    main()
