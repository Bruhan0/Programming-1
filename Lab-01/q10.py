#10. Mini Challenge :
# Attendance Percentage Calculator (eligible if attendance ≥75%),
classes_attended = int(input("Enter the number of classes attended: "))
total_classes = int(input("Enter the total number of classes: "))
if classes_attended < 0 or total_classes <= 0 or classes_attended > total_classes:
    print("Invalid input.")
else:
    percentage = (classes_attended / total_classes) * 100
    print(f"Attendance Percentage: {percentage:.2f}%")
    if percentage >= 75:
        print("You are eligible.")
    else:
        print("You are not eligible.")
