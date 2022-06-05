import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

beginning = True
line = []


def load():
    global line, beginning
    with open("save.txt", "r") as inputFile:
        load_data = inputFile.readline().split()
    load_data = [int(d) for d in load_data]
    if len(load_data) != 0:
        line = load_data
        draw()
        beginning = False


def draw():
    global line
    canvas.create_line(line, tags="line")


def point(event):
    global line, beginning
    x, y = event.x, event.y
    if beginning:
        line = [x, y, x, y]
        draw()
        beginning = False
    else:
        line.append(x), line.append(y)
        canvas.coords("line", line)


def stretching(event):
    global line, beginning
    x, y = event.x, event.y
    if not beginning:
        temporal_line = line[:]
        temporal_line.append(x), temporal_line.append(y)
        canvas.coords("line", temporal_line)


def end(event):
    global line, beginning
    if not beginning:
        line.append(event.x), line.append(event.y)
        canvas.coords("line", line)
    beginning = True


def save():
    with open("save.txt", "w") as outputFile:
        for data in line:
            outputFile.write(str(data) + " ")
    exit()


def delete():
    file1 = open("save.txt", "w")
    file1.close()
    canvas.delete("line")


load()
canvas.bind("<Button-1>", point)
canvas.bind("<Double-Button-1>", end)
canvas.bind("<Motion>", stretching)
button1 = tkinter.Button(text="Save", command=save)
button2 = tkinter.Button(text="Delete", command=delete)
button1.pack()
button2.pack()
canvas.mainloop()
