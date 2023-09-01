matrix = [[12, 23, 34, 45], [56, 67, 78, 89], [10, 20, 30, 40]]

# Display matrix
print(matrix)

# Calculate and display the sum of numbers in matrix
total = 0
for row in matrix:
    for col in row:
        total += col
print("Sum of all numbers in matrix is:", total)
print("\n---------------------------------\n")

# Calculate and display the average of numbers in matrix
count = 0
for row in matrix:
    count += len(row)
avg = total/count
print("Average of all numbers in matrix is:", avg)
print("\n=================================\n")

# Calculate and display max number in matrix
max_number = matrix[0][0]
for row in matrix:
    for col in row:
        if col > max_number:
            max_number = col
print("Max number in matrix is:", max_number)
print("\n=================================\n")

# Calculate and display min number in matrix
min_number = matrix[0][0]
for row in matrix:
    for col in row:
        if col < min_number:
            min_number = col
print("Min number in matrix is:", min_number)
print("\n=================================\n")

# Display a two-dimensional list as a table
for row in matrix:
    for col in row:
        # If number is odd change it to "X"
        if col % 2 != 0:
            col = "X"
        print(col, end=" ")
    print()
print("\n=================================\n")

# Display a two-dimensional list as a table
for row in matrix:
    for col in row:
        # If number divisible by 7 or ends to 7 change it to "*"
        if col % 7 == 0 or col % 10 == 7:
            col = "*"
        print(col, end=" ")
    print()
print("\n=================================\n")
