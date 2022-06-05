import tkinter
import time
canvas = tkinter.Canvas(height=300)
canvas.pack()


#  Draw matches in user range
def draw_matches(r, sprite):
    width = r * sprite.width() + 10
    canvas["width"] = width
    for i in range(r):
        canvas.create_image(i * 50 + 20, 150, image=sprite)


#  Boolean value to switch between players
def player_handler(switch):
    global player1, user_click
    if switch:
        player1 = False
    else:
        player1 = True
    user_click = 0
    progress_arr.append("switch")
    label_value(player_var)


def click(event):
    global user_click
    x, y = event.x, event.y
    picked = canvas.find_overlapping(x, y, x, y)
    user_click += 1

    #  3 is the maximum number of moves in a round;
    if user_click <= 3:
        if len(picked) > 0:
            picked = picked[0]
            progress_arr.append(picked)
            canvas.delete(picked)

    check(player1)


#  Check function to evaluate possible game scenarios
def check(switch):

    #  Proceed if no matches are left
    if len(canvas.find_all()) == 0:
        if switch:
            player = "Player1"
            progress_arr.append(f"{player}\n{user_range}")
            print("Player 1 lost.")
        else:
            player = "Player2"
            progress_arr.append(f"{player}\n{user_range}")
            print("Player 2 lost.")
        canvas.create_text(int(canvas["width"]) / 2, int(canvas["height"]) / 2,
                           text=f"{player} lost!", font="Arial 20 bold")


#  Player status for tkinter.Label() via tkinter.Var();
def label_value(var):
    if player1:
        var.set("Player 1")
    else:
        var.set("Player 2")


#  Simulates previous game stored in 'R10_save.txt'
def restart():
    with open("R10_save.txt", "r") as inputTextFile:
        data = [line.strip() for line in inputTextFile]

    if len(data) > 0:
        matches_count = int(data[-1])  # The last element is the number of matches
        data = data[:-1]  # All recorded moves
        player_loser = data[-1]

        if matches_count == user_range:
            i = 0
            for j in range(len(data)):
                move = data[j]

                #  Player switch; div. by 2;
                if move == "switch":
                    i += 1
                    if i % 2 == 0:
                        player_var.set("Player 1")
                    else:
                        player_var.set("Player 2")

                #  Loser user stored as penultimate element;
                elif j == len(data) - 1:
                    canvas.create_text(int(canvas["width"]) / 2,
                                       int(canvas["height"]) / 2,
                                       text=f"{player_loser} lost!",
                                       font="Arial 20 bold")
                else:
                    canvas.delete(move)
                time.sleep(1.25)
                canvas.update()

                #  Reset txt. file to default
                file_reset = open("R10_save.txt", "w")
                file_reset.close()
    else:
        print("Empty txt. file.")


#  Save to a text file upon user prompt
def save_progress():
    with open("R10_save.txt", "a") as output_progress:
        for move in progress_arr:
            output_progress.write(str(move) + "\n")
    exit("Your progress was saved.")


progress_arr = []  # Used to store all data to replay progress;
user_range = int(input("Number of matches: "))
user_click, player1 = int(), True

player_var = tkinter.StringVar()
label_value(player_var)

match_sprite = tkinter.PhotoImage(file="match.png")
draw_matches(user_range, match_sprite)

label1 = tkinter.Label(textvariable=player_var)
label1.pack()

player_button = tkinter.Button(text="Done", width=7, height=2,
                               command=lambda: player_handler(player1))
player_button.pack()
save_button = tkinter.Button(text="Save", width=7, height=2,
                             command=save_progress)
save_button.pack()
restart_button = tkinter.Button(text="Replay", width=7, height=2,
                                command=restart)
restart_button.pack()
canvas.bind("<Button-1>", click)
canvas.mainloop()
