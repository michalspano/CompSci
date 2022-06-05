import tkinter
c=tkinter.Canvas(height=400, width=400)
c.pack()

print("Speaker 1 - 'red'")
print("Speaker 2 - 'blue'")
print("Speaker 3 - 'green'")

t=()
with open("dialogue.txt", "r") as textfile:
  for line in textfile:
    t+=(line.strip(),)
y=20
x=200
for i in range(0,len(t),2):
  y+=30
  speaker=t[i]
  lineSpeak=t[i+1]
  if speaker=="1":
    color="red"
  elif speaker=="2":
    color="blue"
  elif speaker=="3":
    color="green"
  c.create_text(x,y, text=lineSpeak, fill=color, font="Helvetica 20 bold")
    
  
