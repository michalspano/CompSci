import tkinter
from random import *
from collections import Counter
canvas = tkinter.Canvas(height=310, width=310)
canvas.pack()


#  Function to draw circles 10x10
def draw_circles(colors, w):
    for i in range(10):
        for j in range(10):
            pick_color = choice(colors)  # Chooses a rand. color for every circle
            canvas.create_oval(10 + i*w, 10 + j*w,
                               10 + i*w + w - 5, 10 + j*w + w - 5,

                               #  Assigns tags respective to the color
                               fill=pick_color, outline="",
                               tags=pick_color)

    #  Resets the txt. file upon initial call
    file1 = open("R15_progress.txt", "w")
    file1.close()
    progress_save()


def click(event, mode):
    global move_count
    move_count += 1

    x, y = event.x, event.y
    picked = canvas.find_overlapping(x, y, x, y)

    if len(picked) > 0:
        picked = picked[0]

        #  Left-click for column
        if mode == "left":
            column_ID = (int(picked) - 1) // 10

            for i in range(column_ID * 10, (column_ID * 10) + 10):
                current_tag = (i + 1)
                change_colors(current_tag)

        else:  # Right-click for row
            row_ID = (y - 10) // 30 + 1

            for i in range(10):
                current_tag = row_ID + (i * 10)
                change_colors(current_tag)

        configure_colors()
        progress_save()
        check()


#  Function to process diagonal event for 'Up' and 'Down 'keys
def diagonal_event(event):
    global move_count
    move_count += 1

    #  Configures diagonal 1 (1-100)
    if event.keysym == "Up":
        j = 0
        for i in range(0, 100, 10):
            j += 1
            current_tag = i + j
            change_colors(current_tag)

    #  Configures diagonal 1 (10-91)
    elif event.keysym == "Down":
        for current_tag in range(10, 100, 9):
            change_colors(current_tag)

    progress_save()
    configure_colors()


#  Function to change colors cyclically
def change_colors(par):
    color_tag = canvas.gettags(par)[0]
    current_color_index = color_order.index(color_tag) + 1  # Gets the index of current color + 1
    if current_color_index >= len(color_order):
        current_color_index = 0  # If the last index -> repeat
    canvas.itemconfig(par, tags=color_order[current_color_index])


#  Changes colors according to individual tags
def configure_colors():
    for ID in canvas.find_all():
        color = canvas.gettags(ID)[0]
        canvas.itemconfig(ID, fill=color)


#  Saves progress to txt. file
def progress_save():
    progress = []
    for ID in canvas.find_all():
        color_tags = canvas.gettags(ID)[0]
        progress.append(color_tags)

    #  Writes to a txt. file in a given format (["color1";"color2", ...], ...)
    with open("R15_progress.txt", "a") as output_progress:
        output_progress.write(";".join(progress) + "\n")


#  Checks for winning scenario (all circles of 1 color)
def check():
    colors = []
    for ID in canvas.find_all():
        colors.append(canvas.gettags(ID)[0])
    count = len(Counter(colors))

    #  All colors are the same (100% occurrence of a single color)
    if count == 1:
        end()


#  End scenario function
def end():
    canvas.destroy()
    endView = tkinter.Canvas(height=200, width=200, bg="black")
    endView.pack()

    #  Prints respective text layers
    endView.create_text(100, 80, text="YOU WON!",
                        fill="white", font="Arial 25 bold")
    endView.create_text(100, 110, text=f"Number of tries: {move_count}",
                        fill="white", font="Arial 15")


move_count = int()
color_order = ["red", "green", "blue"]  # Default colors for cyclical change
draw_circles(color_order, 30)
#  Lambda function for 2 different events
canvas.bind("<Button-1>", lambda event: click(event, "left"))
canvas.bind("<Button-2>", lambda event: click(event, "right"))
canvas.bind_all("<Key>", diagonal_event)
canvas.mainloop()
