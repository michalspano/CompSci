import tkinter
import time
canvas = tkinter.Canvas(height=150, width=400)
canvas.pack()

display_word = list(input("Input: "))
index = 0


def appearAnimation():
    global display_word, index
    while index < len(display_word):
        canvas.delete("w")
        index += 1
        canvas.create_text(200, 75, text=display_word[:index], font="Bold 35", tags="w")
        time.sleep(.8)
        canvas.update()
    while index > 0:
        canvas.delete("w")
        index -= 1
        canvas.create_text(200, 75, text=display_word[:index], font="Bold 35", tags="w")
        time.sleep(.8)
        canvas.update()
    appearAnimation()


appearAnimation()
canvas.mainloop()
