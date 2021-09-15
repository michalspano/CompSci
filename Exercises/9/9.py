"""
Michal Špano
9. Boat Race
15/09/2021
"""

# Import used libs'
import tkinter as tk
import random as r

# Include constant typing
from typing import final

# Define canvas bounds
c_width, c_height = 500, 500

# Create global canvas
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()

# Store individual locations in a list (start position of x = 20)
NUMBER_OF_BOATS: final = 15
start_x: int = 20
boat_pos: list = [start_x] * NUMBER_OF_BOATS


# Define function to draw a boat
def boat(x: int, y: int):

    # Create random sail int
    sail: int = r.randint(-3, 3)
    canvas.create_line(x, y, x, y - 25, x + 10 + sail, y - 10, x, y - 5, tags='boat')

    # Draw the base of the boat
    canvas.create_polygon(x - 20, y, x + 20, y, x + 10, y + 8, x - 10, y + 8, tags='boat')


# Create a function to display all boats
def display_boats():

    # Iterate in a specified range
    for i in range(NUMBER_OF_BOATS):

        # Display each boat
        boat(boat_pos[i], i * 32 + 30)


# Detect user click
def start_click(argv):
    global start_detected

    # Create a bool switch (resume and start animation)
    if not start_detected and not end_race:
        start_detected = True
        state = 'ON'
    else:
        start_detected = False
        state = 'OFF'

    # LOG STATUS
    print(f'Animation is: {state}')
    race()


# Create a function to start and process race
def race():
    global start_detected

    # Continue race if start is switched to True
    if start_detected:

        # Delete all previous boats
        canvas.delete('boat')

        # Iterate in a loop
        for i in range(NUMBER_OF_BOATS):

            # Assign random speed to each boat
            random_speed: int = r.randint(1, 5)
            boat_pos[i] += random_speed

            # Detect winning position
            if boat_pos[i] > c_width - 15:

                # Call win function with winning index
                win_position(i + 1)
                start_detected = False

        # Display boats and recursively call the function
        display_boats()
        canvas.after(50, race)


# Create a function to show winner
def win_position(win_index: int):
    global end_race
    end_race = True  # -> Prevent animation snapping
    win_msg: str = f'The winner is boat: \nnumber {win_index}'
    canvas.create_text(c_width / 2, c_height / 2, text=win_msg, font='Arial 20 bold')


# Create a function to display the winning line
def display_winning_line(bound: int):
    canvas.create_line(bound, 0, bound, c_height, width=5, fill='green')


# Call static functions
display_boats(), display_winning_line(c_width - 30)

# Create a bool-type to start current state of a switch
start_detected: bool = False

end_race: bool = False  # -> bool to prevent animation snapping

canvas.bind_all("<Button-1>", start_click)
canvas.mainloop()
