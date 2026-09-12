# 3. Display the following patterns for N lines (value of N taken from the user) using while loop:
'''a)   1                       
        1 2
        1 2 3
        1 2 3 4
        (till N lines)'''

n = int(input())
i = 1
while i <= n:     #Using for loop is piece of cake for these types of pattern problems, but i appreciate my lecturer, lettin us to try differently....
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1




''' b)  * * * *
        * * *
        * *
        *
        (till N lines) '''

n = int(input())
i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1



'''c)            *
               * *
             * * *
           * * * *
     (till N lines) '''

n = int(input())
i = 1
# Starts from row1 and goes till nth row
while n >= i:  # repeats till the condition satisfies
    j = 1      #starts counting the space from 1
    while j <= n - i:           #we nneed n-i spaces, so
        print(" ", end=" ")     # prints the spaces without going to the next line
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

