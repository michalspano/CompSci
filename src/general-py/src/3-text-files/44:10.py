import tkinter
c=tkinter.Canvas(height=250, width=150, background="cyan")
c.pack()

textfile=open("textV2.txt", "r")

t=()
y=-10
def show():
  global t,y
  for line in textfile:
    t=(line.strip(),)
    y+=30
    if y<=240:
      c.create_text(80,y, text=t, font="Helvetica 15 bold")
      c.update()
      c.after(800)
    else:
      c.delete("all")
      y=20
      c.create_text(80,y, text=t, font="Helvetica 15 bold")
      c.update()
      c.after(800)
      
show()
