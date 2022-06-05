import tkinter
import math
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()


#  Creates the initial point drawing
def robot(x, y):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                       fill="red", outline="", tags="robot")


#  Returns entry value after button-click
def entry_action():
    action = entry1.get()
    perform_action(action)


#  Function to determine all actions
def perform_action(ac):

    #  For single command
    if len(ac) < 2:
        action = ac.split()

    #  For sequence of commands
    else:
        action = ac.split(",")
        action = [acs.split() for acs in action]

    j = 0
    while j < len(action):

        #  Identifier, value of an action; [id, value]
        identifier = action[j][0]
        value = action[j][1]

        #  All possible identifiers and their functions
        if identifier == "right":
            right(value)

        elif identifier == "left":
            left(value)

        elif identifier == "line":
            add_line(value)

        elif identifier == "pencolor":
            pen_color(value)

        elif identifier == "penwidth":
            pen_width(value)

        elif identifier == "repeat":
            repeat(value, j, action)
        j += 1


#  Function for "right" module
def right(par):
    global angle_deg
    angle_deg -= int(par)


#  Function for "left" module
def left(par):
    global angle_deg
    angle_deg += int(par)


#  Function for "pencolor" module
def pen_color(par):
    global _pen_color
    _pen_color = par


#  Function for "penwidth" module
def pen_width(par):
    global _pen_width
    _pen_width = int(par)


#  Function for "repeat" module
def repeat(par, index, _action):
    # Syntax: [repeat, n, k]; n - number of repeats, k - number of influenced actions

    repeated_values = []  # Arr with repeated actions
    info = par.split(";")
    n, end = int(info[0]), int(info[1])  # [n, k]
    for i in range(n):  # Repetition n
        for k in range(end):  # Range of influenced actions k
            rep_val = _action[index + k + 1]
            repeated_values.append(rep_val)

    for r in range(len(repeated_values)):
        #  Inserts repeated values
        _action.insert(index + r + 1, repeated_values[r])


#  Loads data from a txt. file
def load_data():
    data = str()
    with open("R20_sequence.txt") as sequence:
        for seq in sequence:
            data += seq

    data = data.replace("\n", ", ")

    # Performs actions after data was loaded
    perform_action(data)


#  Mathematical function to draw lines
def add_line(length):
    global coords
    angle_rad = round((angle_deg / 180) * math.pi, 3)  # Converts the angle to RAD

    #  Calculation using the unit circle with radius of "length"
    new_x = coords[0] + (math.sin(angle_rad) * int(length))
    new_y = coords[1] + (math.cos(angle_rad) * int(length))
    coords.append(new_x), coords.append(new_y)
    canvas.create_line(coords, fill=_pen_color, width=_pen_width,
                       tags="t_line")
    # Stores the 2 last coords. only
    coords = coords[2:]


#  Exports the drawing - .eps (vector) file
def export():
    canvas.delete("robot")
    from datetime import datetime
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current time
    canvas.postscript(file=f"export{time}.eps")
    exit(f"Your image was saved at/ export{time}.eps")


#  Default values and widgets
coords = [int(canvas["height"]) / 2] * 2
angle_deg, _pen_width, _pen_color = 180, 1, "blue"  # Default values
robot(200, 200)
load_button = tkinter.Button(text="Load", width=5, height=2,
                             command=load_data)
load_button.pack()
entry1 = tkinter.Entry(bd=5)
entry1.pack()
entry_button = tkinter.Button(text="Done", width=5, height=2,
                              command=entry_action)
entry_button.pack()
export_button = tkinter.Button(text="Export", command=export)
export_button.pack()
canvas.mainloop()
