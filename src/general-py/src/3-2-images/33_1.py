import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#  Loads default image sprite
img_sprite = tkinter.PhotoImage(file="pictures/image_template.png")


#  Configures width and height
def configure():
    width, height = int(img_sprite.width()), int(img_sprite.height())
    canvas["height"], canvas["width"] = height, width
    canvas.create_image(0, 0, image=img_sprite, anchor="nw")
    color_effect(width, height)


#  Processes the black&white + negative effect
def color_effect(w, h):
    for x in range(w):
        for y in range(h):
            get_color = img_sprite.get(x, y)
            average = (get_color[0] + get_color[1] + get_color[2]) // len(get_color)
            if average > 127:
                new_color = "black"  # Inverse shift
            else:
                new_color = "white"

            #  Alternative version
            # nr, ng, nb = 255 - new_color[0], 255 - new_color[1], 255 - new_color[2]
            # new_color = "#{:02x}{:02x}{:02x}".format(nr, ng, nb)
            img_sprite.put(new_color, (x, y))
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


export_button = tkinter.Button(text="Export", width=5, height=2, command=export)
configure()
canvas.mainloop()
