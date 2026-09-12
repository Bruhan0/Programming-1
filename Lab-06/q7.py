''' 7. Display the following pattern using nested loops:
                   1
                  2 2
                 3 3 3
                4 4 4 4
(till N lines) '''

n = int(input())
for i in range(1,n+1):
    j = 1
    while j <= n-i+1 :
        print(" ", end='')
        j += 1
    for j in range(1,i+1):
        print(i, end=' ')
    print()