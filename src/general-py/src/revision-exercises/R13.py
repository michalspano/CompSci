from random import *
from collections import Counter


#  Returns a random number from the specified range
def pick_number(_range):
    if len(_range.split()) != 2:
        exit("Wrong input")
        # Exits the program if input requirements are not fulfilled

    r = [int(number) for number in _range.split()]
    r.sort()
    return randint(r[0], r[1])


#  Prompts the user to enter a number
def user_input(number, switch):
    while switch:
        user_guess = int(input("\nInput a number: "))

        #  Detects if user_guess was already used
        if user_guess in user_progress:
            print(f"{user_guess} was already used.")

        #  Stores user progress
        user_progress.append(user_guess)

        #  Prompts the user if value is smaller
        if user_guess > number:
            print("Smaller")

        #  Prompts the user if value is bigger
        elif user_guess < number:
            print("Bigger")

        #  Loop is disabled, data evaluated
        elif user_guess == number:
            print("Correct!\n")
            evaluation(user_progress)
            switch = False


#  Evaluates progress data after completion
def evaluation(progress):
    output_progress = list()

    #  Inputs a list with value frequency
    for key, value in (Counter(progress)).items():
        output_progress.append([key, value])  # Converts dic. to list
    output_progress.sort()

    #  Prints values and their frequencies
    for i in range(len(output_progress)):
        print(f"Value {output_progress[i][0]} "
              f"was guessed {output_progress[i][1]} time(s).")
    save_progress(progress)


#  Saves to a text file after evaluation
def save_progress(output):
    with open("R13_progress.txt", "w") as outputTextFile:
        outputTextFile.write(f"Game progress: number of guesses {len(output)},"
                             f" winning number: {chosen_number}")

        #  Writes to a text file with corresponding index values
        i = 0
        for guess in output:
            i += 1
            outputTextFile.write(f"\nGuess n. {i}: {guess}")


user_progress = list()
start = True
chosen_number = pick_number(input("Input values range separated by a space: "))
user_input(chosen_number, start)
