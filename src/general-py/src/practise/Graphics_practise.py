import tkinter
from datetime import date

today = str(date.today())
print(today)
print(type(today))

# canvas = tkinter.Canvas(width=440, height=200, bg="white")
# canvas.pack()

#  List Box
# def recolor(event):
#     selected = listbox1.curselection()
#     canvas["bg"] = listbox1.get(selected)
#
#
# def add():
#     listbox1.insert("end", entry1.get())
#
#
# def remove():
#     selected = listbox1.curselection()
#     if len(selected) == 1:
#         listbox1.delete(selected)
#
#
# listbox1 = tkinter.Listbox()
# listbox1.pack()
#
# colors = ["red", "green", "blue"]
#
# for element in colors:
#     listbox1.insert("end", element)
#
# listbox1.bind("<Double-Button-1>", recolor)
#
# label1 = tkinter.Label(text="Enter a color name: ")
# label1.pack()
# entry1 = tkinter.Entry()
# entry1.pack()
# button1 = tkinter.Button(text="Add color", command=add)
# button1.pack()
# button2 = tkinter.Button(text="Remove selected color", command=remove)
# button2.pack()

#  Scale

# rx, ry = 100, 50
# x, y = 200, 100
# canvas.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline="green",
#                    tags="oval")
#
#
# def change1(event):
#     global rx
#     rx = scale1.get()
#     redraw()
#
#
# def change2(event):
#     global ry
#     ry = scale2.get()
#     redraw()
#
#
# def redraw():
#     canvas.coords("oval", [x-rx, y-ry, x+rx, y+ry])
#
#
# scale1 = tkinter.Scale(from_=10, to=200, orient="horizontal",
#                        length=400, command=change1)
#
# scale1.pack()
# scale1.set(rx)
#
# scale2 = tkinter.Scale(from_=10, to=100, orient="vertical",
#                        length=200, command=change2)
#
# scale2.place(x=400, y=0)
# scale2.set(ry)

#  Text Field
# canvas = tkinter.Canvas(width=200, height=200, bg="white")
# canvas.pack(side="left")
#
# text1 = tkinter.Text(height=5, width=30)
# text1.pack()
#
# text1.insert("end", "first\n")
# text1.insert("end", "second\n")

# text1 = tkinter.Text(height=5, width=30)
# text1.pack(side="left")
#
# scrollbar1 = tkinter.Scrollbar()
# scrollbar1.pack(side="right", fill="y")
# scrollbar1.config(command=text1.yview)
# text1.config(yscrollcommand=scrollbar1.set)
#
# f = open("testFile.py", "r")
# for line in f:
#     text1.insert("end", line)
# f.close()
#
# text1.mainloop()

#  Radio Button
# canvas = tkinter.Canvas(width=200, height=200)
# canvas.pack()
#
# v = tkinter.IntVar()
#
# radiobutton1 = tkinter.Radiobutton(text="circle", variable=v, value=1)
# radiobutton1.pack()
#
# radiobutton2 = tkinter.Radiobutton(text="square", variable=v, value=2)
# radiobutton2.pack()
#
#
# def click(coord):
#     typ = v.get()
#     x, y = coord.x, coord.y
#     if typ == 1:
#         canvas.create_oval(x - 5, y - 5, x + 5, y + 5)
#     elif typ == 2:
#         canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5)
#     else:
#         print("Default")
#
#
# canvas.bind("<1>", click)

# window = tkinter.Tk()
# v = tkinter.StringVar()
#
# cities = [("New York", "NYC"), ("Prague", "PRG"), ("Bratislava", "BA")]
#
#
# def write():
#     print(v.get())
#
#
# for city, abbreviation in cities:
#     rb = tkinter.Radiobutton(window, text=city, value=abbreviation,
#                              variable=v, command=write)
#     rb.pack(anchor="w")
# window.mainloop()

