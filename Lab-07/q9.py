elements = [int(nums) for nums in input("").split()]

for i in range(len(elements)):
    for j in range(len(elements) - 1 - i):
        if elements[j] < elements[j+1] :
            elements[j] , elements[j+1] = elements[j+1] , elements[j] 
print("Descending order:", elements)