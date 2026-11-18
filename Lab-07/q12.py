s = input()
res = ''

for ch in s :
    if ch not in res :
        res += ch
print(res)


#2
'''
items = dict.fromkeys(s)
res = " ".join(items)
print(res) '''