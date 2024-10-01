"""
Michal Špano
13. Glutton
15/09/2021
"""

import tkinter as tk
import random as r
from typing import final

# Define fixed canvas bounds
c_width, c_height = 500, 500

# Define max number of apples
N: final = 20

canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()


# Create a function to draw glutton
def display_glutton(fix_d: int = 20):
    r_x, r_y = r.randint(fix_d * 2, c_width - (fix_d * 2)), r.randint(fix_d * 2, c_width - (fix_d * 2))
    canvas.create_oval(r_x - fix_d, r_y - fix_d, r_x + fix_d, r_y + fix_d, fill='blue', outline='', tags='glutton')
    display_apples(r_x, r_y)


# Create a function to draw apples (detect glutton collision)
def display_apples(g_x, g_y):

    # Iterate over a randomly chosen range
    for i in range(r.randint(1, N)):
        while True:
            a_x, a_y = r.randint(10 * 2, c_width - (10 * 2)), r.randint(10 * 2, c_width - (10 * 2))

            # Non-conflicting coords
            if a_x > g_x + 20 or a_x < g_x - 20 and a_y > g_y + 20 or a_y < g_y - 20:
                break

        # Create a canvas object
        canvas.create_oval(a_x - 10, a_y - 10, a_x + 10, a_y + 10, fill='red', outline='')


# Define a function to move with glutton
def move_glutton(tag: str = 'glutton', m_s: int = 1):
    global move_arr, move_ID

    # Get the current position of glutton
    c: list = canvas.coords(tag)

    # Append new key
    move_arr.append(move_ID)

    # Check for correct key
    if move_ID not in ['w', 'a', 's', 'd']:

        # Else use the previously stored key
        move_ID = move_arr[0]

        # Prompt with incorrect usage
        print("Incorrect usage: keys = 'w' 's' 'a' 'd'")

    # Switch for correct game keys
    if move_ID == 'd':
        c[0] += m_s
        c[2] += m_s

    elif move_ID == 'a':
        c[0] -= m_s
        c[2] -= m_s

    elif move_ID == 'w':
        c[1] -= m_s
        c[3] -= m_s

    elif move_ID == 's':
        c[1] += m_s
        c[3] += m_s

    # Remove old key
    move_arr.pop(0)

    # Assign new coords
    canvas.coords(tag, c)

    # Check for collisions
    apple_collision(c)

    # Number of left canvas elements
    c_arr = len([True for _ in canvas.find_all()]) - 1

    # Check for winning scenario (i.e.m no apples left)
    if not detect_end_game(c_arr):
        canvas.after(5, move_glutton)
    else:
        game_win()


# Detect apple collision
def apple_collision(gl_c):
    overlap = canvas.find_overlapping(gl_c[0], gl_c[1], gl_c[2], gl_c[3])
    if len(overlap) != 1:  # -> Indicates detected collision
        canvas.delete(overlap[1])  # Remove collided apple


# Detect player controls
def key_input(event):
    global move_ID
    move_ID = event.keysym


# Check for end game scenario
def detect_end_game(counter: int) -> bool:
    return True if counter <= 0 else False


# Display end game msg
def game_win():
    canvas.create_text(c_height / 2, c_width / 2, text='Game Won!', font='Helvetica 40 bold')


display_glutton()
move_ID: chr = 'd'  # ->  Default right
move_arr: list = [move_ID]  # -> 2el. list to store positions options
move_glutton()
canvas.bind_all("<Key>", key_input)
canvas.mainloop()
