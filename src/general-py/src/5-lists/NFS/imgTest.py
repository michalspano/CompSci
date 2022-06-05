import tkinter
canvas = tkinter.Canvas()
canvas.pack()

path = tkinter.PhotoImage(file="car@1x.png")
canvas.create_image(50, 100, image=path)

canvas.mainloop()
