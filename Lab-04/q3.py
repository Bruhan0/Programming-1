''' 3. Write a program that reads input data from the console - the measures of a geometric
shape and calculates its area. There are four types of
shapes: square, rectangle, circle and triangle.
The first line of input is the type of shape (square, rectangle, circle, triangle):
If the shape is a square, the next argument will be one number - the length of its side.
If the shape is a rectangle, the next argument will be two numbers - the lengths of its sides.
If the shape is a circle, the next argument will be one number - the radius of the circle.
If the shape is a triangle, the next argument will be two numbers - its base and the
corresponding altitude. '''

shape = input("Enter the type of shape From one of these...(square, rectangle, circle, triangle): ")

if shape == "square":
    side = float(input("Enter the length of the side: "))
    area = side ** 2
    print(f"The area of the square is: {area:.3f}")
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.3f}")
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area:.3f}")
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid shape entered.")