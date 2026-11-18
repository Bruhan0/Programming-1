s = input("Enter a string: ")
count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1. #safe one , cuz it wont throw an error if an element isnt there

max_char = ""
max_count = 0

for x, y in count.items():
    if y > max_count:
        max_char = x
        max_count = y

print(max_char, max_count)