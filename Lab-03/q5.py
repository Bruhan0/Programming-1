'''5. Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built
functions and do not use loops. Also print the position of that digit counted from the left. If the
largest digit occurs more than once, print the position of its first occurrence.'''

num = int(input("Enter a 5-digit number: "))
a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num // 10) % 10
e = num % 10
largest = a
position = 1
if b > largest:
    largest = b
    position = 2
if c > largest:
    largest = c
    position = 3
if d > largest:
    largest = d
    position = 4
if e > largest:
    largest = e
    position = 5
print("The largest digit is:", largest)
print("The position of the largest digit is:", position)