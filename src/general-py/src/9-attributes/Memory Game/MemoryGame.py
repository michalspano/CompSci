import tkinter
from random import *
canvas = tkinter.Canvas(width=800, height=400)
status_view = tkinter.Canvas(width=800, height=50, bg="black")
canvas.pack()

my_tags, images, turned = list(), list(), list()
count_turned, move_count = int(), 2
player1_score, player2_score = int(), int()
player1_switch = True
width, height = int(), int()
index_delete = list()

card_sprite = tkinter.PhotoImage(file="cardback.png")
empty_sprite = tkinter.PhotoImage(file="empty_slot.png")


def load(name, filetype, count, img):
    for k in range(1, count + 1):
        image = tkinter.PhotoImage(file=name + str(k) + "." + filetype)
        img.append(image)


def draw_back(x, y, m_t):
    order = 0
    for j in range(height):
        for n in range(width):
            canvas.create_image(x + n * 90, y + j * 90,
                                image=card_sprite, tags=m_t[order])
            order += 1

    for obj in canvas.find_withtag("empty"):
        canvas.itemconfig(obj, image=empty_sprite)


load("/Users/michalspano/Google Drive/P-4th Grade/6. Images/Images/91_5/oz_", "png", 16, images)


def identical(cards):
    if cards[0] == cards[1]:
        return True
    return False


def remove_from_game(cards):
    global my_tags
    canvas.delete(cards[0])
    my_tags.insert(index_delete[0] - 1, "empty")
    my_tags.pop(index_delete[0])
    my_tags.insert(index_delete[1] - 1, "empty")
    my_tags.pop(index_delete[1])


def turn(cards):
    for card in cards:
        info = card.split("_")
        new_tag = "back_" + info[1]
        ID = canvas.find_withtag(card)
        canvas.addtag(new_tag, "withtag", ID)
        canvas.dtag(ID, card)
        canvas.itemconfig(ID, image=card_sprite)


def click(event):
    global count_turned, turned, move_count, player1_switch, \
        player1_score, player2_score, index_delete
    clicked = canvas.find_withtag("current")
    move_count += 1
    if len(clicked) > 0:
        clicked = clicked[0]
        tags1 = canvas.gettags(clicked)
        if tags1[0] != "current":
            old_tag = tags1[0]
        else:
            old_tag = tags1[1]
        info = old_tag.split("_")
        if info[0] == "back" and count_turned < 2:
            count_turned += 1
            new_tag = "face_" + info[1]
            turned.append(new_tag)
            index_delete.append(clicked)
            image_number = int(info[1])
            canvas.addtag(new_tag, "withtag", clicked)
            canvas.dtag(clicked, old_tag)
            canvas.itemconfig(clicked, image=images[image_number])
            if count_turned == 2:
                canvas.update()
                canvas.after(500)
                if identical(turned):
                    remove_from_game(turned)
                    if player1_switch:
                        player1_score += 1
                    else:
                        player2_score += 1
                    display_scores()
                    pairs_found()
                else:
                    turn(turned)
                div = move_count // 2
                if div % 2 == 1:
                    player1_switch = True
                else:
                    player1_switch = False
                display_status()
                turned = []
                index_delete.clear()
                count_turned = 0
                canvas.after(200)
                canvas.update()
                canvas.delete("empty")
                end()


def display_status():
    status_view.delete("status")
    if player1_switch:
        player = 1
    else:
        player = 2
    status_view.create_text(75, 25,
                            text=f"Status: Player{player}", font="Arial 15",
                            tags="status", fill="white")


def display_scores():
    status_view.delete("score_label")
    status_view.create_text(250, 25,
                            text=f"Player 1 score: {player1_score}",
                            fill="white", font="Arial 15", tags="score_label")
    status_view.create_text(400, 25,
                            text=f"Player 2 score: {player2_score}",
                            fill="white", font="Arial 15", tags="score_label")


def pairs_found():
    status_view.delete("pairs")
    pairs = player1_score + player2_score
    status_view.create_text(550, 25, text=f"Pairs found: {pairs}",
                            tags="pairs", fill="white",
                            font="Arial 15")


def customization():
    global width, height
    user_input = int(input("Number of pairs? (8-16): "))
    if 8 <= user_input <= 16 and user_input % 2 == 0:
        if user_input == 8:
            width, height = 8, 2
        elif user_input == 10:
            width, height = 5, 4
        elif user_input == 12:
            width, height = 8, 3
        elif user_input == 14:
            width, height = 7, 4
        elif user_input == 16:
            width, height = 8, 4
        load_data(user_input)
    else:
        exit("Wrong input.")


def save():
    print("Saving...")
    with open("MG_save.txt", "w") as outputTextFile:
        for element in my_tags:
            outputTextFile.write(f"{element} \n")
        outputTextFile.write(f"{player1_score};{player2_score}")
    exit()


def load_data(r):
    global my_tags, player1_score, player2_score
    to_load = input("Load from text file? y/n")
    if to_load == "y":
        with open("MG_save.txt", "r") as inputTextFile:
            my_tags = [line.strip() for line in inputTextFile]
            if len(my_tags) == 0:
                exit("No data recorded.")
    
        scores = my_tags[-1].split(";")
        my_tags = my_tags[:-1]

        tag_count = 0
        for tag in my_tags:
            if tag == "empty":
                tag_count += 1
        if tag_count == len(my_tags):
            retreatInput = open("MG_save.txt", "w")
            retreatInput.close()
            exit("This game has been already completed")

        player1_score = int(scores[0])
        player2_score = int(scores[1])
        if r != len(my_tags) / 2:
            exit("Inputs not matching.")

    else:
        create_new_game(r)

    draw_back(50, 50, my_tags)
    display_status()
    display_scores()
    pairs_found()


def create_new_game(r):
    global my_tags
    for i in range(r):
        my_tags.append("back_" + str(i))
    my_tags = my_tags + my_tags
    shuffle(my_tags)


def end():
    if len(canvas.find_all()) == 0:
        canvas.delete("all")
        if player1_score > player2_score:
            final = "Player1 is the winner!"
        elif player2_score > player1_score:
            final = "Player2 is the winner!"
        else:
            final = "Tie"
        canvas.create_text(400, 200, text=final,
                           fill="black", font="Arial 30 bold")


customization()
button1 = tkinter.Button(text="Save", width=5, height=3, command=save)
button1.pack(side="left")
status_view.pack()
canvas.bind("<Button-1>", click)
canvas.mainloop()
