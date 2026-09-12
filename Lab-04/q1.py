''' 1. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the net bonus amount.'''

salary = float(input("Enter your salary: "))
service_years = int(input("Enter your years of service: "))

if service_years > 5:
    bonus = salary * 0.05
    print(f"Congo! You r eligible for a bonus of: {bonus}")
else:
    print("Sorry,Bud! You r not eligible for a bonus.")
