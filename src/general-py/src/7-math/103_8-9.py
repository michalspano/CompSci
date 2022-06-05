import tkinter
import math
canvas = tkinter.Canvas(height=500, width=500, bg="white")
canvas.pack()

angle = 90
cx, cy, = 250, 250
r = 100


def click(c):
    global cx, cy
    canvas.delete("all")
    x = c.x
    y = c.y
    cx, cy = x, y
    dial(cx, cy, r)


def hand():
    global angle
    angle += 6
    C = (cx, cy)
    angle_rad = math.radians(angle)
    x = cx + math.sin(angle_rad) * r
    y = cy - math.cos(angle_rad) * r
    canvas.delete("hand")
    canvas.create_line(C, x, y, width=3, tags="hand")
    canvas.after(100, hand)


def dial(cx_1, cy_1, r_1):
    for i in range(1, 13):
        alpha = 90 - (i * 360 // 12)
        alpha_rad = math.radians(alpha)
        x = cx_1 + math.cos(alpha_rad) * (r_1 + 20)
        y = cy_1 - math.sin(alpha_rad) * (r_1 + 20)
        romans = ["I", "IV", "V", "IX", "X"]
        if i < 4:
            num = i * romans[0]
        elif i == 4:
            num = romans[1]
        elif 4 < i < 9:
            num = romans[2] + romans[0] * (i - 5)
        elif i == 9:
            num = romans[3]
        else:
            num = romans[4] + romans[0] * (i - 10)
        canvas.create_oval(cx_1 - 5, cy_1 - 5, cx_1 + 5, cy_1 + 5,
                           fill="red",
                           outline="")
        canvas.create_text(x, y, font="Arial 15 bold", text=num)


canvas.bind_all("<Button-1>", click)
dial(cx, cy, r)
hand()
canvas.mainloop()
