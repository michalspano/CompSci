import tkinter
from random import *
c=tkinter.Canvas(height=140, width=350, background="white")
c.pack()
print("Press 'space' to renew")
voters=input("number of voters? / randomizer ")

#random choice, inp
x=0
while True:
  x+=1
  w=choice(("yes", "no"))
  textfile=open("satisfactionV2.txt", "a")
  textfile.write(w+"\n")
  textfile.close()
  if x>=int(voters):
    break
  
#a), voters
tVote=()
file=open("satisfactionV2.txt", "r")
for vote in file:
  tVote+=(vote.strip(),)
textfile.close()
count=len(tVote)
print("Total number of people who voted: " + str(count))

#b], columns
yesCount,noCount=0,0
for i in range(len(tVote)):
  if tVote[i]=="yes":
    yesCount+=1
  elif tVote[i]=="no":
     noCount+=1

def columns():
  global yesCount,noCount
  c.delete("value")
  c.create_text(60,30,text="'Yes' voters: " + str(yesCount),tags="value", fill="green")
  c.create_text(61,60,text="'No' voters: " + str(noCount),tags="value", fill="red")
  c.create_rectangle(280,130,300,130-(int(noCount)*3), fill="red")
  c.create_rectangle(250,130,270,130-(int(yesCount)*3), fill="green")
columns()

#c)
average=((yesCount)/count)*100
average=round(average)
c.create_text(95, 100, text="≈"+str(average)+"% voters were satisfied.",font="bold")
c.create_text(105, 120, text="≈"+str(100-int(average))+"% voters were not satisfied.",font="bold")

def delete(event):
  c.delete("all")
  f=open("satisfactionV2.txt", "w")
  f.close()

c.bind_all("<space>", delete)
