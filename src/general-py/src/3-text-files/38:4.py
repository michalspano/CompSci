import tkinter
c=tkinter.Canvas(height=200, width=300,background="skyblue")
c.pack()

def text():
  c.create_text(150,50, text="Did you enjoy today's shopping?",
                font="Helvetica 15 bold", fill="white")
text()

count=0

def button1_click():
  global count
  count+=1
  textfile=open("satisfaction.txt", "a")
  print("Customer " + str(count) + " WAS satisfied with your service"+".- 'yes' ", file=textfile)

count2=0
def button2_click():
  global count
  count+=1
  textfile=open("satisfaction.txt", "a")
  print("Customer " + str(count) + " WAS NOT satisfied with your service"+". - 'no' ", file=textfile)
  textfile.close()

button1=tkinter.Button(text="Yes :)",
                       command=button1_click,width=4,height=2).place(x=50,y=100)
button2=tkinter.Button(text="No :(",
                       command=button2_click,width=4,height=2).place(x=200,y=100)
