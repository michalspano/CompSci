import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#  Loads default image sprite
img_sprite = tkinter.PhotoImage(file="pictures/image_template.png")


#  Configures width and height
def configure():
    width, height = int(img_sprite.width()), int(img_sprite.height())
    canvas["width"], canvas["height"] = width, height
    canvas.create_image(0, 0, image=img_sprite, anchor="nw")
    effect(width, height, int(input("Dimensions of a square: ")))


#  Pixel effect
def effect(w, h, k):
    #  Loops skip every k-th element
    for x in range(0, w, k):
        for y in range(0, h, k):
            color = img_sprite.get(x, y)
            new_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            canvas.create_rectangle(x, y, x + k, y + k, fill=new_color, outline="")
        canvas.update()
    finished()


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
