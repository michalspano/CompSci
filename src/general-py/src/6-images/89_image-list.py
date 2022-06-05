import tkinter
from random import *
from collections import Counter

images, roll = list(), list()
dice_count = int(input("Number of dice: "))
g_switch = True
canvas = tkinter.Canvas(width=int(), height=150)
canvas.pack()


def update_canvas(d):
    canvas["width"] = 10 + (d * 100)


def load(filetype):
    shift = 0
    if not g_switch:
        shift = 6
    for i in range(1, 7):
        path = tkinter.PhotoImage(file=f"Images/90-3_4/die_{str(i + shift)}{filetype}")
        images.append(path)


def draw(x, y):
    for j in range(dice_count):
        index = roll[j] - 1
        canvas.create_image(x, y, image=images[index], anchor="nw", tags="die")
        x += 100


def animation():
    global roll
    roll.clear()
    canvas.delete("die")
    for i in range(dice_count):
        roll.append(randint(1, 6))
    draw(10, 30)
    canvas.after(500, animation)


def key(event):
    logic()
    canvas.delete("points")
    canvas.create_text((dice_count * 100) // 2, 10, text=points, tags="points")


def logic():
    global points
    data_medium = len(Counter(roll))
    if dice_count == 2:
        if data_medium == 1:
            points += 1
        else:
            points -= 1
    elif dice_count == 3:
        if data_medium == 1:
            points += 2
        elif data_medium == 2:
            points += 1
        else:
            points -= 1
    elif dice_count > 3:
        if data_medium == 1:
            points += 3
        elif data_medium == 2:
            points += 2
        elif data_medium == 3:
            points += 1
        else:
            points -= 1
    else:
        print("Error! Min. is 2. {RESTART}")


def dice_graphics():
    global g_switch, images
    images.clear()
    g_switch = True
    load(".png")


def weather_graphics():
    global g_switch, images
    images.clear()
    g_switch = False
    load(".png")


points = 0
update_canvas(dice_count)
load(".png")
animation()
button1 = tkinter.Button(text="Dice", width=10, command=dice_graphics)
button1.pack(side="left")
button2 = tkinter.Button(text="Weather", width=10, command=weather_graphics)
button2.pack(side="left")
canvas.bind_all("<space>", key)
canvas.mainloop()
