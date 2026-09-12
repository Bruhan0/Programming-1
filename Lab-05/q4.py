'''4. Take a positive integer N and a positive integer P as input and find the value of N raised to the
power P using a while loop. Do not use the ** operator or the pow() function. Handle invalid
cases as well.'''

N = int(input())
P = int(input())
if N < 0 or P < 0:
    print("Invalid input")
else:
    result = 1
    count = 0
    while count < P:
        result *= N
        count += 1
    print(result)