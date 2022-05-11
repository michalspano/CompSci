#!/usr/bin/env python3
# =*= coding: utf-8 =*=
# ~/main.py

'''
 Objective: create a prorgam that will load names of particitpants
 and create visual representations of the participants, pictures with
 their names on them.
'''

import tkinter as tk
from time import sleep as s
from subprocess import call
from os import system

c: tk.Canvas = tk.Canvas(width=500, height=500)
c.pack()

input_path: str = '../src/names.csv'


def main():
    # Create a buffer to hold the names
    c.create_text(250, 250, text='', tags='name_holder')

    data_set: list = load_database(input_path)

    for name in ['a', 'b']:
        c.itemconfig('name_holder', text=name), s(0.1), c.update()  # animation delay

        # Export to .eps
        c.postscript(file='./raw/' + name + '.eps', colormode='color')

        # Convert .eps to .png
        call([
            'convert', '-density', '150', '-strip', # utility args
            f'./raw/{name}.eps', f'./out/{name}.png' # input and output
        ])

    # Remove all *.eps buffers
    system('rm -f ./raw/*.eps'), exit(0)


def load_database(path: str) -> list:
    return [line.strip() for line in open(path, 'r')]


if __name__ == '__main__':
    main()
    c.mainloop()
