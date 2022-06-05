from random import *


def task(students, questions, output):

    #  The limit is 26, English alphabet contains 26 letters; no repetition
    if students <= 26 and questions <= 26:

        print("Processing...")

        #  Default data sets
        students_list = [(i + 1) for i in range(students)]
        questions_list = [chr(j + 65) for j in range(questions)]

        #  Handler for students > questions
        if students > questions:
            i = len(questions_list)
            while i < len(students_list):
                questions_list.append(chr(i + 65))
                i += 1

        #  Handler for students < questions
        elif questions > students:
            i = len(students_list)
            while i < len(questions_list):
                students_list.append(i + 1)
                i += 1

        #  Randomisation via random.shuffle()
        shuffle(students_list), shuffle(questions_list)

        for i in range(len(students_list)):
            output.append((students_list[i], questions_list[i]))

    else:
        exit("Wrong input")

    #  Resets the txt. file to empty
    file1 = open("6_save.txt", "w")
    file1.close()

    return output


#  Save to a text file
def save(data):
    for element in data:
        if element != "":
            with open("6_save.txt", "a") as outputTextFile:
                outputTextFile.write(f"Student: {element[0]} - Question: {element[1]} \n")


save(task(int(input("Number of students: ")), int(input("Number of questions: ")), list()))
