'''2.Take a positive integer as input and display the product of its digits. The number can be of any
length.'''

n = int(input())
product = 1
while n > 0:
    product *= n % 10
    n //= 10
print(product)