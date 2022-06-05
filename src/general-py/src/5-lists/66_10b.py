import tkinter
from random import *

canvas = tkinter.Canvas(height=300, width=300)
canvas.pack()

colors = []


def button1_click():
    pickRandomColors()


def pickRandomColors():
    global colors
    colors.clear()
    colors = [choice(("red", "green", "blue")) for i in range(len(entry1.get()))]
    colorShift()


def colorShift():
    canvas.delete("displaytext")

    # appends first color + removes last color
    colors.append(colors[0])
    colors.pop(colors.index(colors[-1]))
    text()
    canvas.after(500, colorShift)


def text():
    displaytext = entry1.get()
    for i in range(len(displaytext)):
        canvas.create_text(20 + i * 20, 300 / 2, text=displaytext[i], tags="displaytext",
                           fill=colors[i], font="Arial 20")


label1 = tkinter.Label(text="Input to display")
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text="OK", command=button1_click)
button1.pack()
canvas.mainloop()
