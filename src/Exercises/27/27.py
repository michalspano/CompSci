#!/usr/bin/env python3

"""
Michal Špano
27. Virus
06/10/2021
"""

# Import random module
import random as r


# Define main function
def main(input_path: str = 'src/in.txt', output_path: str = 'dist/out.txt'):
    print(f'A virus has been found on this device...\n'
          f'Input file: {input_path!r}\nOutput file: {output_path!r}\n')
    loaded_data: list = load_input_file(input_path)
    display_data(loaded_data, True)

    # Call the virus function
    output: list = virus(loaded_data)
    display_data(output, False)

    # Write to local output
    _write(output, output_path)


# Load input file to a list
def load_input_file(PATH: str) -> list[list]:
    return [row.strip().split(' ') for row in open(PATH)]


# Format and display data from input
def display_data(src: list[list], inp: bool):
    """
    Nested list comprehension:
    [val for '1st priority' for '2nd priority']
    """
    data: list = [word for row in src for word in row]
    _str: str = ' '.join(data)
    print(f"{'Input' if inp else 'Output'} content:\n{_str!r}")


# Define virus function with consecutive methods
def virus(data: list[list]) -> list[list]:

    # Randomly choose an event
    def event() -> bool:
        return r.choice([True, False])

    # Randomly decide to shuffle individual lines
    if event():
        r.shuffle(data)

    # Randomly decide to shuffle individual words in a line
    for i in range(len(data)):
        if event():
            r.shuffle(data[i])

    # Randomly decide to shuffle individual characters in a word
    for row in data:
        for j in range(len(row)):
            if event():
                word = list(row[j])
                r.shuffle(word)
                row[j] = ''.join(word)
    return data


# Write locally to txt
def _write(src: list[list], PATH):
    with open(PATH, 'w') as f:
        for row in src:
            f.write(f"{' '.join(row)}\n")


# Invoke main function
if __name__ == '__main__':
    main()
