''' 4. Write a program that reads two integers - hours and minutes based on a 24-hour day format and
calculates what time it will be 15 minutes later. The result should be printed in the following
format hh:mm. Hours should always be between 0 and 23, while minutes should always be
between 0 and 59. Hours should be written with one or two digits as needed, while the minutes
should always be written with two digits - add a leading zero, as needed. Example, Given the time
1:46 as input, the output displayed should be 2:01.'''

hours = int(input("Enter the hours (0-23): "))
minutes = int(input("Enter the minutes (0-59): ")) 
minutes += 15
if minutes >= 60:
    minutes -= 60
    hours += 1
if hours >= 24:
    hours -= 24
print(f"{hours}:{minutes:02d}")