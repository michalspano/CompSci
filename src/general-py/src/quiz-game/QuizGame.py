import tkinter
from random import *
import tkinter.colorchooser
import tkinter.messagebox
from datetime import datetime

window = tkinter.Tk()
window.title("Welcome to my Quiz!")
default_color = "skyblue"
canvas = tkinter.Canvas(width=300, height=300, bg=default_color)
quiz1 = tkinter.Canvas(width=400, height=400, bg=default_color)
canvas.pack()

data1, data2 = (list(),) * 2
wrong_count, question_index = (int(),) * 2
language_switch = tkinter.IntVar()


def load_data():
    global data1, data2
    with open("data.txt", "r") as inputTextFile:
        data = [line.strip().split(";") for line in inputTextFile]
    data1 = [data[i][0] for i in range(len(data))]
    data2 = [data[i][1] for i in range(len(data1))]


load_data()


def language_options():
    global data1, data2
    if language_switch.get() == 1:
        dismiss_main_menu_elements()
        #  Default data, no selection needed;
    elif language_switch.get() == 2:
        dismiss_main_menu_elements()
        data1, data2 = data2, data1
    else:
        print("No option was selected")
        QuizFunctions.restart()


def pick_color():
    c = tkinter.colorchooser.askcolor()
    color = c[1]
    if color is not None:
        QuizWidgets.label1["bg"], QuizWidgets.radiobutton1["bg"], canvas["bg"], \
            QuizWidgets.radiobutton2["bg"], QuizWidgets.button1["highlightbackground"], \
            quiz1["bg"], QuizWidgets.text_list1["bg"] = (color,) * 7


def test_type1():
    language_options()
    dismiss_main_menu_elements()
    quiz1.pack()

    QuizWidgets.listbox1.pack()
    shuffled_data = data2[:]
    shuffle(shuffled_data)

    for element in shuffled_data:
        QuizWidgets.listbox1.insert("end", element)

    button2 = tkinter.Button(text="Close", command=QuizFunctions.restart)
    button2.pack()
    question_pick()


def question_pick():
    global question_index
    quiz1.delete("word_text")
    if len(data1) > 0:
        question_index = randrange(0, len(data1))
        quiz1.create_text(200, 200, text=data1[question_index], font="Arial 60",
                          tags="word_text")
    else:
        save_data()
        quiz1.after(200)
        quiz1.update()
        end_var = tkinter.messagebox.showinfo("Congratulations",
                                              f"You made {wrong_count} mistake(s)!")
        if end_var == "ok":
            QuizFunctions.restart()


def save_data():
    with open("high_score.txt", "a") as outputHighScore:
        now = datetime.now()
        time_string = now.strftime("%m/%d/%Y, %H:%M:%S")
        outputHighScore.write(f"{wrong_count};{time_string}\n")


def show_high_score():
    with open("high_score.txt", "r") as inputScore:
        data = [line.strip().split(";") for line in inputScore]
        if len(data) > 0:
            for i in range(len(data)):
                QuizWidgets.text_list1.insert("end", "Mistakes: " + data[i][0] + " " + data[i][1] + "\n")


def correct_result(event):
    global wrong_count
    selected = QuizWidgets.listbox1.curselection()
    if selected is not None:
        if QuizWidgets.listbox1.get(selected[0]) == data2[question_index]:
            QuizWidgets.listbox1.delete(selected)
            data1.pop(question_index), data2.pop(question_index)
        else:
            wrong_count += 1
    question_pick()


def main_menu_assets():
    global tx
    canvas.delete("main_label")
    tx += 3

    if tx >= int(canvas["width"]) + 100:
        tx = - 100
    canvas.create_text(tx, int(canvas["height"]) / 2, text="Test your skills!",
                       font="Arial 25 bold", tags="main_label")
    canvas.after(25, main_menu_assets)


def dismiss_main_menu_elements():
    canvas.destroy()
    QuizWidgets.label1.destroy(), QuizWidgets.radiobutton1.destroy(), QuizWidgets.radiobutton2.destroy()
    QuizWidgets.button1.destroy(), QuizWidgets.text_list1.destroy()


tx = 150
main_menu_assets()


class QuizWidgets:
    menu = tkinter.Menu(window)
    window.config(menu=menu)

    file_menu = tkinter.Menu(menu)
    file_menu.add_command(label="Quiz 1", command=test_type1)

    menu.add_cascade(label="Quizzes", menu=file_menu)

    end_menu = tkinter.Menu(menu)
    end_menu.add_command(label="End", command=exit)

    menu.add_cascade(label="End", menu=end_menu)

    label1 = tkinter.Label(text="Choose a language to translate to: ",
                           bg=default_color)
    label1.pack()
    radiobutton1 = tkinter.Radiobutton(text="English", variable=language_switch,
                                       value=1, bg=default_color)
    radiobutton1.pack(anchor="center")
    radiobutton2 = tkinter.Radiobutton(text="Slovak", variable=language_switch,
                                       value=2, bg=default_color)
    radiobutton2.pack(anchor="center")

    text_list1 = tkinter.Text(heigh=5, width=35, bg=default_color)
    text_list1.pack(anchor="center")
    text_list1.config(state="normal")

    button1 = tkinter.Button(text="Settings", command=pick_color,
                             highlightbackground=default_color)
    button1.pack(anchor="center")
    listbox1 = tkinter.Listbox()


class QuizFunctions:

    @staticmethod
    def restart():
        import sys
        import os
        os.execv(sys.executable, ['python'] + sys.argv)


show_high_score()
QuizWidgets.listbox1.bind("<Double-Button-1>", correct_result)
window.mainloop()
