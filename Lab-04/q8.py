# 8.Write a program that reads n integers and finds their sum.
n = int(input("Enter the number of integers: "))
total = 0
for _ in range(n):
    num = int(input("Enter an integer: "))
    total += num
print(f"The sum of the {n} integers is: {total}")