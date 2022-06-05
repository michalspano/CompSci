"""
Michal Špano
22. Scrambled Text 2
29/09/2021
"""

# Import shuffle module
from random import shuffle

# Time module (optional)
import datetime


# Define main function
def main():
    begin = datetime.datetime.now()

    # Define IO paths
    input_path: str = 'input.txt'
    output_path: str = 'scrambled_text.txt'

    # Open output text file
    output_file = open(output_path, 'w')

    # Load individual words to a list (include all chars)
    loaded_data: list = ''.join([row for row in open(input_path)]).split(' ')

    # Create a list to store all alphabetical chars from words
    temp: list = []
    for word in loaded_data:
        valid_string: str = ''
        for w in word:
            if w.isupper() or w.islower():
                valid_string += w
        temp.append(valid_string)

    # Shuffle all chars in a word (ignore first and last character)
    # -> only alphabetical chars parsed her
    for i in range(len(temp)):
        if len(temp[i]) != 1:  # {Words of len 1 will be ignored}
            f_word = list(temp[i])[1:-1]  # {Create a substring and omit first, last chars}
            shuffle(x=f_word)

            # Assign formatted output: 'first_char' + 'shuffled_char(s)' + 'last_char'
            temp[i] = f"{temp[i][0]}{''.join(f_word)}{temp[i][-1]}"

    # Iterate over all words
    for j in range(len(temp)):
        original_word = loaded_data[j]
        scrambled_word = temp[j]

        # Store indexes that shall be ignored (non-alphabetical values)
        k: int = 0
        ignored_index: list = []
        for char in original_word:  # {Iterate over all chars from original words}
            if not char.isupper() and not char.islower():
                ignored_index.append(k)
            k += 1  # {Increment index}

        # Parse scrambled word into a list of chars
        list_word = list(scrambled_word)

        for index in ignored_index:

            # Insert non-alphabetical (from original words) values at current index
            list_word.insert(index, original_word[index])

        # Format output to text file
        output_word = ''.join(list_word)
        output_file.write(f'{output_word} ')

    # Close IO
    output_file.close()

    # Performance TIME
    end = datetime.datetime.now()
    print(f'Performance TIME: {end - begin}')


# Invoke main function
if __name__ == '__main__':
    main()
