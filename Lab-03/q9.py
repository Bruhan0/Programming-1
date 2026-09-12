''' 9. Enter the coefficients of two straight lines a1x + b1y = c1 and a2x + b2y = c2 and display their point
of intersection. Handle all the cases for invalid input as well as the cases where the two lines are
parallel or coincident, and display the solution till exactly 2 decimal places.'''

a1 = float(input("Enter the coefficient a1: "))
b1 = float(input("Enter the coefficient b1: "))
c1 = float(input("Enter the coefficient c1: "))
a2 = float(input("Enter the coefficient a2: "))
b2 = float(input("Enter the coefficient b2: "))
c2 = float(input("Enter the coefficient c2: "))

if a1 == 0 and b1 == 0:
    print("Invalid input for the first line.")
elif a2 == 0 and b2 == 0:
    print("Invalid input for the second line.")
elif a1 * b2 == a2 * b1:
    if a1 * c2 == a2 * c1:
        print("The two lines are coincident.")
    else:
        print("The two lines are parallel.")
else:
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    print("The point of intersection is: ({x:.2f}, {y:.2f})")
    