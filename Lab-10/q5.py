# 5. Write a function simple_interest(p, r, t=1) that returns the simple interest p * r * t / 100. Read p and r, then print the interest for the default time and for t = 3.

def simple_interest(p, r, t=1):
    return p * r * t / 100

p = int(input())
r = int(input())
print(simple_interest(p, r))
    