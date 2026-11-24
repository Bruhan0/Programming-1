n = list(map(int, input().split()))
even = [i for i in nums if i % 2 == 0]
odd = [i for i in nums if i % 2 != 0]
print("Even: ", even)
print("Odd: ", odd)