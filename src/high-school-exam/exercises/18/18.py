"""
Michal Špano
18. Drawing Robot 1
26/09/2021
"""

# Import libs
import math
import tkinter as tk
from typing import final

# Define constant canvas dimensions
c_width: final = 400
c_height: final = 400

# Predefine possible commands
keywords: list = ['line', 'left', 'right']

"""
An angle pointing upwards (in Tk env) shall have y coord. negative
"""
current_angle: int = -90  # {In DEG}

# Create canvas
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()


# Define main function
def main():
    # Define robots mid point
    canvas.create_line(c_width / 2, c_height / 2,
                       c_width / 2, c_height / 2,
                       fill='red', tags='line')


# Detect button click
def button_click():
    entry_data = process_entry_input()
    # Indicate correct usage
    commands(entry_data) if entry_data is not None else error()


# Create a function to be called upon button click
def process_entry_input() -> str or list:
    if entry.get() == '':  # {Detect empty entry}
        return
    # Return parsed command
    command: list = entry.get().split()
    return command


# Function to evaluate commands
def commands(command_sequence: list):
    global current_angle

    # Receive action type
    action = command_sequence[0].strip().lower()

    # 1 member sequence -> change angle
    if len(command_sequence) == 1:
        # Check if it belongs to the predefined keywords
        if action in keywords[1:]:
            if action == keywords[1]:  # {Left}
                current_angle -= 90
            elif action == keywords[2]:  # {Right}
                current_angle += 90
        else:
            error()

    # 2 member sequence -> draw line
    elif len(command_sequence) == 2:
        if action == keywords[0]:  # {Check if correct command 'line'}
            draw_line(int(command_sequence[1])) if command_sequence[1].isdigit() else error()
    else:
        error()


"""
Using standard trigonometry to compute coords.
Computing of new coords based on the principle of a unit circle.
Unit circle: https://en.wikipedia.org/wiki/Unit_circle
"""


def draw_line(d):
    line_coords = canvas.coords('line')  # {Receive current line coordinates}
    # Split to current x and y
    current_x, current_y = line_coords[-2], line_coords[-1]

    # Create new x and y using math lib
    new_x = d * math.cos(math.radians(current_angle)) + current_x
    new_y = d * math.sin(math.radians(current_angle)) + current_y
    line_coords.append(new_x), line_coords.append(new_y)
    canvas.coords('line', line_coords)  # {Append to coords list}


# Static error msg
def error():
    print('Incorrect usage')


# Invoke main function
if __name__ == '__main__':
    main()

# Show tk elements
entry = tk.Entry()
entry.pack(), entry.focus()  # -> {Set up autofocus}
command_button = tk.Button(text='Do', command=button_click)
command_button.pack()
canvas.mainloop()
