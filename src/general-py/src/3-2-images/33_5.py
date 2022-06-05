import tkinter
import os
canvas = tkinter.Canvas()
canvas.pack()


#  Loads default image sprite
def sprite(file_name):
    path = tkinter.PhotoImage(file=f"pictures/{file_name}.png")
    return path


#  Configures width and height
def configure():
    width, height = int(img_sprite.width()), int(img_sprite.height())
    canvas["width"], canvas["height"] = width, height
    canvas.create_image(0, 0, image=img_sprite, anchor="nw")
    effect(width, height, input("Horizontal or vertical h/v: "))


#  Effect with horizontal/vertical mirror image
# def effect_alt(w, h, inp):
#     #  Horizontal mirror image selected
#     if inp == "h":
#         interface_boundary = (h // 2)  # Middle axis for height
#         for x in range(w):
#             i = -1  # Default value -1, (index 0)
#             for y in range(h):
#                 new_y = y
#                 if y >= interface_boundary:  # If mid-line is crossed, assign the opposite values
#                     i += 2
#                     new_y -= i  # Default value increased by 1, decreased by 2
#                 current_color = img_sprite.get(x, new_y)
#                 img_sprite.put(rgb_to_hex(current_color), (x, y))
#             canvas.update()
#
#     #  Vertical mirror image selected
#     else:
#         interface_boundary = (w // 2)  # Middle axis for width
#         for y in range(h):
#             i = -1  # Default value -1, (index 0)
#             for x in range(w):
#                 new_x = x
#                 if x >= interface_boundary:  # If mid-line is crossed, assign the opposite values
#                     i += 2
#                     new_x -= i  # Default value increased by 1, decreased by 2
#                 current_color = img_sprite.get(new_x, y)
#                 img_sprite.put(rgb_to_hex(current_color), (x, y))
#             canvas.update()


#  Effect with horizontal/vertical mirror image
def effect(w, h, inp):  # General function
    #  Horizontal mirror image selected
    if inp == "h":
        interface_boundary = (h // 2)  # Middle axis for height
        range1, range2 = w, h
    else:
        interface_boundary = (w // 2)  # Middle axis for height
        range1, range2 = h, w  # Substitution for width - height

    for r1 in range(range1):
        j = -1  # Default value -1, (index 0)
        for r2 in range(range2):
            new_coord = r2
            if r2 >= interface_boundary:  # If mid-line is crossed, assign the opposite values
                j += 2
                new_coord -= j  # Default value increased by 1, decreased by 2

            #  Different configs for h/v
            if inp == "h":  # r1 - x; r2 - y, new_coord - y
                current_color = img_sprite.get(r1, new_coord)
                img_sprite.put(rgb_to_hex(current_color), (r1, r2))
            else:  # r1 - y; r2 - x, new_coord - x
                current_color = img_sprite.get(new_coord, r1)
                img_sprite.put(rgb_to_hex(current_color), (r2, r1))
        canvas.update()
    finished()


#  Transforms color from grb to hex
def rgb_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])


#  Once effect is finished, display export button
def finished():
    export_button.pack(side="left")


#  Exports the image at a specified path
def export():
    path = input("Specify the file name: ") + ".eps"
    canvas.postscript(file=path)
    exit(f"Your photo was saved at: /{path}")


export_button = tkinter.Button(text="Export", command=export)
dir_list = os.listdir("pictures")[1:]
print("Options: " + ", ".join(dir_list))
img_sprite = sprite(input("File: "))
configure()
canvas.mainloop()
