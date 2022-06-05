import tkinter
import time
from random import *
menu = tkinter.Canvas(height=100, width=300)
canvas = tkinter.Canvas(height=400, width=1000)
menu.pack()

frogs = list(range(10))
shuffle(frogs)  # shuffles elements from the list
frogs_positions = list()

frog_path = tkinter.PhotoImage(file="frog.png")
frog_width = frog_path.width()
win_image_path = tkinter.PhotoImage(file="win.png")


def menu_lobby():
    menu_label()


def menu_label():
    global c
    c += 1
    title_colors = ["darkgreen", "forestgreen", "limegreen", "springgreen"]
    menu.create_text(300 / 2, 50,
                     text="Žabky", fill=title_colors[c-1],
                     font="Arial 25")
    if c == len(title_colors):
        c = 0
    menu.after(500, menu_label)


def start():
    print("Start initialized.")
    dismiss_elements()
    canvas.pack()
    draw()
    display_swap_count()


def training():
    global frogs
    print("Training initialized.")
    positions = input("Input initial positions separated by a space: ").split()
    positions = [int(p) for p in positions]
    frogs = positions
    start()


def load_game():
    global frogs, swaps_count
    print("Load initialized.")
    with open("load_frogs.txt", "r") as load_progress_from_input:
        input_data = [var.split() for var in load_progress_from_input][0]
    input_data = [int(d) for d in input_data]
    frogs = input_data[:-1]
    swaps_count = input_data[-1]
    start()


def bot():
    print("Bot initialized.")
    start()
    canvas.unbind("<Button-1>")
    bot_completion()


def dismiss_elements():
    menu.destroy()
    button1.destroy(), button2.destroy(), button3.destroy(), button4.destroy()


def draw_frog():
    for i in range(len(frogs_positions)):
        canvas.create_line(15 + i * 100, 260, 85 + i * 100, 260, width=5, fill="green")
        x, y, number = frogs_positions[i][0], frogs_positions[i][1], frogs_positions[i][2]
        if number != 0:
            canvas.create_image(x, y, image=frog_path,
                                tags=f"frog{i}")
        canvas.create_text(50 + i*100, 300, text=frogs_positions[i][2],
                           font="Arial 30 bold", tags="numbers")


def draw():
    global frogs_positions
    frogs_positions.clear()
    for i in range(len(frogs)):
        canvas.delete(f"frog{i}")
    canvas.delete("numbers")
    for i in range(len(frogs)):
        frogs_positions.append([i * frog_width + 50, 200, frogs[i]])
    draw_frog()


def click(coord):
    global swaps_count, my_pick
    index = coord.x // frog_width
    empty = frogs.index(0)
    distance = abs(index-empty)
    my_pick = index
    jump_up()

    if distance < 3 and 0 <= index <= 9:
        jump_over()
        swaps_count += 1
        display_swap_count()
        frogs[index], frogs[empty] = frogs[empty], frogs[index]
        save_progress()
        draw()
        if check_positions():
            congratulations_view()
    else:
        jump_down()


def jump_up():
    i = 0
    while i < 7:
        time.sleep(0.05)
        canvas.update()
        canvas.move(f"frog{my_pick}", 0, -5)
        i += 1


def jump_down():
    i = 0
    while i < 7:
        time.sleep(0.05)
        canvas.update()
        canvas.move(f"frog{my_pick}", 0, 5)
        i += 1


def jump_over():
    empty_index = frogs.index(0)
    distance = (empty_index-my_pick)
    x = distance * frog_width / 15
    y = - abs(distance * frog_width / 15)
    i = 0
    while i < 15:
        time.sleep(0.01)
        canvas.update()
        canvas.move(f"frog{my_pick}", x, y)
        i += 1
        j = 0
        while j < 10:
            canvas.move(f"frog{my_pick}", 0, 1)
            j += 1


def save_progress():
    global frogs
    with open("load_frogs.txt", "w") as output:
        for position in frogs:
            output.write(str(position) + " ")
        output.write(str(swaps_count))


def bot_completion():
    global swaps_count, my_pick
    empty = frogs.index(0)
    bot_index = abs(empty - randint(-2, 2))
    my_pick = bot_index
    jump_up()
    if 0 <= bot_index <= 9:
        jump_over()
        swaps_count += 1
        display_swap_count()
        frogs[bot_index], frogs[empty] = frogs[empty], frogs[bot_index]
        draw()
        save_progress()
        if check_positions():
            congratulations_view()
    else:
        jump_down()
    canvas.after(400, bot_completion)


def check_positions():
    for i in range(len(frogs) - 1):
        if i != frogs[i] - 1:
            return False
    return True


def display_swap_count():
    canvas.delete("count")
    canvas.create_text(100, 20, text=f"Number of swaps: {swaps_count}",
                       tags="count", font="Arial 20")


def congratulations_view():
    canvas.destroy()
    w = win_image_path.width()
    h = win_image_path.height()
    end_view = tkinter.Canvas(height=400, width=400, bg="black")
    end_view.pack()
    end_view.create_image(h / 2 + 20, w / 2 + 50, image=win_image_path)


c, swaps_count = int(), 0
my_pick = int()
button1 = tkinter.Button(text="Start", command=start,
                         width=10, height=2)
button1.pack()
button2 = tkinter.Button(text="Training", command=training,
                         width=10, height=2)
button2.pack()
button3 = tkinter.Button(text="Load", command=load_game,
                         width=10, height=2)
button3.pack()
button4 = tkinter.Button(text="Bot", command=bot,
                         width=10, height=2)
button4.pack()
canvas.bind("<Button-1>", click)
menu_lobby()
menu.mainloop()
