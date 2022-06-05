import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

canvas.create_rectangle(100, 100, 180, 180, fill="blue",
                        tags=("rectangle", "color1"))
canvas.create_rectangle(200, 100, 280, 180, fill="red",
                        tags=("rectangle", "color2"))
canvas.create_oval(100, 200, 180, 280, fill="blue",
                   tags=("circle", "color1"))
canvas.create_oval(200, 200, 280, 280, fill="red",
                   tags=("circle", "color2"))

print(canvas.gettags(1))

canvas.mainloop()
