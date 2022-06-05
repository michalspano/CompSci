import tkinter
import time
startView = tkinter.Canvas(width=200, height=200)
canvas = tkinter.Canvas(width=310, height=310)
startView.pack()


#  Replays the game upon button-click
def start_replay():
    print("The game progress ie being played.")
    startView.destroy(), button1.destroy()
    canvas.pack()
    load_data()


#  Loads data in the desired format from local txt. file
def load_data():
    with open("R15_progress.txt", "r") as inputTextFile:
        data = [line.strip().split(";") for line in inputTextFile]
    if len(data) > 0:
        draw_circles(30, data)
    else:
        exit("No progress was found.")


def draw_circles(w, progress):
    for i in range(10):
        for j in range(10):
            canvas.create_oval(10 + i*w, 10 + j*w,
                               10 + i*w + w - 5, 10 + j*w + w - 5,
                               fill="", outline="")

    #  Updates moves respectively
    for n in range(len(progress)):
        for ID in canvas.find_all():
            canvas.itemconfig(ID, fill=progress[n][int(ID) - 1])
            time.sleep(0.005)
            canvas.update()
    print("Finished.")


startView.create_text(100, 100,
                      text="Replay gameplay", font="Arial 20 bold")
button1 = tkinter.Button(text="Replay", width=10, height=2,
                         command=start_replay)
button1.pack()
canvas.mainloop()
