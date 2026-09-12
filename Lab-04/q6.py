''' 6. Tom Cat likes to sleep all day but, unfortunately, his owner is always playing with him whenever
he has free time. To sleep well, the norm of games that Tom has is 30,000 minutes per year. The
time for games he has depends on the holidays that his owner has:
• During workdays, his owner plays with him 63 minutes per day.
• During holidays, his owner plays with him 127 minutes per day.
Write a program that reads the number of holidays and prints whether Tom can sleep well and
how much the difference from the norm for the current year is. It is assumed that there are 365
days in one year.'''

holidays = int(input("Enter the number of holidays: "))
workdays = 365 - holidays
total = (workdays * 63) + (holidays * 127)
diff = abs(total - 30000)
if total > 30000:
    print(f"Tom will sleep well.\nHe has {diff} minutes more from the norm.")
else:
    print(f"Tom will not sleep well.\nHe has {diff} minutes less from the norm.")