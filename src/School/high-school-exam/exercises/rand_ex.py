#!/usr/bin/env python3

# Import modules
from os import listdir
from random import choice
from sys import argv


# Define the main function
def main():
    # Check usage, if no arguments are passed, show usage
    if len(argv) != 2:
        print('Usage: ./count_files.py <operand>')
        return
    
    # Parse the operand
    operand: str = str(argv[1]).lower()
    
    # Check the operand and execute the corresponding function
    if operand == '--read' or operand == '-r':
        read_dir(), exit()
        
    elif operand == '--pick' or operand == '-p':
        print(f'Randomly chosen exercise: {show_random_int()}'), exit()

    print('Unknown operand.')


def read_dir(_dir: str = './') -> None:
    buff: list = []

    for name in listdir(_dir):
        if name.isdigit():  # assign only digits to buffer
            buff.append(int(name))  

    buff.sort()  # sort to ascending order

    _ = open('sorted.txt', 'w').write(', '.join(map(str, buff)))  # write sorted numbers to file

    print(f'{len(buff)} Python files found.')  # print number of files found


# Compute a random number from the interval of parsed numbers
def show_random_int(inp: str = 'sorted.txt') -> int:
    return choice(open(inp).read().split(', '))  # return random number from file


if __name__ == '__main__':
    main()
