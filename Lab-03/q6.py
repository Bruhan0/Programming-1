'''6. Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of
b moves to c, and the value of c moves to a, without using a fourth variable or multiple
assignment operation.'''

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)
print("After rotation:")
print("a =", a)
print("b =", b)
print("c =", c)


''' or '''


a , b , c = b , c , a 

print("After rotation:")
print("a =", a)
print("b =", b)
print("c =", c)
