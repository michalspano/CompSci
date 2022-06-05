import tkinter
from random import *

canvas = tkinter.Canvas(width=400, height=300, bg="white")
canvas.pack()

dieCount = int(input("How many die? "))
dieRange = (dieCount * 6) - (dieCount - 1)

counts = [0] * dieRange
maxY = 500
maxX = 500

handleButtonAction = True
toHandleAnimation = True


def didTapAnimationButton():
    global toHandleAnimation
    toHandleAnimation = False


def initialView():
    canvas.create_text(400 / 2, 300 / 2, text="Dice histogram", font="Arial 30 bold", tags="initialLabel")


initialView()


def didTapButton1():
    global handleButtonAction
    handleButtonAction = True
    draw()


def didTapButton2():
    global handleButtonAction
    handleButtonAction = False
    draw()


# function to delete previous stored data
def delete():
    outputFile = open("CountSum.txt", "w")
    outputFile.close()
    simulation()


def draw():
    canvas.delete("percentage")
    canvas.delete("CountSum")
    global handleButtonAction, dieRange, dieCount
    percentages = [0] * dieRange
    realized_throw_count = sum(counts)
    i = 0
    for value in counts:
        percentages[i] = (value / realized_throw_count) * 100
        i += 1
    for i in range(dieRange):
        if handleButtonAction:
            percentage = "{:.1f}%".format(percentages[i])
            canvas.create_text(5 + i * 30 + 10, maxY - 50 - counts[i] - 20, text=percentage, tags="percentage",
                               angle=90)
        else:
            canvas.create_text(5 + i * shift + 10, maxY - 70 - counts[i], text=counts[i], tags="CountSum")
        canvas.create_rectangle(5 + i * shift, maxY - 50, 10 + i * shift + 20 - dieCount, maxY - 50 - counts[i],
                                fill="#4cb050")


def simulation():
    global throw_count, counts, dieCount
    mysum = 0
    outputValues = []
    outputFile = open("CountSum.txt", "a")
    for i in range(dieCount):
        throw = randint(1, 6)
        mysum += throw
        outputValues.append(throw)
    outputFile.write(str(outputValues) + "\n")
    counts[mysum - dieCount] += 1
    draw()
    if toHandleAnimation:
        if throw_count > 0:
            throw_count -= 1
            canvas.after(10, simulation)
    else:
        while throw_count > 0:
            throw_count -= 1
            canvas.after(10, simulation)
    outputFile.close()


def start():
    global throw_count, maxY, maxX, dieRange
    throw_count = int(entry1.get()) - 1
    maxY = throw_count // 5 + 100
    canvas["height"] = maxY
    canvasX = dieRange * shift
    canvas["width"] = canvasX
    canvas.delete("initialLabel")
    labels()
    delete()


def labels():
    global dieCount
    for i in range(dieRange):
        canvas.create_text(5 + i * shift + 10, maxY - 20, text=str(i + dieCount))


label1 = tkinter.Label(text="Number of throws: ")
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text="start", command=start)
button1.pack()
button2 = tkinter.Button(text="percentage", command=didTapButton1)
button3 = tkinter.Button(text="exact", command=didTapButton2)
button2.pack()
button3.pack()
button4 = tkinter.Button(text="Animation Off", command=didTapAnimationButton)
button4.pack()
throw_count = 0
shift = 30
canvas.mainloop()
