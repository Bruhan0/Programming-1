''' 6. Take two positive integers as input. Check whether the second number is the exact reverse of
the first one. Do not use any inbuilt reverse functions. '''

x = int(input())
y = int(input())
reverse = 0
i = x
while i > 0:
    reverse = reverse * 10 + i % 10
    i //= 10
if reverse == y:
    print("Yes, the second number is the exact reverse of the first one.")
else:
    print("No, the second number is not the exact reverse of the first one.")