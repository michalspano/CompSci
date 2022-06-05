import math
print("Distance between 2 points in 2D space.")
x = [int(input(f"Point A coord. {i+1}: ")) for i in range(2)]
y = [int(input(f"Point B coord. {j+1}: ")) for j in range(2)]

distance = math.sqrt((y[1]-x[1]) ** 2 + (y[0] - x[0]) ** 2)
print(round(distance, 2))
