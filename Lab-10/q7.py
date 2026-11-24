n = tuple(map(int, input().split()))

print(tuple(i for i in n if i % 2 == 0))