print("Input your rgb value: ")
n=[]
count=0
for i in range(3):
  count+=1
  n.append(int(input(str(count)+": ")))
def rgb(n):
  color="#{:02x}{:02x}{:02x}".format(n[0],n[1],n[2])
  return color
print("Hex. color: ",rgb(n))

import tkinter as tk
c=tk.Canvas(width=400, height=400, bg=rgb(n))
c.pack()
