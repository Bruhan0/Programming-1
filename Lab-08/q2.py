s = input()
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i].lower()

print(result)