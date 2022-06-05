import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=600, bg="black")
canvas.pack()

frequency = (31, 62, 125, 250, 500, "1K", "2K", "4K", "8K", "16K", "[Hz]")
equalizer = []

for f in frequency[:-1]:
    equalizer.append(randint(20, 50))


def display_values(n):
    for i in range(len(n)):
        canvas.create_text(30 + i*55, + 380, text=n[i], fill="white")


def draw(eq):
    for j in range(len(eq)):
        min_height = int(canvas["height"]) - 40
        height = min_height - int(eq[j])
        x1, x2 = (j * 55 + 10), (j * 55 + 45)

        if min_height > height > min_height / 2:
            canvas.create_rectangle(x1, min_height, x2, height,
                                    fill="green", outline="",
                                    tags="EQ")
        elif min_height/2 >= height > min_height/4:
            canvas.create_rectangle(x1, min_height, x2, min_height / 2,
                                    fill="green", outline="",
                                    tags="EQ")
            canvas.create_rectangle(x1, min_height / 2, x2, height,
                                    fill="yellow", outline="",
                                    tags="EQ")
        elif min_height/4 >= height:
            canvas.create_rectangle(x1, min_height, x2, min_height / 2,
                                    fill="green", outline="",
                                    tags="EQ")
            canvas.create_rectangle(x1, min_height / 2, x2, min_height / 4,
                                    fill="yellow", outline="",
                                    tags="EQ")
            canvas.create_rectangle(x1, min_height / 4, x2, height,
                                    fill="red", outline="",
                                    tags="EQ")


def animation():
    global equalizer
    canvas.delete("EQ")

    for i in range(len(equalizer)):
        if 360 > equalizer[i] > 10:
            equalizer[i] += randint(-5, 10)

    draw(equalizer)
    canvas.after(200, animation)


def reset():
    for e in range(len(equalizer)):
        equalizer[e] = 20


display_values(frequency)
draw(equalizer)
animation()
button1 = tkinter.Button(text="Reset", command=reset)
button1.pack()
canvas.mainloop()
