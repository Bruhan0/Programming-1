'''7. Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is
exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad
number. '''

num = int(input("Enter a 3-digit number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
sum = a + b + c

if num % sum == 0:
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")