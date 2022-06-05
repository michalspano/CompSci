"""
Michal Špano
8. Find the Cracked Plate
11/09/2021
"""

import tkinter as tk
from random import randint
c_width, c_height = 610, 100  # Define fixed size of canvas
canvas = tk.Canvas(height=c_height, width=c_width)
canvas.pack()

# Define constant size of a plate
WIDTH: int = 60

# Define empty dict to store the progress
progress_data: dict = {}

# Decide on random broken index
broken_plate_index = randint(1, 10)


# Create a function to draw a plate
def plate(x, id):
    # Assign 'plate' tags to plates only
    canvas.create_oval(x + 5, 20, x + 5 + WIDTH, 20 + WIDTH, fill='blue', tag=('plate', id))
    canvas.create_text(x + 35, 50, text=chr(id + 64))


# Invoke draw in a loop
for i in range(10):
    plate(x=i * 60, id=i + 1)


# Create a function to receive the user click
def user_click(coords):
    x, y = coords.x, coords.y

    # Detect overlapping canvas objects (with user click)
    overlap = canvas.find_overlapping(x - 2 ,y - 2,x + 2 ,y + 2)

    # Iterating over the tuple (both ovals and text have an assigned tag) -> prevents error
    for tag in overlap:

        # Get the tags of the object
        current_tags = canvas.gettags(tag)

        # Check if plate tag is present
        if 'plate' in current_tags:
            object_tag: int = int(current_tags[1])

            # Store progress in a dict
            progress(chr(object_tag + 64))

            # Check if broken plate was found
            if check(object_tag, broken_plate_index):
                won()


# Determine whether match was made and return bool
def check(current, win) -> bool:
    return True if current == win else False


# Function to store the user's progress
def progress(key):
    global progress_data
    
    # Check whether the current plate was already selected
    if key not in progress_data:
        progress_data[key] = 0

    # Increment the key's counter
    progress_data[key] += 1


# Winning position function
def won():
    canvas.delete('all')
    canvas.create_text(c_width / 2, c_height / 2 - 25, text="Congratulations!\nPlate clicked multiple times:")

    i = 0
    # Show all plates selected multiple times
    for plate in progress_data:
        if progress_data[plate] != 1:
            canvas.create_text(20 * i + 50, c_height / 2, text=plate)
            i += 1


canvas.bind_all("<Button-1>", user_click)
canvas.mainloop()
