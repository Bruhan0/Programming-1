''' 6. Display all the Armstrong numbers between 1 and N, where the value of N is taken as input
from the user.'''

n = int(input())
count = 0
for i in range(1, n + 1):
    x = i
    digit_count = 0
    while x > 0:
        digit_count += 1
        x //= 10
    x = i
    total = 0
    while x > 0:
        total += (x % 10) ** digit_count
        x //= 10
    if total == i:
        print(i, end=" ")
        count += 1
print(f"\ncount: {count}")
