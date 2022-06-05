# Need For Speed
import tkinter
from random import *

initialView = tkinter.Canvas(width=200, height=200)
endView = tkinter.Canvas(width=300, height=300, bg="black")

length = 0
hp = 3
go_on = True
road_switch = True
autopilot_switch = False
quality_switch = True

lines = speed = road_difficulty = \
    d = track_length = line_length = track_span = int()
road = list()
canvas_width = canvas_height = int()

car1path = tkinter.PhotoImage(file="car@1x.png")
car2path = tkinter.PhotoImage(file="car@2x.png")
hearthpath = tkinter.PhotoImage(file="hp-image.png")


def highQuality():
    global quality_switch
    quality_switch = True
    graphics()


def lowQuality():
    global quality_switch
    quality_switch = False
    graphics()


def graphics():
    controller_panel.delete("graphics")
    global lines, road, speed, road_difficulty, \
        canvas_width, canvas_height, d, track_length, line_length, carx, cary, track_span
    if quality_switch:
        print("high")
        line_length = 2
        road_difficulty = 2
        canvas_width = 960
        canvas_height = 720
        lines = canvas_height // 10 * 5
        speed = 16
        text_switch = "High"
        track_length = 200
        track_span = 5
    else:
        print("low")
        line_length = 10
        road_difficulty = 10
        canvas_width = 640
        canvas_height = 480
        lines = canvas_height // 10
        speed = 100
        text_switch = "Low"
        track_length = 100
        track_span = 1
    controller_panel.create_text(550, 10, text=f"Graphics: {text_switch}",
                                 fill="white", tags="graphics")
    canvas["width"] = canvas_width
    canvas["height"] = canvas_height
    controller_panel["width"] = canvas_width

    d = (canvas_width // 2) - (track_length // 2)
    road = [d] * lines

    carx = canvas_width // 2
    cary = canvas_height - 20


canvas = tkinter.Canvas(bg="green")
controller_panel = tkinter.Canvas(height=15, bg="black")


def loadInitialView():
    label1.pack()
    switchButton1.pack(anchor="center")
    switchButton2.pack(anchor="center")
    initialView.pack()
    button1.pack()
    button2.pack()
    button3.pack()

    initialView.create_text(100, 100, text="Need For Speed",
                            font="Helvetica 20 bold", fill="red")


def loadProgress():
    global road, carx, speed, hp, length
    print("Loading progress.")
    with open("progress.txt", "r") as inputTextFile:
        load_road = inputTextFile.readline().strip()
        load_road = load_road[:-1].split(";")
        load_data = inputTextFile.readlines()
    load_road = [int(x) for x in load_road]
    load_data = load_data[0].split()
    load_data = [int(x) for x in load_data]
    if load_data[2] > 0:
        road = load_road
        carx = load_data[0]
        speed = load_data[1]
        hp = load_data[2]
        length = load_data[3]
    didTapStartButton()


def didTapStartButton():
    print("Start")
    dismissElements()
    canvas.pack()
    controller_panel.pack()
    animation()
    draw_speed_label()
    draw_hp()
    generate_road()
    autopilotStatus()


def dismissElements():
    initialView.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    switchButton1.destroy()
    switchButton2.destroy()
    label1.destroy()


def draw_road():
    canvas.delete("road")
    for i in range(lines):
        canvas.create_rectangle(road[i], i * line_length,
                                road[i] + track_length, i * line_length + line_length,
                                fill="white", outline="", tags="road")


def generate_road():
    global road_switch
    b = randint(100, 500)
    if road_switch:
        road_switch = False
    else:
        road_switch = True
    canvas.after(b, generate_road)


def move_road():
    global road_difficulty
    if road_switch:
        new = road[0] + 1 * road_difficulty
    else:
        new = road[0] + -1 * road_difficulty
    if new < 0:
        new = 0
    if new > (canvas_width - track_length):
        new = (canvas_width - track_length)
    road.insert(0, new)
    road.pop()


def animation():
    global length
    length += 1
    draw_road()
    move_road()
    draw_car()
    if autopilot_switch:
        autopilotCalculation()
    check()
    difficulty()

    with open("progress.txt", "w") as outputTextFile:
        for char in road:
            outputTextFile.write(str(char) + ";")
        outputTextFile.write("\n" +
                             str(carx) + " " +
                             str(speed) + " " +
                             str(hp) + " " +
                             str(length))

    if go_on:
        canvas.after(speed, animation)
    else:
        endScreen()


def autopilot():
    global autopilot_switch
    autopilot_switch = True
    print("Autopilot enabled")
    didTapStartButton()


def autopilotCalculation():
    global carx, road
    carx = int(road[-1]) + (track_length // 2)


def autopilotStatus():
    if autopilot_switch:
        status = "ON"
    else:
        status = "OFF"
    controller_panel.create_text(400, 10, text=f"Autopilot: {status}", fill="white")


def difficulty():
    global speed, length, road_difficulty
    for i in range(6):
        if length == i * 100 * track_span:
            controller_panel.delete("speed")
            speed -= line_length
            if not quality_switch:
                road_difficulty += 1
            draw_speed_label()


def draw_speed_label():
    if quality_switch:
        delay = 80
    else:
        delay = 0
    controller_panel.create_text(200, 10,
                                 text=f"Speed: {150 - delay - speed} km/h",
                                 fill="white",
                                 tags="speed")


def draw_car():
    canvas.delete("car")
    cars = [car1path, car2path]
    if quality_switch:
        cars = cars[1]
    else:
        cars = cars[0]
    canvas.create_image(carx, cary, image=cars, tags="car")


def left(event):
    global carx
    if quality_switch:
        carx -= 15
    else:
        carx -= 10


def right(event):
    global carx
    if quality_switch:
        carx += 15
    else:
        carx += 10


def lostLive():
    controller_panel.delete("hp")
    global hp, go_on
    hp -= 1
    if hp == 0:
        go_on = False
    draw_hp()


def draw_hp():
    controller_panel.create_text(280, 10, text="HP: ", fill="white")
    for i in range(hp):
        controller_panel.create_image(300 + 15*i, 10, image=hearthpath,
                                      tags="hp")


def check():
    global carx, hp
    controller_panel.delete("check")
    if carx < int(road[-1]) or carx > int(road[-1] + track_length - 10):
        check_value = "Out of the road."
        lostLive()

    else:
        check_value = "On the road."
    controller_panel.create_text(75, 10,
                                 text=f"Status: {check_value}",
                                 fill="white",
                                 tags="check")


def endScreen():
    canvas.destroy()
    controller_panel.destroy()
    endView.pack()
    endView.create_text(150, 125,
                        text="The End", font="Helvetica 30 bold", fill="red")
    endView.create_text(150, 150,
                        text=f"Travelled: {length}km",
                        font="Helvetica 15",
                        fill="red")


carx = cary = int()
button1 = tkinter.Button(text="Start", command=didTapStartButton, width=8)
button2 = tkinter.Button(text="Load", command=loadProgress, width=8)
button3 = tkinter.Button(text="Autopilot", command=autopilot, width=8)
switchButton1 = tkinter.Radiobutton(text="High", command=highQuality,
                                    indicatoron=False, value="High", width=12)
switchButton2 = tkinter.Radiobutton(text="Low", command=lowQuality,
                                    indicatoron=False, value="Low", width=12)

label1 = tkinter.Label(text="Graphics")
loadInitialView()
canvas.bind_all("<Left>", left)
canvas.bind_all("<Right>", right)
canvas.mainloop()
