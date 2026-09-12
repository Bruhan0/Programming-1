# 7. Write a program that finds all numbers in the range [1 … 1000], that end in 6.


for num in range(1, 1001):
    if num % 10 == 6:
        print(num)
