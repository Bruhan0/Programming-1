#2 finding the length of the last word in sentence
sen = input("").split()
if sen :
    print("ength of the last word in sentence:", len(sen[-1]))
else :
    print("no sentence found")