#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exporting canvas attributes to `ps`

import tkinter as tk

c_dim: int = 500
c = tk.Canvas(width=c_dim, height=c_dim, bg='blue')
c.pack()


# -> out
def post(path: str) -> None:
    c.update(), c.postscript(file=f"{path}.ps", colormode='color')


def load_data(path: str = 'src/names.csv') -> list:
    return [name.strip() for name in open(path)]


for idx, name in enumerate(load_data()):
    c.delete('text'), c.create_text([c_dim // 2] * 2, text=name, font='Arial 50 bold', tags='text', fill='black')
    post(path=f"foo_out/{idx + 1}.ps")

c.mainloop()
