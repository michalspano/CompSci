#!/usr/bin/env python3

"""
Michal Špano
42. Save the falling egg
23/10/2021
"""

import tkinter as tk
import random as r
from sys import argv

# Canvas settings
c_dim: int = 500
canvas = tk.Canvas(width=c_dim, height=c_dim)
canvas.pack()


# noinspection PyTypeChecker
def animate_object(e_dim: tuple = (20, 25)):
    global y_pos, x_pos, state, current_key  # {Global references}

    # Increment y position
    y_pos += 2

    # Delete current object and update new position
    canvas.delete('egg')
    canvas.create_oval(x_pos, y_pos, x_pos + e_dim[0], y_pos + e_dim[1],
                       tags='egg', fill='white')

    # Display desired char once 2/3 are passed
    if y_pos > (c_dim // 3) * 2:
        canvas.create_text(x_pos + e_dim[0] // 2, y_pos + e_dim[1] // 2,
                           text=current_key, tags='egg')

    # Call upon function if y position is valid and char not guessed
    if y_pos < c_dim - e_dim[1] and not state:
        canvas.after(10, animate_object)

    # If char is guessed
    elif state:
        x_pos, y_pos = r.randint(10, c_dim - 10), 0  # {Restart position}
        state = False  # {Restart state}
        current_key = generate_random_char()  # {Generate new char}

        # Show keys (based on command-line passed value)
        show_key: bool = lambda op: True if len(op) == 2 and op[1] == 'ON' else False
        if show_key(argv):
            print(f"Key: {current_key}")

        # New animation
        animate_object()
    else:
        exit("You lost!")


# Function to generate a random char
def generate_random_char(_range: int = 26) -> str:
    return r.choice([chr(i + 97) for i in range(_range)])


# Function to generate random x position
def generate_random_x(d: int = c_dim, x_s: int = 10) -> int:
    return r.randint(x_s, d - x_s)


# Check user input
def check_key(event):
    global state  # {Global reference}
    state = True if event.keysym == current_key else False


# Global variables
x_pos, y_pos = generate_random_x(), 0  # {Initial position}
current_key: str = generate_random_char()
state: bool = False

# Initial function call
animate_object()
print(f"Welcome to 'SAVE THE FALLING EGG'\nFirst char: {current_key}")

canvas.bind_all('<Key>', check_key)
canvas.mainloop()
