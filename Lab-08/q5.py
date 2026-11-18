s = input("Enter a sentence: ")
words = s.split()

for word in words:
    print(len(word), end=" ")