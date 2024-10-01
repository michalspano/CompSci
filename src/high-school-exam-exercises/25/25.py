"""
Michal Špano
25. Lottery
29/09/2021
"""

# Import libs
import os
import time
import random as r
from sys import exit


# Define main function
def main():
    N: int = 49  # {Max number from lottery}
    n_cards: int = 6

    # Define random winning values from the range
    values: list = [i + 1 for i in range(N)]

    # Create winning values (only non-repeating values)
    winning_val: list = []
    for _ in range(n_cards):

        # Pick a random index
        random_index: int = r.randrange(len(values))

        # Assign the value and remove it from the list (ensures non-repeating draws)
        winning_val.append(values[random_index])
        values.pop(random_index)

    # Ensure non-repeating values -> set{}
    user_values: set = user_input()

    if not evaluate_user_input(user_values, n_cards):
        # Exit and prompt incorrect usage
        exit(f'Incorrect usage, number of different votes ${n_cards}')

    # Proceed with valid input
    win_numbers_count: int = check_guess(user_values, winning_val)
    print(f"Number of correct guesses: {win_numbers_count}\nOriginal sequence: {' '.join(str(val) for val in winning_val)}")

    input_path: str = 'lottery.txt'

    # Check for other players
    if not multiple_players(input_path):
        exit('No more players.')

    # Input file does exist
    print(f'\nMore players were found...\n')
    time.sleep(0.5)

    # List of sets (input)
    loaded_players: list = [set(row.strip().split(' ')) for row in open(input_path)]

    i = 0
    # Ensured that all players inputted 6 different values
    for player in loaded_players:
        win_count: int = check_guess(player, winning_val)
        print(f'Player {i + 1} guessed {win_count} number(s) correctly.')
        i += 1


# Take user input from command line
def user_input() -> set:
    return set(map(int, input().split()))


# Evaluate correctness of the input
def evaluate_user_input(inp: set, N) -> bool:
    return True if len(inp) == N else False  # {Returns type bool}


# Check for number of winning guesses
def check_guess(user_inp: set, win: list) -> int:
    counter: int = 0
    for value in user_inp:
        if int(value) in win:  # {Ensure to compare type int}
            counter += 1
    return counter


# Check if input txt exists -> more players enrolled
def multiple_players(PATH) -> bool:
    return True if os.path.isfile(PATH) else False


# Invoke main function
if __name__ == '__main__':
    main()
