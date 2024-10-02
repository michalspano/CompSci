"""
Michal Špano
1. Baby Snake
07/09/2021
"""

# Import tkinter and create a canvas to display the game
import tkinter
canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()


# Define snake's run
def run():
    global x_head, y_head, collision

    # Increment the head of the snake
    x_head += x
    y_head += y
    
    # Get the current coords of the snake, i.e. the whole line stored in a list
    c = canvas.coords("snake")

    # Get the x and y coordinates respectively (using slices) in separate lists
    cord_x, cord_y = c[::2], c[1::2]

    i = 0
    while i < len(cord_x) and not collision:

        """
        To detect collision:
        If any of the coordinates match the current head of the snake -> collision detected
        """
        if cord_x[i] == x_head and cord_y[i] == y_head:
            collision = True
        i += 1

        # Detect if head is touching the frame borders
        coords: list = [x_head, y_head]

        # Collision -> True
        for head in coords:
            if head <= 0 or head >= int(canvas['width']):
                collision = True

    # If collision was not detected -> continue in a cycle
    if not collision:

        # Append the current head to the snake (leave a mark as a line)
        c.append(x_head), c.append(y_head)

        # Update the coordinates in the canvas
        canvas.coords("snake", c)

        # Recursively call the function with a time delay
        canvas.after(10, run)

    # Close if collision was found
    else:
        canvas.destroy()
        exit("Collision detected.")


# Create a function to shift the move depending on the key
def key(event):
    global x, y
    if event.keysym == "Left":
        x, y = -1, 0
    elif event.keysym == "Right":
        x, y = 1, 0
    elif event.keysym == "Up":
        x, y = 0, -1
    elif event.keysym == "Down":
        x, y = 0, 1


# Create a collision bool value
collision: bool = False

# Initial coordinates of the head
x_head = y_head = int(canvas['width']) / 2

# Define moving on x and y axis (heading north by default -> y = -1)
x, y = 0, -1

# Create snake's steps
canvas.create_line(x_head, y_head, x_head, y_head, tags="snake")

# Create main executable
if __name__ == '__main__':
    run()
    canvas.bind_all("<Key>", key)
    canvas.mainloop()
