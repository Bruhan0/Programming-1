def stats(nums):
    return(min(nums), max(nums), sum(nums)/len(nums))
nums = list(map(int, input().split()))
print(stats(nums))