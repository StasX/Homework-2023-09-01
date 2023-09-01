multiplication_board = []

# Create table
for i in range(1, 11):
    multiplications = []
    for j in range(1, 11):
        multiplication = i*j
        multiplications.append(multiplication)
    multiplication_board.append(multiplications)

# Print table
for row in multiplication_board:
    for col in row:
        if 1 <= col <= 9:
            start = "   "
        elif 10 <= col <= 99:
            start = "  "
        else:
            start = " "
        print(f"{start}{col}", end=" ")
    print()

# Calculate and print sum of all numbers in matrix
total = 0
for numbers in multiplication_board:
    for number in numbers:
        total += number
print("Sum of all numbers is", total)
