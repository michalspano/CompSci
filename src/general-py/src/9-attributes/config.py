import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

canvas.create_rectangle(100, 100, 200, 190, fill="blue", tags="s1")
canvas.create_rectangle(250, 200, 350, 290, fill="red")
canvas.create_oval(120, 220, 190, 290, fill="yellow")
canvas.create_oval(270, 120, 340, 190, fill="green")
canvas.create_line(100, 350, 150, 300, 200, 350, 100, 350, width=3)
canvas.create_polygon(250, 350, 300, 300, 350, 350, fill="orange")
canvas.create_text(200, 50, text="Shape attributes", font="Arial 20")

r = (len(canvas.find_all()))
print(r)

n = [canvas.itemcget(i, "fill") for i in range(1, r + 1)]
print(n)
canvas.itemconfig("s1", fill="cyan")

c = [canvas.coords(i) for i in range(1, r + 1)]
print(f"{len(c)}: {c}")

t = [canvas.type(i) for i in range(1, r + 1)]
print(t)

canvas.move(1, 70, 70)
f = canvas.find_all()
print(f)

canvas.mainloop()
