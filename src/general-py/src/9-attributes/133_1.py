import tkinter
from random import *
import time
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()


def default():
    canvas.create_rectangle(100, 100, 200, 190, fill="blue")
    canvas.create_rectangle(250, 200, 350, 290, fill="red")
    canvas.create_oval(120, 220, 190, 290, fill="yellow")
    canvas.create_oval(270, 120, 340, 190, fill="green")
    canvas.create_line(100, 350, 150, 300, 200, 350, 100, 350, width=3)
    canvas.create_polygon(250, 350, 300, 300, 350, 350, fill="orange")
    canvas.create_text(200, 50, text="Shape attributes", font="Arial 20")
    canvas.create_text(200, 70, text="Text sample 1", font="Helvetica 10")
    canvas.create_text(150, 10, text="", tags="a")


def shrink(s):
    shapes = canvas.find_all()
    for shape in shapes:
        if canvas.type(shape) == "rectangle" or canvas.type(shape) == "oval":
            coordinates = canvas.coords(shape)
            x1, y1, x2, y2 = coordinates
            center_x = (x2 + x1) / 2
            n_width = (x2 - x1) / s
            center_y = (y2 + y1) / 2
            n_height = (y2 - y1) / s
            new_coordinates = [center_x - n_width, center_y - n_height,
                               center_x + n_width, center_y + n_height]
            canvas.coords(shape, new_coordinates)


def reverse():
    shapes = canvas.find_all()
    for shape in shapes:
        if canvas.type(shape) == "text":
            text = canvas.itemcget(shape, "text")
            r_text = text[::-1]
            canvas.itemconfig(shape, text=r_text)


def animation():
    for i in range(20):
        r = choice((1, 4))
        shrink(r)
        time.sleep(0.1)
        canvas.update()


def mouse(event):
    x1, y1, x2, y2 = event.x - 5, event.y - 5, event.x + 5, event.y + 5
    under_cursor = canvas.find_overlapping(x1, y1, x2, y2)
    info = f"You are under shape(s) number: {under_cursor}"
    canvas.itemconfig("a", text=info)


default()
canvas.bind("<Motion>", mouse)
button1 = tkinter.Button(text="Shrink", command=lambda: shrink(4))
button3 = tkinter.Button(text="Undo shrink", command=lambda: shrink(1))
button4 = tkinter.Button(text="Animation", command=animation)
button2 = tkinter.Button(text="Reverse text", command=reverse)
button1.pack(side="left")
button3.pack(side="left")
button4.pack(side="left")
button2.pack(side="left")
canvas.mainloop()
