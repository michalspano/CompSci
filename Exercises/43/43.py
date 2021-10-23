#!/usr/bin/env python3

"""
Michal Špano
43. Pyrotechnic
23/10/2021
"""

# Import libs
import os, sys
import random as r
import tkinter as tk

c_width, c_height = 500, 300
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()

# Global variables
limit: int = 30
timer_on: bool = True


# Function to generate possible cables with type check and no repetition
def generate_cable(N: int, colors: list[str]) -> list[list[str, bool]]:
    cable_stats: list[list[str, bool]] = []
    correct_cable_index = r.randrange(0, N)

    # Populate sequence
    for i in range(N):
        r_color: int = r.randrange(0, len(colors))
        cable_state: bool = True if i == correct_cable_index else False
        cable_stats.append([colors[r_color], cable_state])
        colors.pop(r_color)  # {Remove a used color}

    return cable_stats


# Possible colors, max number of cables
c: list[str] = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'purple']

# Generate a sequence with non repeating colors and with randomly chosen correct index
sequence: list[list[str, bool]] = generate_cable(r.randint(3, len(c)), c)


# Function to display the header of the file
def display_header(_font=lambda val: f"Helvetica {val} bold") -> None:
    canvas.create_text(c_width // 2, 30, text='Pyrotechnic', font=_font(30))
    canvas.create_text(c_width // 2, 60, text='select the right cable', font=_font(10))


# Display objects
def display_obj(d: int = 15) -> None:
    for i in range(len(sequence)):
        row: list[str, bool] = sequence[i]
        canvas.create_rectangle(50, 100 + i * d, 300, 100 + (i + 1) * d,
                                fill=row[0], tags=row[1], outline='')


# Create a recursive timer function
def timer() -> None:
    global limit  # {Global reference}
    canvas.delete('time')
    canvas.create_text(400, c_height // 2, text=str(limit),
                       tags='time', font='Helvetica 60 bold')
    limit -= 1

    # Call upon itself
    if limit > 0 and timer_on:
        canvas.after(1000, timer)


# Detect user click
def user_click(coords):
    global timer_on  # {Global reference]

    # Detect overlap with cursor
    overlap: tuple = canvas.find_overlapping(coords.x - 2, coords.y - 2, coords.x + 5, coords.y + 5)

    # Break out if no overlapping elements
    if not overlap:
        return

    # Receive status
    cable_state: str = canvas.gettags(overlap[0])[0]
    timer_on = False  # {Disable timer animation}

    # Show decision step - Unbind and destroy canvas
    canvas.create_text(c_width // 2, 250, text='You won!', font='Helvetica 20 bold') \
        if cable_state == '1' else canvas.destroy(), canvas.unbind_all('<Button-1>')


# Invoke dependent functions
display_header()
display_obj()
timer()

# Canvas attributes
canvas.bind_all('<Button-1>', user_click)

# Create a restart button
restart_button = tk.Button(text='Reset', command=lambda: os.execv(sys.argv[0], sys.argv))
restart_button.pack()
canvas.mainloop()
