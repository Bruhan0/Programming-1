def get_grades(marks):
    if marks > 80 :
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
res = []    
n = int(input())
d = {}
for _ in range(n):
    name , marks = input().split()
    grade = get_grades(int(marks))
    res.append(f"{name}:{grade}")
    d[grade] = d.get(grade, 0) + 1
for i in res:
    print(i)
print("Grade count:")
print(d)