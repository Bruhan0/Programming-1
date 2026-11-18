s = input("Enter a string: ")
seen = set()
result = ""

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)

print(result)