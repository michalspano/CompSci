import tkinter
import math
from random import *
canvas = tkinter.Canvas(bg="black")
canvas.pack()


di = int(input("Canvas dimensions: "))


def dimensions(d):
    canvas["height"] = d
    canvas["width"] = d
    draw()


def draw():
    global c_count
    c_count += 1
    x = randint(0, di)
    y = randint(0, di)

    # check condition
    S = (di//2, di//2)
    d = round(math.sqrt((S[0] - x) ** 2 + (S[1] - y) ** 2), 2)
    parameter = di // 10
    k = d // parameter
    if k % 2 == 0:
        c = "red"
    else:
        c = "white"
    w = (di // 80)
    canvas.create_oval(x - w, y - w, x + w, y + w, fill=c, outline="")
    if c_count <= 2000:
        canvas.after(10, draw)
    else:
        print("Finished.")


c_count = 0
dimensions(di)
canvas.mainloop()
