# Lambda function expression
import tkinter
c = tkinter.Canvas()
c.pack()

c.create_line(10, 100, 210, 100, width=5)
b1 = tkinter.Button(text="-", command=lambda: c.move("all", 0, -5))
b1.pack()
b2 = tkinter.Button(text="+", command=lambda: c.move("all", 0, 5))
b2.pack()

# Exercise 3), https://www.w3resource.com/python-exercises/lambda/index.php
n = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
n.sort(key=lambda x: x[1])
print(n)

c.mainloop()
