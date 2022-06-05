import tkinter
canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

places = []
altitudes = []
distances = []
f = open('cycleroute1.txt', 'r')
line = f.readline().strip()
info = line.split(';')
places.append(info[0])
altitudes.append(int(info[1]))
distances.append(float(info[2]))

for line in f:
    line = line.strip()
    info = line.split(';')
    places.append(info[0])
    altitude = altitudes[-1] + int(info[1])
    altitudes.append(altitude)
    distances.append(float(info[2]))
f.close()
print(places)
print(altitudes)
print(distances)
x = 50
maxy = 500
route = ()
for i in range(len(places)):
    x += distances[i] * 10
    y = maxy - altitudes[i] - 60
    route = route + (x, y)
    canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill='#4cb050', outline='')
    canvas.create_text(x, y - 10, text=altitudes[i])
    canvas.create_text(x, maxy - 120, text=places[i], angle=90)

canvas.create_line(route)
route_length = sum(distances)
highest_altitude = max(altitudes)
highest_altitude_index = altitudes.index(highest_altitude)
highest_altitude_place = places[highest_altitude_index]

lowest_altitude = min(altitudes)
lowest_altitude_index = altitudes.index(lowest_altitude)
lowest_altitude_place = places[lowest_altitude_index]

canvas.create_text(500, 500, text='The place: ' + highest_altitude_place +
                                  ' is the highest at: ' + str(highest_altitude) + ' m',
                   font='Arial 20', fill='#4cb050')

canvas.create_text(500, 530, text='The place: ' + lowest_altitude_place +
                                  ' is the highest at: ' + str(lowest_altitude) + ' m',
                   font='Arial 20', fill='#4cb050')

mytext = 'The length of the entire route is: {:5.2f} km'.format(route_length)
canvas.create_text(500, 560, text=mytext, font='Arial 20', fill='#4cb050')

canvas.mainloop()
