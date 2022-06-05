import tkinter
import math
canvas = tkinter.Canvas()
canvas.pack()

a = int(input("Side a: "))
b = int(input("Side b: "))


def dimensions():
    global default
    default = 300
    if a > (default - 100) or b > (default - 100):
        default += 100

    canvas["width"], canvas["height"] = default, default


def triangle():
    x, y = 100, default - 50
    A = (x, y - b)
    B = (x + a, y)
    C = (x, y)
    length = round(math.sqrt(a ** 2 + b ** 2), 2)
    print(length)
    canvas.create_line(A, B)
    canvas.create_text(((A[0] + B[0]) // 2) + 30, (A[1] + B[1]) // 2, text=f"c={length}")
    canvas.create_line(B, C)
    canvas.create_text(((B[0] + C[0]) // 2), ((B[1] + C[1]) // 2) + 20, text=f"c={a}")
    canvas.create_line(A, C)
    canvas.create_text(((A[0] + C[0]) // 2) - 30, ((A[1] + C[1]) // 2), text=f"c={b}")


default = int()
dimensions()
triangle()
canvas.mainloop()
