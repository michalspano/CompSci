import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()


def create_flowers(r, s, store):
    for i in range(r):
        c_width = int(canvas["width"])
        x, y = randint(s, c_width - s), randint(s, c_width - s)
        cords = [x - s, y - s, x + s, y + s]

        canvas.create_oval(cords,
                           fill="red",
                           tags=f"f{r + 1}",
                           outline="")
        store.append(cords)


def wilting():
    global counter, flower_count
    counter += 1
    obj_count = len(canvas.find_all())

    if obj_count > 0:
        for ID in canvas.find_all():
            c = canvas.coords(ID)
            if c[2] - c[0] > 0:
                canvas.coords(ID, [c[0] + 2, c[1] + 2, c[2] - 2, c[3] - 2])
            else:
                canvas.delete(ID)
                flower_count.set((flower_count.get() - 1))
        canvas.after(obj_count * 50, wilting)
    else:
        canvas.destroy(), label1.destroy()
        end = tkinter.Canvas(height=300, width=300)
        end.pack()
        end.create_text(150, 150, text=f"You lost!\nScore: {counter}xp.",
                        font="Arial 20 bold")


def click(event):
    x, y = event.x, event.y
    click_over = canvas.find_overlapping(x, y, x, y)

    if len(click_over) > 0:
        click_over = click_over[0]
        def_val_index = default_values[click_over - 1]
        canvas.coords(click_over, def_val_index)
    else:
        print("No flower was selected.")


default_values, counter = list(), int()
create_flowers(randint(15, 30), 26, default_values)
wilting()

flower_count = tkinter.IntVar()
flower_count.set(len(canvas.find_all()))
label1 = tkinter.Label(textvariable=flower_count)
label1.pack()
canvas.bind("<Button-1>", click)
canvas.mainloop()
