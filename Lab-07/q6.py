#6 , Palindrome or not

s = input()
rev = ""

for ch in range(len(s)-1,-1,-1):
    rev += s[ch]
if s == rev :
    print("Palindrome")
else :
    print("Not Palindrome")