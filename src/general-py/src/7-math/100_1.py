import math

print("Circle operations")
r = int(input("Radius of a circle: "))
circumference = round(2*math.pi*r, 2)
area = round(math.pi*r**2, 2)
print(f"Circumference: {circumference} cm.")
print(f"Area {area} cm2.")
