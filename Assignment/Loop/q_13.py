#  Use nested loops to print a pyramid pattern of *.

rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(i):
        print("* ", end="")

    print()

