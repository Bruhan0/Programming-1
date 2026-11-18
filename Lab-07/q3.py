#3 , Check wether a word occurs in a sentence and count its occurnces

s = input()
word = input()

count = s.count(word)

if word in s:
    print("word occur in sentence")
    print("Occurences:", count)
else :
    print("Word not occur")