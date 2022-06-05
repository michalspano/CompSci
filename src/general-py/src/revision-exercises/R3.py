import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

#  Since tkinterPhotoImage has only one x,y coord;
#  we will make it move instead of scaling

flowers = []
for f in range(3):
    flowers.append(tkinter.PhotoImage(file=f"flowers/flower{f + 1}.png"))


def create_flowers(r, s):
    for i in range(r):
        c_width = int(canvas["width"])
        x, y = randint(s, c_width - s), randint(s, c_width - s)

        random_flower = choice(flowers)
        if random_flower == flowers[0]:
            tag = "flower1"
        elif random_flower == flowers[1]:
            tag = "flower2"
        else:
            tag = "flower3"

        canvas.create_image(x, y, image=random_flower,
                            tags=(str(i), tag))


def wilting():
    global flower_count
    obj_count = len(canvas.find_all())
    canvas_edge = int(canvas["height"])
    if obj_count > 0:
        for ID in canvas.find_all():
            c = canvas.coords(ID)
            if c[1] <= canvas_edge:
                canvas.coords(ID, [c[0] + randint(-1, 1)], c[1] + 2)
            else:
                flower_count.set(flower_count.get() - 1)
                canvas.delete(ID)
        canvas.after(obj_count * 30, wilting)
    else:
        canvas.destroy(), label1.destroy()
        end = tkinter.Canvas(height=300, width=300)
        end.pack()
        end.create_text(150, 150, text=f"You lost!\nScore: {score_count}.",
                        font="Arial 20 bold")


def click(event):
    global score_count
    x, y = event.x, event.y
    click_over = canvas.find_overlapping(x, y, x, y)

    if len(click_over) > 0:
        click_over = click_over[0]
        c = canvas.coords(click_over)
        flower_ID = canvas.gettags(click_over)[1]
        score_count += int(flower_ID[-1])
        push_up = int(flower_ID[-1]) * 15
        canvas.coords(click_over, [c[0], c[1] - push_up])
    else:
        print("No flower was selected.")


score_count = int()
create_flowers(randint(15, 30), 30)
wilting()

flower_count = tkinter.IntVar()
flower_count.set(len(canvas.find_all()))
label1 = tkinter.Label(textvariable=flower_count)
label1.pack()
canvas.bind("<Button-1>", click)
canvas.mainloop()
