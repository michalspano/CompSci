import tkinter
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()


def add_ball(event):
    global count
    count += 1

    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                       fill="green", outline="")


def animation():
    if count <= 100:
        for ID in canvas.find_all():
            c = canvas.coords(ID)
            y1, y2 = c[1], c[3]

            if y2 >= int(canvas["height"]):
                y1, y2 = 0, 10
            canvas.coords(ID, [c[0], y1 + 2, c[2], y2 + 2])

        canvas.after(50, animation)
    else:
        exit("The maximum has been reached.")


def reset():
    global count
    count = 0
    canvas.delete("all")


count = int()
animation()
button1 = tkinter.Button(text="Reset", width=5, height=2, command=reset)
button1.pack(side="left")
canvas.bind("<Button-1>", add_ball)
canvas.mainloop()
