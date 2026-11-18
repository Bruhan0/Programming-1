#4 , Pangram or not

s = input("").lower()

if set(s) > set("qwertyuiopasdfghjklzxcvbnm") :
    print("Given sentence is Pangram")
else:
    print("Given sentence is not Pangram")