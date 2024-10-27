"""
Michal Špano
20. Table of Frequency
26/09/2021
"""

"""
--- ABSTRACT ---
This module is case-insensitive (default: lower-case);
"""


# Define main function
def main():
    # Create frequency table of type 'dict'
    frequency_table: dict = {(chr(i)): 0 for i in range(97, 123)}
    raw_t = read_text_file()
    print(f'Text:\n{raw_t}')  # {Print out input text}

    # Parse modified table (with frequency)
    new_table: dict = compute_frequency(raw_t, frequency_table)
    print('\nFrequency analysis: ')

    # Print chars with their occurrence
    for key in new_table:
        if new_table[key] != 0:
            print(f'{key.upper()} - {new_table[key]}')
        else:
            print(f'{key.upper()} was not found.')


# Function to read IO
def read_text_file(PATH='frequency_table.txt') -> str:
    raw_text: str = ''.join([line for line in open(PATH)])
    # Return raw input
    return raw_text


# Function to compute frequency table based upon txt input
def compute_frequency(text: str, table: dict) -> dict:
    f_text = text.replace('\n', '')  # {Produce a sequence}
    for char in f_text:  # {Iterate over all chars in the text}
        if char.islower():  # {Check for alphabetical chars only}
            table[char] += 1
    return table


# Invoke main function
if __name__ == '__main__':
    main()
