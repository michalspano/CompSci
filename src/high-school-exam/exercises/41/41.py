#!/usr/bin/env python3

"""
Michal Špano
41. Ordering meals
19/10/2021
"""

import tkinter as tk
c_width, c_height = 500, 250
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()

# Define output path and generate new file
out_path: str = 'orders.txt'
output_file = open(out_path, 'w').close()


# Define main function
def main() -> None:
    i: int = 0  # {Counter}
    canvas.create_text(int(canvas['width']) // 2, 25, text='CHOOSE A MEAL!')
    r_dim: int = c_width // 4  # {Fixed size of an obj}

    # Create 4 possible buttons
    for color in ['green', 'red', 'blue', 'orange']:
        canvas.create_rectangle(i * r_dim + 5, 55,
                                (i + 1) * r_dim - 5, 50 + r_dim - 5,
                                fill=color, tags=color)
        i += 1


# Get user choice from a click
def user_click(event) -> None:
    if meal_entry.get().strip() == '':  # {Ignore blank of white spaces}
        return

    # Get current tags' cursor
    overlap: tuple = canvas.find_overlapping(event.x - 5, event.y - 5, event.x + 5, event.y + 5)
    if len(overlap) == 1:  # {Detects an object}
        ID = canvas.itemconfig(overlap[0], 'fill')[-1]  # {Get the color of the obj}
        write(meal_entry.get().strip(), ID)  # {Write}


# Function to write to a local txt file
def write(code: str, m_type: str) -> None:
    with open(out_path, 'a') as f:
        f.write(f'{code} {m_type}\n')


# Invoke main function
if __name__ == '__main__':
    main()
    # Tk Attributes GLOBAL
    label1 = tk.Label(text="Student's code")
    meal_entry = tk.Entry()
    label1.pack(), meal_entry.pack()
    canvas.bind_all('<Button-1>', user_click)
    canvas.mainloop()
