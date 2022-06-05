import tkinter
import time
canvas = tkinter.Canvas(height=500, width=500, bg="cyan")
configView = tkinter.Canvas(height=10, width=300)
configView.pack()


#  Dismiss initial window, enable canvas, get entry values
def configuration():
    global entry1_var, entry2_var

    #  Entry values for width and height
    entry1_var, entry2_var = int(entry_width.get()), int(entry_height.get())
    print(entry1_var, entry2_var)
    configView.destroy(), entry_height.destroy(), entry_width.destroy()
    button1.destroy(), label1.destroy(), label2.destroy()
    canvas.pack()
    load_data()


#  Loads data from x.txt, y.txt
def load_data():
    global coords
    x_cord, y_cord = open("x.txt", "r"), open("y.txt", "r")
    x_list, y_list = [int(x) for x in x_cord], [int(y) for y in y_cord]

    #  Combines (x, y) to a persistent array
    for i in range(len(x_list)):
        coords.append((x_list[i], y_list[i]))
    print_data(coords)


#  Prints (x;y) to console respectively
def print_data(arr):
    for i in range(len(arr)):
        print(f"{i + 1}: {arr[i][0]};{arr[i][1]}")


#  Animates circles
def animation(event, c, k):
    x_d, y_d = event.x, event.y  # Shifts the circles respective to button-click

    #  Calculates the percentage of reduction/expansion
    x_k, y_k = ((k / 100) * (100 + entry1_var), ((k / 100) * (100 + entry2_var)))
    for i in range(len(c)):
        x, y = c[i][0] + x_d, c[i][1] + y_d
        canvas.create_oval(x - x_k, y - y_k, x + x_k, y + x_k,
                           fill="white", outline="")
        #  Animation delay
        time.sleep(0.6)
        canvas.update()


coords, quotient = list(), 10
entry1_var, entry2_var = int(), int()  # Entry variables
label1 = tkinter.Label(text="Height reduction/expansion in %")
label2 = tkinter.Label(text="Width reduction/expansion in %")
entry_height = tkinter.Entry(bd=5)
entry_width = tkinter.Entry(bd=5)
label1.pack(), entry_width.pack(), label2.pack(), entry_height.pack()
button1 = tkinter.Button(text="Start", width=5, height=2,
                         command=configuration)
button1.pack()
canvas.bind("<Button-1>", lambda event: animation(event, coords, quotient))
canvas.mainloop()
