import tkinter
canvas = tkinter.Canvas(height=600, width=800)
canvas.pack()

with open("cycleroute1.txt") as inputTextFile:
    d = [data.strip().split(";") for data in inputTextFile]
    places = [place[0] for place in d]
    altitudes = [int(alt[1]) for alt in d]
    distances = [float(dist[2]) for dist in d]

a, gradual_altitudes = int(), list()
for altitude in altitudes:
    a += altitude
    gradual_altitudes.append(a)

x, gradual_distances = float(), list()
for distance in distances:
    x += distance
    gradual_distances.append(round(x, 2))

x_list = list()
e1, e2, e3, abs_e = ([] for i in range(4))
x, maxy = 50, 500
route = tuple()
for i in range(len(places)):
    x += distances[i] * 10
    x_list += [x]


def scroll_bar():
    global fill, x_list
    canvas.delete("scroll")
    canvas.create_rectangle(x_list[0], 20, x_list[-1] + 40, 40)
    canvas.create_rectangle(x_list[0], 20, x_list[0] + fill, 40,
                            fill="green", tags="scroll")
    canvas.create_text((x_list[-1] + 40) + 35, 30,
                       text=f"{round(percentage, 2)}%", tags="scroll")


def cursor(cord):
    # 77_25
    global x_list, places, gradual_altitudes, distances, \
        e1, e2, e3, abs_e, x, maxy, route, fill, percentage
    scroll_bar()
    x1 = cord.x
    shift = round((x_list[-1]) / len(x_list))
    canvas.delete("route")
    for j in range(0, len(x_list) + 1):
        if x1 < x_list[-1]:
            if x_list[j-1] < x1 < x_list[j]:
                fill = j * shift
                percentage = j * (100 / len(x_list))
                e1, e2, e3, abs_e = places[:j], distances[:j], gradual_altitudes[:j], altitudes[:j]
        elif x1 >= x_list[-1]:
            fill = len(x_list) * shift
            percentage = len(x_list) * (100 / len(x_list))
            e1, e2, e3, abs_e = places[:], distances[:], gradual_altitudes[:], altitudes[:]
        altitudinal_calc()

    x, maxy = 50, 500
    route = tuple()
    for n in range(len(e1)):
        x += e2[n] * 10
        y = maxy - e3[n] - 50
        route = route + (x, y)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='#4cb050', outline='', tags="route")
        canvas.create_text(x, y - 15, text=e3[n], tags="route")
        canvas.create_text(x, maxy - 100, text=e1[n], angle=90, tags="route")
    draw()


def altitudinal_calc():
    global abs_e
    abs_e = [abs(alt) for alt in abs_e]


def draw():
    global route
    canvas.delete("draw")
    if len(route) >= 4:
        canvas.create_line(route, tags="draw")
    if len(e3) != 0:
        highest_altitude = max(e3)
        highest_altitude_place = places[gradual_altitudes.index(highest_altitude)]
        # 77_24
        lowest_altitude = min(e3)
        lowest_altitude_place = places[gradual_altitudes.index(lowest_altitude)]
        canvas.create_text(400, 500, text='The place: ' + highest_altitude_place +
                                          ' is the highest at: ' +
                                          str(highest_altitude) + ' m',
                           font='Arial 15', fill='#4cb050', tags="draw")

        canvas.create_text(400, 530, text='The place: ' + lowest_altitude_place +
                                          ' is the lowest at: ' +
                                          str(lowest_altitude) + ' m',
                           font='Arial 15', fill='#4cb050', tags="draw")

    my_text = 'The length of the entire route is: {:5.2f} km'.format(sum(e2))
    canvas.create_text(400, 560, text=my_text, font='Arial 15',
                       fill='#4cb050', tags="draw")
    if len(abs_e) != 0:
        canvas.create_text(400, 590, text=f"Greatest altitudinal change: {max(abs_e)}m.",
                           fill="#4cb050", tags="draw")


# 77_26
with open("cycleroute2.txt", "w") as outputTextFile:
    for i in range(len(places)):
        outputTextFile.write(places[i] + ";" + str(gradual_altitudes[i]) + ";" +
                             str(gradual_distances[i]) + "\n")
fill, percentage = 0, 0
scroll_bar()
canvas.bind_all("<B1-Motion>", cursor)
canvas.mainloop()
