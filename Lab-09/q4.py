nums = list(map(int, input().split()))
lar = nums[0]
smal = nums[0]
for i in nums:
    if lar < i :
        lar = i
    if smal > i :
        smal = i
print("Largest: ",lar)
print("Smallest: ",smal)