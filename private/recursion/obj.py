"""
Recursion in Python Tk
"""

from sys import argv

# Paste number of canvas objects from user input
obj_counter: int = int(argv[1]) 
 
# Define canvas attribute
import tkinter as tk
canvas = tk.Canvas(height=100, width=(obj_counter) * 25 + 10)
canvas.pack()


# Define main function
def main():
    print('Drawing on canvas recursively.')

    idx: int = 0
    recursion_draw(idx)  # {Initial recusrive call}
   
    # Permanent canvas dispaly
    canvas.mainloop()


# Define a recursive function to draw onto canvas
def recursion_draw(x: int, size: int = 25) -> None:
    if x < obj_counter:
        canvas.create_oval(size * x + 10, size, size * x + size + 10, size * 2,
                fill='#00aacc', outline='')
        canvas.create_text(size * x + size // 2 + 10, size + size // 2, text=f'{x+ 1}')
        recursion_draw(x + 1)


# Invoke main function
if __name__ == '__main__':
    main()
