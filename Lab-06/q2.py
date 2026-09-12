''' 2. Parking Slot Allotment. A parking area has slots numbered from 1 to 1000. Every slot whose
number is divisible by N is reserved. However, a reserved slot whose number is also divisible
by 4 is kept for electric vehicle charging and is not given to staff. Display the slot numbers
given to the staff. Use the continue statement with a while loop.
Input: A single positive integer N.
Output: The slot numbers given to the staff, separated by a single space.
Constraints: 1 ≤ N ≤ 1000.'''


n = int(input())
i = 1
while i <= 1000:            
    if i % n == 0:       #more simply, if i % n == 0 and i % 4 != 0: but Lab says to use continue
        if i % 4 == 0:
            i += 1
            continue
        print(i, end=" ")
    i += 1
