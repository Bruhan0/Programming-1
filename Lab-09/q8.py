s = input()
res = [int(x) for x in s if s.isdigit()]
print("List of nums: ",res)
print("sum of list of nums: ",sum(res))