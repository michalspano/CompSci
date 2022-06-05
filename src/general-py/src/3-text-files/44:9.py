import tkinter
c=tkinter.Canvas(height=250, width=150, background="cyan")
c.pack()
t=()
y=0
with open("text.txt", "r") as textfile:
  for line in textfile:
    t+=(line.strip(),)
for i in range(0,len(t)):
  y+=30
  word=t[i]
  c.create_text(75,y,text=word, fill="red")
  c.update()
  c.after(800)
