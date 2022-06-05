import tkinter
c=tkinter.Canvas(height=300, width=300)
c.pack()

def click(coordinates):
  x,y=(coordinates.x,coordinates.y)
  c.create_oval(x-5,y-5,x+5,y+5,tags="circle")
  textfile=open("coordinates.txt", "a")
  textfile.write(str(x)+"\n")
  textfile.write(str(y)+"\n")
  print(x, y)

def delete(event):
  c.delete("circle")
  textfile=open("coordinates.txt", "w")
  textfile.close()
  
c.bind("<1>",click)
c.bind_all("<space>", delete)
