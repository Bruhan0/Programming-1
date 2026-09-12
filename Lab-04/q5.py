''' 5. A student has to travel n kilometers. He can choose between three types of transportation:
Taxi. Starting fee: 33.58 INR. Day rate: 37.89 INR/km. Night rate: 43.17 INR/km.
Bus. Day / Night rate: 4.32 INR/km. Can be used for distances of a minimum of 20 km.
Train. Day / Night rate: 2.88 INR/km. Can be used for distances of a minimum of 100 km.
Write a program that reads the number of kilometers n and period of the day (day or night) and
calculates the price for the cheapest transport.'''

n = float(input("Enter the number of kilometers to travel: "))
time = input()
# logic,
''' taxi ; always available, 
day, 33.58 + 37.89 * n
night, 33.58 + 43.17 * n
bus ; available only if n >= 20,
day, 4.32 * n
train ; available only if n >= 100,
day, 2.88 * n
'''
taxi_rate = 37.89 if time == "day" else 43.17
taxi = 33.58 + taxi_rate * n

bus = n * 4.32

train = n * 2.88

cheapest = taxi
if n >= 20:
    if cheapest > bus:
        cheapest = bus
if n >= 100:
    if cheapest > train:
        cheapest = train
print(f'{cheapest:.2f} INR')