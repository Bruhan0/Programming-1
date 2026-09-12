''' 5. Display the first N terms of the sequence of powers of 2. Do not use the ** operator or the
pow() function.
1, 2, 4, 8, 16, 32, ….. till N terms'''

N = int(input())
count = 0
result = 1
while count < N:
    print(result, end=' ')
    result *= 2
    count += 1