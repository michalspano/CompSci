import tkinter
import time
from random import *

canvas = tkinter.Canvas(width=1000, height=400, bg="aqua")
canvas.pack()

grass = [randint(1, 50) for i in range(100)]
weed_count = int(input("Weed percentage: "))

weed = grass[:]
weed = weed[:weed_count]
for j in range(len(weed)):
    weed[j] = weed[j] * 1.5
for i in range(100 - weed_count):
    weed.append(0)
shuffle(weed)

for index in range(len(weed)):
    if weed[index] != 0:
        grass[index] = 0


def draw_grass():
    canvas.delete("grass")
    global grass
    x = -10
    for n in range(len(grass)):
        x += 10
        canvas.create_rectangle(0 + x, 410, 10 + x, 410 - grass[n],
                                fill="green", outline="", tags="grass")


def draw_weed():
    canvas.delete("weed")
    global weed, color
    x = - 10
    for k in range(len(weed)):
        x += 10
        canvas.create_rectangle(0 + x, 410, 10 + x, 410 - weed[k],
                                fill=color, outline="", tags="weed")


def water_lawn():
    global herbicide_switch
    for i in range(len(grass)):
        if grass[i] != 0:
            grass[i] += randint(0, 5)
    if herbicide_switch:
        for w in range(len(weed)):
            if weed[w] != 0:
                weed[w] += randint(3, 7)
    if herbicide_switch:
        pick_new_weed()
    draw_grass()
    draw_weed()


def pick_new_weed():
    global grass, weed
    w_list = [element for element in grass if element != 0]
    random_pick = choice(w_list)
    weed_index_value = grass.index(random_pick)
    weed[weed_index_value] = int(grass[weed_index_value]) * 2
    grass[weed_index_value] = 0
    w_list.clear()


def mow_lawn():
    global herbicide_switch
    for m in range(len(grass)):
        grass[m] -= randint(5, 15)
    for w in range(len(weed)):
        weed[w] -= randint(10, 20)
    draw_grass()
    draw_weed()


def weed_lawn():
    global weed, grass, herbicide_switch, color
    list_weed = [w for w in weed if w != 0]
    random_choice = choice(list_weed)
    index_value = weed.index(random_choice)
    weed.clear()
    weed = [0] * 100
    weed[index_value] = random_choice
    i = 0
    while i < 100:
        grass[i] += 1
        i += 1
    herbicide_switch, color = True, "darkgreen"
    draw_grass()
    draw_weed()


def herbicide():
    global herbicide_switch, color
    herbicide_switch, color = False, "darkgray"


def auto_mode():
    for i in range(5):
        water_lawn()
        time.sleep(0.2)
        canvas.update()
    canvas.after(750, auto_mode)


herbicide_switch, color = True, "darkgreen"
button1 = tkinter.Button(text="Water", command=water_lawn)
button1.pack()
button2 = tkinter.Button(text="Mow", command=mow_lawn)
button2.pack()
button3 = tkinter.Button(text="Weed", command=weed_lawn)
button3.pack()
button4 = tkinter.Button(text="Herbicide", command=herbicide)
button4.pack()
auto_mode()
draw_grass()
draw_weed()
canvas.mainloop()
