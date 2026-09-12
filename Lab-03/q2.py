'''2. Write a program that prompts the user to enter the side of a regular pentagon and displays its area.
 The formula for computing the area of a pentagon is Area = (5 * s2) / (4 * tan(π / 5)), where s is the
length of a side.'''

import math

side = float(input("Enter the side of a regular pentagon: "))
area = (5 * side ** 2) / (4 * math.tan(math.pi / 5))
print("The area of the regular pentagon is:", area)
