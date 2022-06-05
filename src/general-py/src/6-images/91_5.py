import tkinter
from random import *
canvas = tkinter.Canvas(width=1000, height=200)
canvas.pack()

#  1-8: Fruits, 9-16: Vegetables


def load_data(s, data, filetype):
    while len(data) < 9:
        r = randint(1, 16)
        if r not in data:
            data.append(r)
    for j in range(len(data)):
        path = tkinter.PhotoImage(file=f"Images/91_5/oz_{data[j]}{filetype}")
        s.append(path)

    s.append(None)
    data.append(0)
    fruit_check()


def draw_items(x, y):
    canvas.delete("img")
    for img in sequence:
        canvas.create_image(x, y, image=img, anchor="nw", tags="img")
        x += 100


def draw_shelf():
    for i in range(10):
        canvas.create_line(10 + i*100, 130, 10 + i*100 + 80, 130, fill="black")


def click(coord):
    global sequence, data_collection
    x = coord.x
    pick_index = x // 100
    click_counter()

    empty_shelf = sequence.index(None)
    distance = abs(pick_index-empty_shelf)
    if distance <= 2:
        sequence[pick_index], sequence[empty_shelf] = sequence[empty_shelf], sequence[pick_index]
        data_collection[pick_index], data_collection[empty_shelf] = \
            data_collection[empty_shelf], data_collection[pick_index]
    draw_items(10, 40)
    progress_check()


def click_counter():
    global click_count
    canvas.delete("count")
    click_count += 1
    canvas.create_text(500, 170,
                       text=f"Count: {click_count}", font="Arial 15", tags="count")


def fruit_check():
    global fruit_count
    for fruit in data_collection:
        if 0 < fruit <= 8:
            fruit_count += 1


def progress_check():
    check_value = 0
    for j in range(fruit_count):
        if 0 < data_collection[j] <= 8:
            check_value += 1
    if check_value == fruit_count and data_collection[-1] == 0:
        win()


def win():
    canvas.destroy()
    end = tkinter.Canvas(width=200, height=200)
    end.pack()
    end.create_text(100, 100, text="You won!", font="Arial 30 bold")


sequence = []
data_collection = []
fruit_count, click_count = int(), int()
load_data(sequence, data_collection, ".png")
draw_items(10, 40)
draw_shelf()
click_counter()
canvas.bind_all("<Button-1>", click)
canvas.mainloop()
