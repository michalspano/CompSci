import tkinter
from random import *

canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

numberOfCubes = int(input("Number of cubes: "))
cubeDimensions = int(input("Dimension: "))


def editCanvas():
    canvas["height"] = cubeDimensions * 3
    canvas["width"] = numberOfCubes * cubeDimensions


editCanvas()
n = [i * cubeDimensions for i in range(numberOfCubes + 1)]
random_color = [choice(("red", "blue", "green", "cyan", "magenta", "yellow", "brown", "purple", "pink"))
                for i in range(numberOfCubes)]
grow = 0


def squares(d):
    global grow, n, random_color
    for i in range(len(n) - 1):
        canvas.create_rectangle(n[i], d - grow, n[i] + d, d * 2 + grow, fill=random_color[i], outline="white")


def hover(cord):
    canvas.delete("growth")
    global n, grow, cubeDimensions
    d = cubeDimensions
    x = cord.x
    y = cord.y
    last_cube = int(len(n))

    if cubeDimensions < y < cubeDimensions * 2:
        if x > n[int(len(n)) - 1]:
            canvas.delete("growth")
        elif n[0] < x < n[1]:

            grow = cubeDimensions // 3
            partial_growth = grow / 3
            canvas.create_rectangle(n[0], d - grow, n[0] + d, d * 2 + grow,
                                    fill=random_color[0], outline="white", tags="growth")
            canvas.create_rectangle(n[1], d - partial_growth, n[1] + d, d * 2 + partial_growth,
                                    fill=random_color[1],
                                    outline="white",
                                    tags="growth")
        elif n[last_cube - 2] < x < n[last_cube - 1]:
            grow = cubeDimensions // 3
            partial_growth = grow / 3
            canvas.create_rectangle(n[last_cube - 2], d - grow, n[last_cube - 2] + d, d * 2 + grow,
                                    fill=random_color[len(random_color) - 1],
                                    outline="white",
                                    tags="growth")
            canvas.create_rectangle(n[last_cube - 3], d - partial_growth, n[last_cube - 3] + d,
                                    d * 2 + partial_growth,
                                    fill=random_color[len(random_color) - 2],
                                    outline="white",
                                    tags="growth")

        else:
            for i in range(len(n)):
                while n[i] < x < (n[i + 1]):
                    grow = cubeDimensions // 3
                    partial_growth = grow / 3
                    canvas.create_rectangle(n[i], d - grow, n[i] + d, d * 2 + grow,
                                            fill=random_color[i], outline="white", tags="growth")
                    canvas.create_rectangle(n[i - 1], d - partial_growth, n[i - 1] + d, d * 2 + partial_growth,
                                            fill=random_color[i - 1], outline="white",
                                            tags="growth")
                    canvas.create_rectangle(n[i + 1], d - partial_growth, n[i + 1] + d, d * 2 + partial_growth,
                                            fill=random_color[i + 1],
                                            outline="white",
                                            tags="growth")
                    break


squares(cubeDimensions)
canvas.bind('<Button1-Motion>', hover)
canvas.mainloop()
