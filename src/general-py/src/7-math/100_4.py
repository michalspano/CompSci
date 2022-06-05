import tkinter
import math
canvas, inst = tkinter.Canvas(), tkinter.Canvas(bg="gray")
canvas.pack()
inst.pack()


coord = input("Coordinates of circle separated by a space (4): ").split()
coord = [int(c) for c in coord]
x1, y1, x2, y2 = coord[0], coord[1], coord[2], coord[3]


def update_canvas():
    canvas["height"] = y2 + y1 + 10
    canvas["width"] = x2 + x1 + 10
    inst["width"] = x2 + x1 + 10
    inst["height"] = 40


update_canvas()


def draw_circle(a1, b1, a2, b2):
    canvas.create_oval(a1, b1, a2, b2, fill="black")


def click(c):
    global text
    x = c.x
    y = c.y

    mid_point = (x2 - x1) // 2 + x1
    d = math.sqrt((mid_point-x) ** 2 + (mid_point-y) ** 2)

    if d > ((x2 - x1) // 2):
        text = "OUT"
    else:
        text = "IN"
    draw_label()


def draw_label():
    inst.delete("label")
    inst.create_text(x2 / 2 + 5, 20, text=text, tags="label")


text = str()
canvas.bind_all("<Button-1>", click)
draw_circle(x1, y1, x2, y2)
canvas.mainloop()
