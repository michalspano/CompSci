import tkinter
import math
canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()


def click(coord):
    global click_count, lengths
    click_count += 1
    x = coord.x
    y = coord.y

    if click_count <= 3:
        lengths.append((x, y))
        draw()
    if click_count == 2:
        draw_line()
        distance_calculator()

    elif click_count == 3:
        draw_triangle()

    elif click_count > 3:
        canvas.delete("all")
        click_count = 0
        lengths.clear()


def draw():
    x = lengths[click_count-1][0]
    y = lengths[click_count-1][1]
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black", tags="v")


def distance_calculator():
    draw_line()
    if len(lengths) == 2:
        distance = round(math.sqrt((lengths[1][0] - lengths[0][0]) ** 2 +
                                   (lengths[1][1] - lengths[0][1]) ** 2), 2)
        canvas.create_text(30, 20, text=distance, tags="d")
    else:
        print("Need 2 x,y coordinates to calculate distance.")


def draw_line():
    global A, B
    A = lengths[0]
    B = lengths[1]
    canvas.create_line(A, B, width=2)


def draw_triangle():
    global C
    canvas.delete("v", "d")
    C = lengths[2]
    canvas.create_line(A, B, width=2)
    canvas.create_line(B, C, width=2)
    canvas.create_line(A, C, width=2)
    circumference()
    area()
    draw_median()


def circumference():
    global a, b, c

    a = round(math.sqrt((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2), 2)
    b = round(math.sqrt((C[0] - A[0]) ** 2 + (C[1] - B[1]) ** 2), 2)
    c = round(math.sqrt((C[0] - A[0]) ** 2 + (C[1] - B[1]) ** 2), 2)
    O_circumference = a + b + c
    print(f"Circumference: {O_circumference} cm.")


def area():
    s = (a + b + c) / 2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area: {round(Area, 2)} cm2.")


def draw_median():
    Sa = [(B[i] + C[i]) / 2 for i in range(2)]
    Sb = [(A[i] + C[i]) / 2 for i in range(2)]
    Sc = [(A[i] + B[i]) / 2 for i in range(2)]
    canvas.create_line(A, Sa, width=1.5, fill="green")
    canvas.create_line(B, Sb, width=1.5, fill="green")
    canvas.create_line(C, Sc, width=1.5, fill="green")


click_count = 0
lengths = []
A, B, C = list(), list(), list()
a, b, c = float(), float(), float()
canvas.bind_all("<Button-1>", click)
canvas.mainloop()
