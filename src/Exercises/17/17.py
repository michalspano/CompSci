"""
Michal Špano
17. The Secret Table
21/09/2021
"""

# Import typing to define constants
from typing import final


# Create a global dict to store frequency
frequency: dict = {}


# Define main function
def main():
    plain_text: str = user_input()

    # Load custom encoding table
    table: dict = secret_table()

    print("Cypher-text: ", end='')

    # Iterate over chars from the plain text
    for char in plain_text:

        # Encode the value and print it out
        value = parser(char, table)
        print(value, end=' ')
    print('\n')

    # Determine the max occurrence from the cells
    max_cell_occurrence: int = max([frequency[key] for key in frequency])

    # Determine if more cells had the same counter (and print them out)
    for key in frequency:
        if max_cell_occurrence == frequency[key]:
            print(f"Key: '{key}' occurred {frequency[key]} times.")


# Get user input
def user_input() -> str:
    return input("Plaintext: ").upper()  # Ensure plaintext is only upper-case


# Define a function to create the desired encoding table
def secret_table() -> dict:
    table = {'0': ' '}  # {Start from the first key}

    char_count: final = 26  # {Number of English characters}
    index: int = 0
    value = 3

    """
    Each cell contains 3 chars,
    except the last one: chars 'Y' and 'Z' respectively.
    """

    # Iterate over all chars (skip every 3rd)
    for i in range(0, char_count, value):
        if index == char_count // value:  # {determine last index}
            value = 2

        # Create a new key with a value (value: list of chars)
        table[str(index + 1)] = [chr(i + j + 65) for j in range(value)]
        index += 1

    # Return created table
    return table


# Create a parser function
def parser(char: str, table: dict) -> str:

    # Global reference of frequency
    global frequency

    # Only encode upper-case letters and spaces
    if not char.isupper() and char != ' ':
        return char

    parsed_value: str = ''

    # Iterate over all keys from the table
    for key in table:

        # Load current list of possible chars
        char_arr = table[key]

        # If chars are matching -> create parsed value, i.e. multiply key (type str) n-times;
        # n - char's position within the list
        if char in char_arr:

            # Create value
            char_index = char_arr.index(char) + 1
            parsed_value = key * char_index

            # Populate frequency
            if key not in frequency:
                frequency[key] = 0

            frequency[key] += 1

    # Return parsed value
    return parsed_value


# Invoke main function
if __name__ == '__main__':
    main()
