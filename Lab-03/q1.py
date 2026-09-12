# 1. Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a
# second point (x2, y2), and displays whether the second point lies inside, on the boundary of, or
# outside the circle. The formula for computing the distance between two points is
# distance = √[(x2 – x1)2 + (y2 – y1)2]

x1 = float(input("Enter the center of the circle: "))
y1 = float(input("Enter the  center of the circle: "))
r = float(input("Enter the radius of the circle: "))
x2 = float(input("Enter the second point: "))
y2 = float(input("Enter the second point: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

if distance < r:
    print("The second point lies inside the circle.")
elif distance >r:
    print("The second point lies outside the circle.")
else:
    print("The second point lies on the boundary of the circle.")

