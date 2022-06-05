import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

# Exercise 9) using lists


def build(inp):
    if inp > (int(canvas["height"]) - 10) / 10:
        inp = 39
    for i in range(inp):
        building.append(randint(0, 30))
        colors.append(choice(["red", "green", "blue"]))


def draw(data, c):
    max_canvas = int(canvas["height"])
    for i in range(len(data)):
        for h in range(data[i]):
            canvas.create_rectangle(i * 10 + 10, - (h * 10) + max_canvas,
                                    i * 10 + 20, - (h * 10) + max_canvas - 10,
                                    fill=c[i])


def animation():
    canvas.delete("all")
    building.insert(0, building[-1]), building.pop(-1)
    colors.insert(0, colors[-1]), colors.pop(-1)
    draw(building, colors)

    canvas.after(200, animation)


building, colors = list(), list()
build(int(input("Number of buildings: ")))
draw(building, colors)
button1 = tkinter.Button(text="Animation", width=7, height=2, command=animation)
button1.pack(side="left")
canvas.mainloop()
