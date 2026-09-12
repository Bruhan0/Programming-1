'''3. Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can,
further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases
also. '''

x = float(input("Enter the first angle of the triangle: "))
y = float(input("Enter the second angle of the triangle: "))
z = float(input("Enter the third angle of the triangle: "))
# Check if the angles can form a truiangle
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print("The angles can form a triangle.")


    if x < 90 and y < 90 and z < 90:
        print("The triangle is acute-angled.")
    elif x < 90 and y < 90 and z < 90:
        print("The triangle is acute-angled.")
    else:
        print("The triangle is obtuse-angled.")
else:
    print("The angles cannot form a triangle.")