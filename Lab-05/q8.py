'''8. Take a positive integer N as input and display the following pattern of N lines:
*
* *
* * *
* * * *
(till N lines)'''

N = int(input())
for i in range(N):
    for j in range(1,i+1):
        print("*", end=' ')
    print()
    