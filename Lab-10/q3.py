students = input().split()
d = {}
for i in students:
    d[i] = 1 + d.get(i , 0)

for name , votes in d.items():
    print(f"{name}:{votes}")
winner = max(d , key = d.get)
print("winner", winner)