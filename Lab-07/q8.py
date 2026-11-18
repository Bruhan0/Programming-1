nums = [int(num) for num in input().split()]         

if len(nums) == 0 :
    print("Enter numbers!!!")
else :
    total = 0
    product = 1
    smallest = nums[0]

    for i in range(len(nums)-1):
        total += nums[i]
        product *= nums[i]
        if nums[i] < smallest :
            smallest = nums[i]
    print("Sum:", total)
    print("Product",product)
    print("Smallest",smallest)

