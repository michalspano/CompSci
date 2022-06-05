import tkinter
c=tkinter.Canvas(height=230, width=400)
c.pack()
x1=20
y1=50
x2=20
y2=100
x3=20
y3=150
opt1=opt2=opt3=0
color1=color2=color3=""
total=0
c.create_rectangle(x1,y1,x1+50,y1+30)
c.create_rectangle(x2,y2,x2+50,y2+30)
c.create_rectangle(x3,y3,x3+50,y3+30)
inp=input("Show the previous value?  y/n ")
if inp=="n":
  c1Shift=c2Shift=c3Shift=0
if inp=="y":
  t=()
  file=open("survey2.txt", "r")
  for line in file:
    t+=(line.strip(),)
  c1Shift=(int(t[0])*5)
  c2Shift=(int(t[1])*5)
  c3Shift=(int(t[2])*5)
  c.create_rectangle(100,50,100+c1Shift,80)
  c.create_rectangle(100,100,100+ c2Shift,130)
  c.create_rectangle(100,150,100+ c3Shift,180)
  opt1=opt1+int(t[0])
  opt2=opt2+int(t[1])
  opt3=opt3+int(t[2])
    
def click(coordinates):
  global x1,y1, opt1, opt2, opt3, color1,color2,color3, total, c1Shift,c2Shift,c3Shift
  x,y=(coordinates.x,coordinates.y)
  textfile=open("survey2.txt", "w")
  c.delete("c1")
  c.delete("c2")
  c.delete("c3")
  if x1< x <x1+50 and y1 < y < y1+30:
    opt1+=1
  if x2 < x < x2+50 and y2 < y < y2+30:
   opt2+=1
  if x3 < x < x3+50 and y3 < y < y3+30:
    opt3+=1
  textfile.write(str(opt1))
  textfile.write("\n"+str(opt2))
  textfile.write("\n"+str(opt3))
  total=opt1+opt2+opt3
  if opt1>opt2>opt3:
    color1="green"
    color2=color3="blue"
    print("The percentage who voted for the highest value", (opt1/total)*100)
  elif opt1>opt3>opt2:
    color1="green"
    color2=color3="blue"
    print("The percentage who voted for the highest value", (opt1/total)*100)
  elif opt2>opt1>opt3:
    color2="green"
    color1=color3="blue"
    print("The percentage who voted for the highest value", (opt2/total)*100)
  elif opt2>opt3>opt1:
    color2="green"
    color1=color3="blue"
    print("The percentage who voted for the highest value", (opt2/total)*100)
  elif opt3>opt2>opt1:
    color3="green"
    color2=color1="blue"
    print("The percentage who voted for the highest value", (opt3/total)*100)
  elif opt3>opt1>opt2:
    color3="green"
    color2=color1="blue"
    print("The percentage who voted for the highest value", (opt3/total)*100)
  c.create_rectangle(100,50,(100)+(int(opt1)*5),80,tag="c1", fill=color1)
  c.create_text(380,62, text=(str(opt1)),tag="c1",fill=color1)
  c.create_rectangle(100,100,(100)+(int(opt2)*5),130,tag="c2", fill=color2)
  c.create_text(380,112, text=(str(opt2)),tag="c2",fill=color2)
  c.create_rectangle(100,150,(100)+(int(opt3)*5),180,tag="c3", fill=color3)
  c.create_text(380,162, text=(str(opt3)),tag="c3",fill=color3)
  
  
c.create_text(85,200, text="green - highest value", fill="green")
c.create_text(200,20,text="Do you prefer online learning?")
c.create_text(45,65,text="yes")
c.create_text(45,115,text="no")
c.create_text(45,165,text="idk")
c.bind("<1>", click)
c.mainloop()
