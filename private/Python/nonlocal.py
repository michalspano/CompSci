#!/usr/bin/env python3

# Using the 'nonlocal' keyword in Python3
# Simple demonstration of the nonlocal keyword
# Consider the 2 following functions


# Just a simple formatting function
def console(key: str, val: int):
    print(f'{key}: {val}')


# No 'nonlocal' keyword
def outer1():
    x: bool = True

    def inner():
        x = False
        console('inner', x)

    inner()
    console('outter', x)


# Using the 'nonlocal' keyword
def outer2():
    x: bool = True

    def inner():
        nonlocal x  # <- nonlocal keyword applied here!
        x = False
        console('inner', x)

    inner()
    console('outter', x)


# run the functions with a formatter
outer1(), print('*' * 15), outer2()
