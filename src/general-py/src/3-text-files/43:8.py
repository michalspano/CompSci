import tkinter
c=tkinter.Canvas(height=300, width=300)
c.pack()

textfile=open("coordinates.txt", "r")
tuple1=()
for text in textfile:
  tuple1+=(text.strip(),)

def timer():
    for i in range(0,len(tuple1)-1,2):
      x=tuple1[i]
      y=tuple1[i+1]
      x,y=int(x),int(y)
      c.create_oval(x-10,y-10,x+10,y+10)
      c.update()
      c.after(500)
timer()
