#!/usr/bin/env python3

"""
Michal Špano
46. Vocabulary Learning
02/11/2021
"""

import random as r
from sys import argv


def main(path: str = 'hangman.txt'):
    print('HANGMAN, guess words\n')
    s_word: str = select_word(path)  # { receive a random word }

    # Turn on seek
    if len(argv) == 2 and argv[1].upper() == 'ON':
        print(f'`Seek mode` ON, word: {s_word}')

    # Returned evaluator method
    evaluator: bool = guess_word(s_word)
    exit('\nCongratulations!') if evaluator else exit('\nYou lost!')


# Select a random word from txt input file
def select_word(PATH: str) -> str:
    return r.choice([word.strip() for word in open(PATH)])


# Compute evaluation
def guess_word(word: str = 'theater', noneChar: str = '*') -> bool:
    # Create a noneChar buffer
    buff: list = list(noneChar * len(word))

    # Count number of guesses
    guess_count: int = 0

    # Process until all chars were found
    while buff.count(noneChar) != 0:
        inp: list = list(input(''))

        # Iterate over all inputted chars
        for char in inp:
            indexes: list = []

            # Append index that match a char
            for i in range(len(word)):
                if char == word[i]:
                    indexes.append(i)

            # Change all indexes to the current char
            for idx in indexes:
                buff[idx] = char

        # Display process
        print(f"Current word: {''.join(buff)}")
        guess_count += 1

    # Return type bool evaluator
    return True if guess_count <= 10 else False


# Invoke main function
if __name__ == '__main__':
    main()
