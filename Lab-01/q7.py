# 7. Input the radius of a circle (1–100 only) and calculate its area. Handle invalid inputs.
radius = float(input("Enter the radius of the circle (1–100): "))
if 1 <= radius <= 100:
    area_circle = 3.14 * radius ** 2
    print(f"The area of the circle is {area_circle:.2f}.")
else:
    print("Invalid Input. Please enter a radius between 1 and 100.")  