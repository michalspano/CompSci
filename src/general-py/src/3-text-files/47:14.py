import tkinter
c=tkinter.Canvas(width=300, height=300)
c.pack()

t=()
with open("stickman.txt", "r") as textfile:
  for line in textfile:
    t+=(line.strip(),)

#head
h=()
h+=t[0:4]
c.create_oval(h)
#body
b=()
b+=t[4:8]
c.create_line(b)
#rLeg
rL=()
rL+=t[8:12]
c.create_line(rL)
#lLeg
lL=()
lL+=t[12:16]
c.create_line(lL)
#rHand
rH=()
rH+=t[16:20]
c.create_line(rH)
#lHand
lH=()
lH+=t[20:]
c.create_line(lH)
