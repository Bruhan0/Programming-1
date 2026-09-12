''' 4. Take a positive integer as input from the user and display its octal equivalent via the repeated
division method. (without using any inbuilt function or format specifier). The final result
should be displayed as a string. Check if the result matches the output of inbuilt oct() function.'''

''' basic idea , umm....
ex - 
n = 25
25 / 8 = 3 remainder 1 {this in python is 25 % 8 = 1, and 25 // 8 = 3}
3 / 8 = 0 remainder 3
and it reads from bottom, so 31...
'''

n = int(input())
octal = ""
while n > 0:
    octal = str(n % 8) + octal       
    n //= 8
print(octal)