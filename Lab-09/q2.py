s = input()
res = [word for word in s.split() if len(word)>3]
print(res)