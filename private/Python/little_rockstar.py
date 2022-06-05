#!/bin/env python3
# 'Go Little Rockstar' trend from your Console

from os import system
from sys import exit as e
from time import sleep as s


def main():
    while 1:
        system('clear')
        for temp in enumerate(['go', 'little', 'rockstar', '<3']):
            i: int = temp[0]
            data: str = temp[1]
            print(f"{'  ' * i}\u001b[{i + 32}m{data}\u001b[0m")
            s(0.75)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted.')
        e(0)

