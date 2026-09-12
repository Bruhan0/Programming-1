''' 1.Street Lamps on a Highway. The lamp posts on a highway are numbered from X to Y. Every
post whose number is divisible by N is out of order. Display the numbers of the posts that are
still working, along with how many of them there are. Consider the posts numbered X ≤ i < Y.
Input: Three integers X, Y and N, each on a separate line.
Output: In the first line, the numbers of the working posts separated by a single space. In the
second line, the count of working posts.
Constraints: 1 ≤ X < Y ≤ 10000, 1 ≤ N ≤ 100.
in the second case every post is divisible by 1, so no post is working and the first line of the output stays
empty.'''

X = int(input())
Y = int(input())
N = int(input())
count = 0

for i in range(X, Y):
    if i % N != 0:
        print(i, end=' ') 
        count += 1  
print() # goes to new line after completing a loop
print(count)
