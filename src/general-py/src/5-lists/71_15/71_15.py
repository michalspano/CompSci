import tkinter
canvas = tkinter.Canvas(height=150, width=400)
canvas.pack()

with open("picture.txt", "r") as inputTextFile:
    n = [line.strip().split() for line in inputTextFile]

for i in range(len(n)):
    color_fill = n[i][-1]
    object_fill = n[i][1:-1]
    if n[i][0] == "r":
        canvas.create_rectangle(object_fill, fill=color_fill, outline=color_fill)
    elif n[i][0] == "o":
        canvas.create_oval(object_fill, fill=color_fill, outline=color_fill)

canvas.mainloop()
