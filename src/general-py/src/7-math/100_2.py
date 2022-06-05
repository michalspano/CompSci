import math

print("Area of triangle")
lengths = [int(input(f"Side {j+1}: ")) for j in range(3)]
a, b, c = lengths[0], lengths[1], lengths[2]
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area: {round(area, 2)} m2.")
