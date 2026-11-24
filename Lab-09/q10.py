n = list(map(int, input().split()))
pos = 0
for i in range(len(n)) :
    if n[i] != 0 :
        n[pos] , n[i] = n[i] , n[pos]
        pos += 1
print(n)