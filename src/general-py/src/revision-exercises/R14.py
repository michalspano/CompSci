#  Prompts the user to input a number from the specified interval
def pick_number(min_val, max_val):
    user = int(input(f"Think of a number between <{min_val}-{max_val}>: "))

    #  Checks whether the number belongs to the specified interval
    if max_val >= user >= min_val:
        file1 = open("R14_progress.txt", "w")

        #  Resets the txt. file to default
        file1.close()
        return user
    else:

        #  Exits the program if number does not belong to the interval
        exit(f"Input should be in the interval <{min_val}-{max_val}>!")


#  Algorithm to determine the guessing logics
def guess(start, number_progress):
    global guess_count

    #  time module to calculate speed of execution
    import time
    start_time, end_time = time.time(), time.time()

    #  To do while still searching
    while start:
        guess_count += 1  # Increment the number of guesses

        #  If chosen number is one of the boundaries of the interval
        if chosen_number == number_progress[0] or chosen_number == number_progress[1]:
            start = False
            end_time = time.time()

        #  If chosen number is between the boundaries of the interval
        else:

            # Calculates the middle value of the interval
            mid_number = (number_progress[1] + number_progress[0]) // 2

            if chosen_number > mid_number:
                number_progress[0] = mid_number

            elif chosen_number < mid_number:
                number_progress[1] = mid_number

            #  If the middle value corresponds to chosen number - stop
            if mid_number == chosen_number:
                start = False
                end_time = time.time()

        #  Save guess progress to txt. file periodically
        with open("R14_progress.txt", "a") as output:
            write_output = "-".join(str(j) for j in number_progress)
            output.write(write_output + "\n")

    #  Returns the speed of the execution
    return end_time - start_time


_min, _max = 10, 10 ** 10  # Specified range of values
guess_count = int()
chosen_number = pick_number(_min, _max)
time = guess(True, [_min, _max])
print(f"Number of guesses: {guess_count}")
print(f"Time of the executions {time}s.")
