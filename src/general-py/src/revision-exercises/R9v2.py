import tkinter
from random import *
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

# Exercise 9) using tags and attributes


def build(inp, _max):
    if inp > (int(canvas["height"]) - 10) / 10:
        inp = 39
    for i in range(inp):
        building.append(randint(0, _max))
    draw(building, 10)


def draw(data, w):

    #  Creates buildings with custom tags in a nested loop
    max_canvas = int(canvas["height"])
    for i in range(len(data)):

        #  Picks a random color for every building, not a story
        color_tag = choice(["red", "green", "blue"])
        for h in range(data[i]):
            canvas.create_rectangle(i * w + w, - (h * w) + max_canvas,
                                    i * w + (w * 2), - (h * w) + max_canvas - w,
                                    tags=color_tag)

    #  Changes the filling based on the tag
    for ID in canvas.find_all():
        tag_fill = canvas.gettags(ID)[0]
        canvas.itemconfig(ID, fill=tag_fill)


def animation():

    #  Trailing x-value from the last building
    max_value = len(building) * 10 + 20
    for ID in canvas.find_all():
        c = canvas.coords(ID)
        x1, x2 = c[0], c[2]

        #  Detects for trailing x-value; push to start
        if x2 >= max_value:
            x1, x2 = 10, 20

        #  Moves for every attribute
        canvas.coords(ID, [x1 + 10, c[1], x2 + 10, c[3]])
    canvas.after(200, animation)


building = list()
build(int(input("Number of buildings: ")), 30)
button1 = tkinter.Button(text="Animation", width=7, height=2, command=animation)
button1.pack(side="left")
canvas.mainloop()
