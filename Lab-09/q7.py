s = input()
res = ' '.join(word[::-1] for word in s.split())
print("Reversed str: ",res)