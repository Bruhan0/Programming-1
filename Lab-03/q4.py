''' 4. Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two
digits separately. Also, check if the two sums are equal or not.'''

num = int(input("Enter a 4-digit number: "))
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
sum1 = a + b
sum2 = c + d

if sum1 == sum2:
    print("The sums of the first two and last two digits are equal.")
else:
    print("The sums of the first two and last two digits are not equal.")