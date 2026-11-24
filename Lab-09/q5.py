s = input()
lar = s[0]
for word in s:
    if len(word) > len(lar) :
        lar = word
print("Largest: ",lar)