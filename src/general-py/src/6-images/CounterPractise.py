from random import *
n = []
while len(n) < 10:
    r = randint(1, 16)
    if r not in n:
        n.append(r)
print(n)
