#  Raster Graphics practise
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

my_image = tkinter.PhotoImage(file="pictures/image_template.png")

width = my_image.width()
height = my_image.height()

canvas["width"] = my_image.width()
canvas["height"] = my_image.height()

canvas.create_image(0, 0, anchor="nw", image=my_image)
canvas.update()

rgb = []
i = 0
while i < 3:
    rgb.append(int(input("")))
    i += 1

for y in range(height):
    for x in range(width):
        new_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        my_image.put(new_color, (x, y))
    canvas.update()

canvas.mainloop()
