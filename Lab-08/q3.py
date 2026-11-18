s = input()
upper = lower = digit = special = False

for ch in s:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch != " ":
        special = True
count = upper + lower + digit + special

if len(s) < 8 or count == 1:
    print("WEAK")
elif count == 4:
    print("STRONG")
else:
    print("MODERATE")