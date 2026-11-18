s = input()
words = s.split("-")

for i in range(len(words)):
    for j in range(len(words) - 1 - i):
        if words[j] < words[j+1] :
            words[j] , words[j+1] = words[j+1] , words[j] 
res = "-".join(words) # for converting list into strings
print(res)