#!/usr/bin/env python3
# Exercise 45 reimplemented in Python
from random import shuffle


# Define the main function
def main(src_path: str = './45/vocabulary_learning.txt') -> None:
    buff: list = [line.strip().lower() for line in open(src_path)]

    supported_lang: Final = ['EN', 'ES']   # Displaying in English by default
    user_lang: str = input('Display language: ').upper()

    # Overring the default behavior, to display in English
    if user_lang == supported_lang[-1]:
        buff = buff[::-1]

    # Detect unsupported language
    elif user_lang not in supported_lang and user_lang != '':
        print('Unsupported language.')
        return

    line_break()

    # Buffers
    dict_lang: dict = format_language_buffer(buff)
    incorrect_words: dict = {}

    # Continue until all words were guessed
    while len(dict_lang):
        guessed_buff: list = []  # Correct, to be removed
        for word in dict_lang:
            user_entry: str = input(f'Translate `{word}`: ').lower()

            # If the word is guessed correctly, schedule it to be removed
            if user_entry == dict_lang[word]:
                guessed_buff.append(word)
            # Otherwise note the mistake
            else:
                if word not in incorrect_words:
                    incorrect_words[word] = 0
                incorrect_words[word] += 1

        # Remove the guessed words 
        for correct_word in guessed_buff:
            del dict_lang[correct_word]
    
    line_break()

    # Detect no mistakes
    if not len(incorrect_words):
        print('Congratulations! You guessed all the words!')
        return

    # Display the incorrect words with the total count and count for each
    counter: int = 0
    for word in incorrect_words:
        print(f'{word}: {incorrect_words[word]}')
        counter += incorrect_words[word]

    line_break()
    print(f'Total incorrect words: {counter}')
    

# Format the language buffer of type list to a dictionary
def format_language_buffer(lang_buff: list) -> dict:
    dict_buff: dict = {}
    for i in range(0, len(lang_buff) - 1, 2):
        dict_buff[lang_buff[i]] = lang_buff[i + 1]
    return dict_buff


# Define a function which create a line break in the console
def line_break() -> None:
    GREEN: str = '\033[92m'
    RESET: str = '\033[0m'
    print(f"\n{GREEN}{'*' * 20}{RESET}\n")


# Invoke the main function
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nhalt')
