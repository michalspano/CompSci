import tkinter
canvas = tkinter.Canvas()
canvas.pack()
#  Color gradient effect


def img_dimensions(img):
    return img.width(), img.height()


def display_image(width, height):
    canvas["width"], canvas["height"] = width, height
    canvas.create_image(0, 0, anchor="nw", image=image_sprite)
    effect(width, height, input("Input color in RGB separated by a space: "))


def effect(w, h, c):
    color = c.split()
    color = [int(_c) for _c in color]
    mod = h / 20
    for y in range(h):
        if y % mod == 0:
            for i in range(len(color)):
                if color[i] >= 255:
                    color[i] = 0
                else:
                    color[i] += 5
        for x in range(w):
            new_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            image_sprite.put(new_color, (x, y))
        canvas.update()


image_sprite = tkinter.PhotoImage(file="pictures/image_template.png")
display_image(img_dimensions(image_sprite)[0], img_dimensions(image_sprite)[1])
canvas.mainloop()
