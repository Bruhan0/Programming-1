'''3. Canteen Billing Counter. The canteen cashier enters the amount of every bill of the day one
by one. To close the counter, the cashier enters -999. A bill is called a large bill if its amount is
greater than N, otherwise it is a small bill. Count the large bills and the small bills of the day.
Input: The first line contains the integer N. Every following line contains one bill amount. The
input ends with the value -999, which is not a bill.
Output: Print the count of large bills in the first line and the count of small bills in the second
line.
Constraints: 1 ≤ N ≤ 100000, at most 100 bills are entered, every bill amount is a positive
integer.'''

N = int(input())
count = 0
while True:
    bill = int(input())
    if bill == -999:
        break
    if bill > N:
        count += 1
print(count)