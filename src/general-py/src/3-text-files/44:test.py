import tkinter

def mysave():
  with open("text1.txt", "a") as textfile:
    textfile.write(str(entry1.get()) + "\n")

entry1=tkinter.Entry()
entry1.pack()
button1=tkinter.Button(text="Save", command=mysave)
button1.pack(side="left")
