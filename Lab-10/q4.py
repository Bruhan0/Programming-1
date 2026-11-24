# 4. Read a word and build a dictionary that stores how many times each letter occurs in it. Print the dictionary.
s = input().strip().lower()
d = {}
for i in s:
    d[i] = 1 + d.get(i , 0)
print(d)