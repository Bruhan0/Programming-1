''' Print the following table.
                    Addition Table
                    1 2 3 4 5 6 7 8 9
                    ---------------------------------------
                    1 | 2 3 4 5 6 7 8 9 10
                    2 | 3 4 5 6 7 8 9 10 11
                    3 | 4 5 6 7 8 9 10 11 12
                    4 | 5 6 7 8 9 10 11 12 13
                    5 | 6 7 8 9 10 11 12 13 14
                    6 | 7 8 9 10 11 12 13 14 15
                    7 | 8 9 10 11 12 13 14 15 16
                    8 | 9 10 11 12 13 14 15 16 17
                    9 | 10 11 12 13 14 15 16 17 18.     '''


for i in range(1, 10):
    if i == 1:
        print("Addition Table")
        for j in range(1, 10):
            print(j, end=" ")
        print("\n-----------------------------")
    for j in range(1, 10):
        if j == 1:
            print(f"{i} |", end=" ")
        print(i + j, end=" ")
    print()