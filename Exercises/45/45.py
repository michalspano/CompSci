#!/usr/bin/env python3

"""
Michal Špano
45. Vocabulary Learning
02/11/2021
"""


# Define main function
def main(path: str = 'vocabulary_learning.txt'):
    # Receive parsed language option
    isTypeInitial: bool = language_option()  # <- Possible languages in upper-case

    # Base case
    if isTypeInitial is None:
        exit('Invalid language option.')

    # Load data
    data: dict = load_content(path, isTypeInitial)
    if data is None:
        exit('Incorrect vocabulary content.')

    # Final evaluation
    ms_count: int = guess_word(data)
    print(f'\nDone! Number of mistakes: {ms_count!r}')


# Identify user-desired language option
def language_option(possible_lang=None) -> bool or None:
    if possible_lang is None:
        #  Default language preferences
        possible_lang = ['ES', 'EN']
    else:
        # Check custom languages
        if len(possible_lang) != 2 or type(possible_lang) != list:
            return

    # Show possible languages to choose from
    print(f"Possible languages: {' '.join(possible_lang)}")
    lang_opt: str = input('Choose a language to display: ')

    # Return type
    if lang_opt.upper() == possible_lang[0]:
        return True
    elif lang_opt.upper() == possible_lang[1]:
        return False

    # Return None if invalid input
    return


# Load vocab content to memory
def load_content(PATH: str, lang_type_init: bool) -> dict or None:
    # Buffers
    i: int = 0
    primary, secondary = [], []
    buff: dict = {}

    # Create a function to parse current word
    add_w = lambda w, l: l.append(w)

    # Open source text file
    with open(PATH) as f:
        for row in f:
            current_word: str = row.strip()
            if i % 2 == 0:
                add_w(current_word, primary) if lang_type_init else add_w(current_word, secondary)
            else:
                add_w(current_word, secondary) if lang_type_init else add_w(current_word, primary)
            i += 1

    # Check proper size
    if len(primary) != len(secondary):
        return

    # Populate dictionary
    for i in range(len(primary)):
        buff[primary[i]] = secondary[i]
    return buff


# Require user to guess all word
def guess_word(vocab_src: dict) -> int:
    print('\nTranslate the words below: ')

    # Count all mistakes
    mistake_count: int = 0

    # Process until all words are guessed
    while len(vocab_src) > 0:
        temp = []
        for key in vocab_src:
            print(key, end=':')

            # Check if user provided translation is correct
            if input('') == vocab_src[key]:
                temp.append(key)  # { assign the key to a temp. list }
            else:
                mistake_count += 1  # { otherwise increase mistake count }

        # Remove keys that were correctly translated
        for k in temp:
            del vocab_src[k]

    # If completed -> return number of mistakes
    return mistake_count


# Invoke main function
if __name__ == '__main__':
    main()
