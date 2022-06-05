import tkinter
from random import *
canvas = tkinter.Canvas(width=610, height=270)
canvas.pack()

frog_width = 60

frogs = list(range(10))

for i in range(len(frogs)):
    which = randrange(10)
    frogs[i], frogs[which] = frogs[which], frogs[i]  # swaps frogs to random order


def draw_frog(x, y, number):
    canvas.create_line(x, y+55, x+50, y+55, width=3, fill="green")
    if number != 0:
        canvas.create_oval(x, y, x+50, y+50, fill="lightgreen", tags="frog")
        canvas.create_oval(x+7, y+28, x+43, y+38, fill="red", tags="frog")
        canvas.create_oval(x+7, y, x+22, y+15, fill="white", tags="frog")
        canvas.create_oval(x+28, y, x+43, y+15, fill="white", tags="frog")
        canvas.create_oval(x+11, y+7, x+19, y+15, fill="black", tags="frog")
        canvas.create_oval(x+31, y+7, x+39, y+15, fill="black", tags="frog")
        canvas.create_oval(x+35, y-20, x+60, y, fill="white", tags="frog")
        canvas.create_text(x+48, y-10, text=number, tags="frog")


def draw():
    canvas.delete("frog")
    for j in range(len(frogs)):
        draw_frog(j * frog_width + 10, 100, frogs[j])
        print(frogs[j])


def click(coord):
    global click_count
    index = (coord.x - 10) // frog_width
    empty = frogs.index(0)
    distance = abs(index - empty)
    if distance < 3 and 0 <= index <= 9:
        click_count += 1
        frogs[index], frogs[empty] = frogs[empty], frogs[index]
        draw()
        if winning_position():
            congratulations()
    display_click_count()


def winning_position():
    for k in range(len(frogs) - 1):
        if k != frogs[k] - 1:
            return False
    return True


def congratulations():
    canvas.create_text(300, 200, text="You won", font="Arial 50", fill="green")


def display_click_count():
    canvas.delete("count")
    global click_count
    canvas.create_text(100, 20, text=f"You clicked {click_count} times.", tags="count")


click_count = int()
draw()
canvas.bind_all("<Button-1>", click)
canvas.mainloop()
