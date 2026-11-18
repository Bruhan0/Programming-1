s = input("Enter a string: ")
count = 0

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        count += 1

print("Changes needed:", count)