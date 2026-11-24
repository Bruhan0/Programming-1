#1.Read a list of integers and a value V. Convert the list into a tuple and print the tuple, its length, the number of times V occurs in it, and the index of the first occurrence of V.


nums = list(map(int, input().split()))
v = int(input())
t = tuple(nums)
print("Tuple:",t)
print("Length:",len(t))
print("count of",v ,":" ,t.count(v))
print("Index of",v ,":" ,t.index(v))