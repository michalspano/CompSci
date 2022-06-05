import tkinter
c=tkinter.Canvas(height=300, width=300)
c.pack()

t=()
with open("survey.txt", "r") as textfile:
  for line in textfile:
    t+=(line.strip(),)

question=t[0]
x1,x2,x3=t[1],t[2],t[3]
c.create_text(150,50, text=question, font="Arial 20 bold")
c.create_rectangle(50,250,100,(250-(int(x1)*10)),fill="red")
c.create_text(75,260, text="yes", fill="red")
c.create_rectangle(120,250,170,(250-(int(x2)*10)),fill="blue")
c.create_text(145,260, text="no", fill="blue")
c.create_rectangle(190,250,240,(250-(int(x3)*10)),fill="green")
c.create_text(215,260, text="idk", fill="green")
  
  
