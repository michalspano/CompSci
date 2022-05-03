#!/usr/bin/env python3

from os import listdir


def main():
    buff: list = []

    for name in listdir():
        if name.isdigit():  # assign only digits to buffer
            buff.append(int(name))  

    buff.sort()  # sort to ascending order

    _ = open('sorted.txt', 'w').write(', '.join(map(str, buff)))  # write sorted numbers to file

    print(f'{len(buff)} Python files found.')  # print number of files found


if __name__ == '__main__':
    main()
