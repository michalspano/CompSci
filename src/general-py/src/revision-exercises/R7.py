from random import *

problems_list, score = list(), int()


def create_quiz(r, op, problems):

    #  Resets the txt. file to empty
    file1 = open("R7_data.txt", "w")
    file1.close()

    #  Creates randomised exercises in given range
    for _ in range(r):
        n1, n2 = randint(0, 20), randint(0, 20)
        problems.append((n1, choice(op), n2))

    #  Stores exercises in the local txt. file
    with open("R7_data.txt", "a") as problemsTextFile:
        for j in range(len(problems)):
            problemsTextFile.write(f"{(j + 1)})     "
                                   f"{problems[j][0]} {problems[j][1]} {problems[j][2]}\n")

    print("Exercises created, open your txt. file!\n")


def solve(task, s):
    counter, exercise = len(task), int()
    i = 0
    #  Check for correct operation and construct read exercises
    while i < counter:
        n1, n2 = task[i][0], task[i][2]
        if task[i][1] == "+":
            exercise = n1 + n2
        elif task[i][1] == "*":
            exercise = n1 * n2

        #  Condition to determine correctness of the solution
        if int(input(f"{(i + 1)}) Solution: ")) == exercise:
            s += 1
        i += 1

    return s


#  Creates the quiz; prints the success rate in percentage
create_quiz(int(input("Number of questions: ")), ["+", "*"], problems_list)
print(f"\nSuccess rate: {((solve(problems_list, 0)) / len(problems_list)) * 100}%")
