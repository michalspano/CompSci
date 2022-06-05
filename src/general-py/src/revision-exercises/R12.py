import tkinter
from random import *
canvas = tkinter.Canvas(height=200, width=500)
canvas.pack()


#  Loads frog sprites
def load_frogs(file, filetype, frogs):
    for i in range(3):
        frogs.append(tkinter.PhotoImage(
            file=f"frogs/{file}{(i + 1)}{filetype}"))
    draw_frogs(frogs, 10)


#  Draws frogs and their identifiers
def draw_frogs(f, _range):
    for i in range(_range):
        random_frog = choice(f)
        canvas.create_image(20 + i*50, 100, image=random_frog)
        canvas.create_text(20 + i*50, 150, text=f"{i + 1}")


#  On/Off button click - bool value
def animation_switch(switch):
    global animation_ON
    if switch:
        animation_ON = False
    else:
        animation_ON = True
    animation()


#  Frogs animation
def animation():
    max_width = int(canvas["width"]) + 20
    if animation_ON:
        for ID in canvas.find_all():
            coords = canvas.coords(ID)
            x, y = (coords[0] + 50), coords[1]
            if x >= max_width:
                x = 20  # Shifts the frog and its ID to the beginning
            canvas.coords(ID, [x, y])
        canvas.after(speed, animation)


frogs_list, speed = list(), int(input("Speed: "))  # User input speed value
animation_ON = False
load_frogs("frog_", ".png", frogs_list)
button1 = tkinter.Button(text="Animation",
                         width=8, height=2, command=lambda: animation_switch(animation_ON))
button1.pack(side="left")
canvas.mainloop()
