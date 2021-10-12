import tkinter as tk
canvas = tk.Canvas(width=650, height=200)
canvas.pack()


def match(x, y, i):
    canvas.create_line(x, y, x, y + 100, width=5, fill='yellow', tag=i)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 8, fill='brown', outline='brown', tags=(i + 'xxx'))


for i in range(15):
    match(40 + i * 40, 100, str(i))

for ID in canvas.find_all():
    print(f'Regular canvas tag: {ID}; assigned tag: {canvas.gettags(ID)}')

"""
def no_obj() -> bool:
    return True if len(canvas.find_all()) == 0 else False


def click(coords):
    print('Click')


while not no_obj():
    remove = int(input('Enter next number: '))
    print(remove)
else:
    print('End')


match = 15
while match > 0:
    remove = int(input('Enter next number: '))
    for x in range(remove):
        match -= 1
        canvas.delete(str(match))
        canvas.delete(str(match) + 'xxx')
    canvas.update()

"""
canvas.mainloop()
