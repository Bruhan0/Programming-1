'''10.Take a positive integer N as input and display all its divisors, one in each line, followed by the
total count of divisors. Using this count, print whether N is a prime number or not.'''


n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count += 1
print(f"Total divisors: {count}")
if count == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")