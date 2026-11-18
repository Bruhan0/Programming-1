s = input()

digits = 0
alpha = 0
upp = 0
low = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1

    elif ch.isalpha():
        alpha += 1

        if ch.isupper():
            upp += 1
        elif ch.islower():
            low += 1

    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alpha)
print("Uppercase:", upp)
print("Lowercase:", low)
print("Special characters:", special)