#  Check Button
# window = tkinter.Tk()
#
#
# def write():
#     subjects = subject1.get() + " " + subject2.get() + \
#                " " + subject3.get()
#     subjects = subjects.strip()
#     print(f"We have selected the subjects: {subjects}")
#
#
# label1 = tkinter.Label(text="Subjects?")
# label1.pack()
#
# subject1 = tkinter.StringVar()
# checkbutton1 = tkinter.Checkbutton(window, text="English", onvalue="EL",
#                                    offvalue="", variable=subject1,
#                                    command=write)
# checkbutton1.pack(anchor="w")
#
# subject2 = tkinter.StringVar()
# checkbutton2 = tkinter.Checkbutton(window, text="French", onvalue="FL",
#                                    offvalue="", variable=subject2,
#                                    command=write)
# checkbutton2.pack(anchor="w")
#
# subject3 = tkinter.StringVar()
# checkbutton3 = tkinter.Checkbutton(window, text="German", onvalue="GL",
#                                    offvalue="", variable=subject3,
#                                    command=write)
# checkbutton3.pack(anchor="w")
# window.mainloop()
# window = tkinter.Tk()
#
#
# def write():
#     subjects = ""
#     for element in information:
#         subjects = subjects + " " + element.get()
#         subjects = subjects.strip()
#     print(f"Currently selected: {subjects}")
#
#
# def reset():
#     for inf in information:
#         inf.set("")
#     write()
#
#
# file1 = open("subjects.txt", "r")
# information = []
# label1 = tkinter.Label(text="Subjects?")
# label1.pack()
#
# for line in file1:
#     line = line.strip()
#     info = line.split(";")
#     information.append(tkinter.StringVar())
#     chb = tkinter.Checkbutton(window, text=info[0], onvalue=info[1],
#                               offvalue="", variable=information[-1],
#                               command=write)
#     chb.pack(anchor="w")
# file1.close()
#
# button1 = tkinter.Button(text="Reset", command=reset)
# button1.pack()
# window.mainloop()

# Menu

# window = tkinter.Tk()
# window.geometry("500x400")
# window.title("Using a menu")
# canvas = tkinter.Canvas(width=400, height=400)
# canvas.pack()
#
#
# def open_file():
#     pass
#
#
# def save_file():
#     pass
#
#
# def about_program():
#     text1.place(x=100, y=100)
#     button1.place(x=300, y=200)
#
#
# def about_program_close():
#     text1.place_forget()
#     button1.place_forget()
#
#
# menu1 = tkinter.Menu(window)
# window.config(menu=menu1)
#
# menu2 = tkinter.Menu(menu1)
# menu2.add_command(label="Open", command=open_file)
# menu2.add_command(label="Save", command=save_file)
# menu2.add_separator()
# menu2.add_command(label="End", command=window.destroy)
#
# menu1.add_cascade(label="File", menu=menu2)
#
# menu3 = tkinter.Menu(menu2)
# menu3.add_command(label="About the program", command=about_program)
#
# menu1.add_cascade(label="Help", menu=menu3)
#
# text1 = tkinter.Text(height=5, width=42)
# info = "About the program"
# text1.insert("end", info)
# text1.config(state="disabled")
# button1 = tkinter.Button(text="Close", command=about_program_close)
#
# canvas.mainloop()

# Dialogue Windows
# import tkinter.messagebox
# canvas = tkinter.Canvas(width=410, height=100)
# canvas.pack()
#
#
# def notice():
#     result = tkinter.messagebox.showinfo("notice", "You pressed a button")
#     print(result)
#
#
# def question1():
#     result = tkinter.messagebox.askyesno("Continue", "Continue?")
#     print(result)
#
#
# def question2():
#     result = tkinter.messagebox.askretrycancel("Continue", "Continue?")
#     print(result)
#
#
# button1 = tkinter.Button(text="Show info", command=notice)
# button1.pack()
# button2 = tkinter.Button(text="Question 1", command=question1)
# button2.pack()
# button3 = tkinter.Button(text="Question 2", command=question2)
# button3.pack()
#
# canvas.mainloop()

# Color Chooser
# import tkinter.colorchooser
# import tkinter.filedialog
#
# canvas = tkinter.Canvas(width=200, height=200)
# canvas.pack(side="left")
#
#
# def load_file():
#     info = tkinter.filedialog.asksaveasfile()
#     if info != None:
#         print(f"Filename: {info.name}")
#         print(f"Encoding: {info.encoding}")
#         file = open(info.name, "r", encoding=info.encoding)
#         content = file.read()
#         file.close()
#         text1.delete(1.0, "end")
#         text1.insert("end", content)
#
#
# def choose_color():
#     color = tkinter.colorchooser.askcolor()
#     print(color)
#     color_number = color[1]
#     if color_number != None:
#         canvas["bg"] = color_number
#         print("Changed to", color_number)
#     else:
#         print("Color was not changed.")
#
#
# text1 = tkinter.Text(width=60, height=10)
# text1.pack()
#
# button1 = tkinter.Button(text="Open file", command=load_file)
# button1.pack()
# button2 = tkinter.Button(text="choose color", command=choose_color)
# button2.pack()
#
# canvas.mainloop()
