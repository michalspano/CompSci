import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=600)
canvas.pack()


#  Loads car sprites
def load_cars(cars):
    for i in range(5):
        cars.append(tkinter.PhotoImage(file=f"cars/car_{(i + 1)}.png"))
    create_cars(cars)


def create_cars(cars):
    colors = ["orange", "green", "white", "red", "blue"]
    for i in range(15):

        #  Chooses a random car sprite and assigns a color tag respectively
        random_car = choice(cars)
        index = cars.index(random_car)
        color = colors[index]
        canvas.create_image(20, 20 + i*25, image=random_car, tags=(i + 1, color))


def race():
    global cars_order
    finish_line = int(canvas["width"]) - 20
    cars_count = len(canvas.find_all())

    for ID in canvas.find_all():
        cords = canvas.coords(ID)
        random_speed = randint(5, 10)
        new_x_coord = cords[0] + random_speed

        #  Car move forward if its x values is smaller than the finish line
        if new_x_coord < finish_line:
            canvas.coords(ID, [new_x_coord, cords[1]])

        #  Car is removed once the finish line is reached, data is stored
        else:
            current_tags = canvas.gettags(ID)
            cars_order.append(current_tags)
            canvas.delete(ID)

    #  The animation continues until all cars reach the finish line
    if cars_count > 0:
        canvas.after(100, race)
    else:
        end(cars_order)


#  Function to display order of cars once animation is finished
def end(order):
    print(order)
    canvas.destroy(), button1.destroy()
    endView = tkinter.Canvas(height=450, width=200, bg="black")
    endView.pack()

    #  Displays the ordered places with cars' colours
    for i in range(len(order)):
        endView.create_text(100, 20 + i*30,
                            text=f"Place: {i + 1}, race number: {order[i][0]}",
                            fill=order[i][1])


cars_list, cars_order = list(), list()
load_cars(cars_list)
button1 = tkinter.Button(text="Start",
                         width=5, height=2, command=race)
button1.pack(side="left")
canvas.mainloop()
