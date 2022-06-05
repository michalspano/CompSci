import tkinter
canvas=tkinter.Canvas()
canvas.pack()

def house():
  A=50,50
  B=100,100
  C=75,25
  D=100,50
  block=A+B
  line1=A+C
  line2=C+D
  canvas.create_rectangle(block)
  canvas.create_line(line1)
  canvas.create_line(line2)
  return "rectangle: "+ str(block), "line1: "+str(line1),"line2: "+ str(line2)
print(house())
