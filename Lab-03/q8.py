'''8. Suppose a water tank initially holds V litres of water. Every day 5% of the water present in the tank
evaporates, and then exactly 10 litres of fresh water is added to it. Therefore, the daily retention
rate is 1 – 0.05 = 0.95. After the first day, the quantity in the tank becomes
V * 0.95 + 10
After the second day, the quantity in the tank becomes
(V * 0.95 + 10) * 0.95 + 10
After the third day, the quantity in the tank becomes
((V * 0.95 + 10) * 0.95 + 10) * 0.95 + 10
and so on.
Write a program that prompts the user to enter the initial quantity of water and the number of
days (N) and displays the quantity of water in the tank after the Nth day. Check for valid and
invalid cases. Do not use loops.'''

V = float(input("Enter the initial quantity of water in litres: "))
N = int(input("Enter the number of days: "))
if V < 0 or N < 0:
    print("Invalid input")
else:
    quantity = V * (0.95 ** N) + 10 * ((1 - (0.95 ** N)) / (0.05)) or quantity = 200 + (V - 200) * (0.95 ** N)
    print("The quantity of water in the tank after", N, "days is:", quantity, "litres.")