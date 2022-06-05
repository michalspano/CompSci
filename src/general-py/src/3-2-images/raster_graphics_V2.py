import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()
#  Distortion effect + export module


def img_dimensions(img):
    return img.width(), img.height()


def display_image(width, height):
    canvas["width"], canvas["height"] = width, height
    canvas.create_image(0, 0, anchor="nw", image=image_sprite)
    effect(width, height)


def effect(w, h):
    for x in range(w):
        for y in range(h):
            color = list(image_sprite.get(x, y))
            new_color = "#{:02x}{:02x}{:02x}".format(choice(color), choice(color), choice(color))
            image_sprite.put(new_color, (x, y))
        canvas.update()


#  Export module with current time details
def export():
    from datetime import datetime
    canvas["height"] = image_sprite.height() + 50
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    canvas.postscript(file=f"export{time}.eps")


image_sprite = tkinter.PhotoImage(file="pictures/image_template.png")
display_image(img_dimensions(image_sprite)[0], img_dimensions(image_sprite)[1])
button1 = tkinter.Button(text="Save", width=7, height=2, command=export)
button1.pack()
canvas.mainloop()
