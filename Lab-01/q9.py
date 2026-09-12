# 9. Input the number of seconds (1–86400) and display the equivalent time in HH:MM: SS format.
seconds = int(input("Enter the number of seconds (1–86400): "))
if 1 <= seconds <= 86400:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"Equivalent time: {hours:02}:{minutes:02}:{remaining_seconds:02}")
else:
    print("Invalid Input. Please enter a number of seconds between 1 and 86400.")