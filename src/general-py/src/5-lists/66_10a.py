import tkinter
from random import *
canvas = tkinter.Canvas(height=300, width=300)
canvas.pack()

colors = []


def button1_click():
    pickRandomColors()


def pickRandomColors():
    global colors
    canvas.delete("displaytext")
    colors.clear()
    colors = [choice(("green", "blue", "red")) for i in range(len(entry1.get()))]
    text()
    canvas.after(400, pickRandomColors)


def text():
    displaytext = entry1.get()
    for i in range(len(displaytext)):
        canvas.create_text(20 + i*20, 300 / 2, text=displaytext[i], tags="displaytext",
                           fill=colors[i], font="Arial 20")


label1 = tkinter.Label(text="Input to display")
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text="OK", command=button1_click)
button1.pack()
canvas.mainloop()