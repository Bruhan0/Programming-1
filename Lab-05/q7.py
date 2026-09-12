'''7. ake an integer as input and check whether it is a perfect number or not (a perfect number is
equal to the sum of all its divisors other than itself, for example 28 = 1 + 2 + 4 + 7 + 14). Handle
invalid conditions and make your code efficient by minimizing the number of loop iterations.'''

n = int(input())
if n <= 0:
    print("Invalid input")
else:
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum == n:
        print("Yes, it is a perfect number.")
    else:
        print("No, it is not a perfect number.")