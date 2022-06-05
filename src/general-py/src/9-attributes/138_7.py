import tkinter
from random import *

canvas = tkinter.Canvas(width=500, height=200)
canvas.pack()


def draw():
    for i in range(20):
        random_color = choice(("green", "yellow", "blue", "red", "pink", "violet", "brown"))
        canvas.create_rectangle(25 * i, 75, 25 + 25 * i, 100,
                                fill=random_color,
                                outline="")


def click(event):
    x, y = event.x, event.y
    enlarge = 15
    default()
    overlap = canvas.find_overlapping(x, y, x, y)

    if len(overlap) > 0:
        index = int(overlap[0])

        main_square = canvas.coords(index)
        trailing_square = canvas.coords(index - 1)
        leading_square = canvas.coords(index + 1)

        y1, y2 = main_square[1], main_square[3]  # Persistent variables

        if index == 1:  # Error handler for the first square
            canvas.coords(index + 1, [leading_square[0], y1 - (enlarge / 2),
                                      leading_square[2], y2 + (enlarge / 2)])

        elif index == 20:  # Error handler for the last square
            canvas.coords(index - 1, [trailing_square[0], y1 - (enlarge / 2),
                                      trailing_square[2], y2 + (enlarge / 2)])
        else:
            canvas.coords(index - 1, [trailing_square[0], y1 - (enlarge / 2),
                                      trailing_square[2], y2 + (enlarge / 2)])
            canvas.coords(index + 1, [leading_square[0], y1 - (enlarge / 2),
                                      leading_square[2], y2 + (enlarge / 2)])
        canvas.coords(index, [main_square[0], y1 - enlarge,
                              main_square[2], y2 + enlarge])


def default():  # Resets to default positions
    for identity in canvas.find_all():
        canvas.coords(identity, [25 * (identity - 1), 75, 25 * (identity - 1) + 25, 100])


draw()
canvas.bind_all("<Button1-Motion>", click)
canvas.mainloop()
