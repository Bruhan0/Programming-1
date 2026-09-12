''' 9.Take an odd positive integer N as input and display the following diamond pattern of N lines
using nested loops:
                       *
                      ***
                     *****
                      ***
                       *
(shown for N = 5) '''

n = int(input())

if n % 2 == 0 :
    print("Inavlid input ")
else:
    for i in range(1, n-1,2):
        j = 1
        while j <= n-i:
            print(" ",end="")
            j += 1
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    for i in range(n,0,-2):
        j = 1
        while j <= n-i :
            print(" ",end="") 
            j += 1
        for j in range(1,i+1):
            print("*",end=" ")
        print()





