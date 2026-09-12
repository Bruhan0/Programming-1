# 4. Modify Problem 3 to accept dimensions in feet and display the area in square metres.
length = float(input("Enter the length in feet: "))
width = float(input("Enter the width in feet: "))
# Conversion factor: 1 foot = 0.30 metres
length_meters = length * 0.30
width_meters = width * 0.30
area_meters = length_meters * width_meters
print(f"The area of the rectangule is {area_meters:.2f} square metres.")  