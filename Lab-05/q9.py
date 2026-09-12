'''9. Take a positive integer and a single digit D (0 to 9) as input. Count how many times the digit D
appears in the number. Do not convert the number into a string.'''


n = int(input())
d = int(input())
if d>0 and d<10:
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n //= 10
    print(f"The digit {d} appears {count} times in the number {n}.")

else:
    print("Invalid input")