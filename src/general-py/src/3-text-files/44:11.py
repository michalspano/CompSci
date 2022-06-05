import tkinter
c=tkinter.Canvas(height=175, width=600, background="skyblue")
c.pack()

c.create_text(300, 87.5, text="Press 'space' to start.", tag="startscreen", font="Helvetica 35 bold")
t=()
quote=()
name=()
textfile=open("quotes.txt", "r")

for line in textfile:
  t+=(line.strip(),)

for i in range(0,len(t),2):
  quote+=(t[i],)
  name+=(t[i+1],)

name_count=-1
quote_count=-1
def quotes(event):
  c.delete("startscreen")
  global name, quote, name_count, quote_count
  name_count+=1
  quote_count+=1
  if name_count==(len(name)-1) and quote_count==(len(quote)-1):
    name_count=-1
    quote_count=-1
  c.delete("name")
  c.delete("quote")
  c.create_text(300, 50, text=quote[int(quote_count)], fill="black",
                font="Helvetica 15 bold", tag="quote")
  c.create_text(100,100, text="-"+name[int(name_count)], fill="teal",
                tag="name",font="Helvetica 15 bold")
  c.update()


c.bind_all("<space>", quotes)
