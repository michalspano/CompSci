import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

#  Loads default image sprite
img_sprite = tkinter.PhotoImage(file="pictures/image_template.png")


#  Configures width and height
def configure():
    width, height = int(img_sprite.width()), int(img_sprite.height())
    canvas["width"], canvas["height"] = width, height
    canvas.create_image(0, 0, image=img_sprite, anchor="nw")
    q = float(input("Effect quotient: "))
    if q <= 1:
        effect(width, height, int(input("Dimensions of a circle: ")), q, input("Animation y/n"))


def effect(w, h, size, k, a_switch):
    r = int((w * h) * k)  # All possible pixels * effect quotient
    for i in range(r):
        x, y = randrange(0, w), randrange(0, h)  # Random pixels from the photo
        color = img_sprite.get(x, y)
        canvas.create_oval(x - size, y - size, x + size, y + size, fill=rgb_to_hex(color), outline="")
        if a_switch == "y":  # To enable animation if prompted
            canvas.update()
    finished()


#  Transforms color from grb to hex
def rgb_to_hex(c):
    exp_color = "#{:02x}{:02x}{:02x}".format(c[0], c[1], c[2])
    return exp_color


#  Once effect is finished, display export button
def finished():
    export_button.pack(side="left")


#  Exports the image at a specified path
def export():
    path = input("Specify the file name: ") + ".eps"
    canvas.postscript(file=path)
    exit(f"Your photo was saved at: /{path}")


export_button = tkinter.Button(text="Export", command=export)
configure()
canvas.mainloop()
