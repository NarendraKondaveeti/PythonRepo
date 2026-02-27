# ====Raw method(it means no ib-built function or methonds)=====
# Function to print Pascal's Triangle
def print_pascals_triangle(n):
    for row in range(n):
        # Print leading spaces for alignment
        print(" " * (n - row - 1), end="")

        # Calculate each element in the row
        number = 1
        for col in range(row + 1):
            print(number, end=" ")
            number = number * (row - col) // (col + 1)  # Binomial coefficient formula

        print()  # Move to the next line

# Input number of rows
n = int(input("Enter the number of rows: "))
print_pascals_triangle(n)


# ====with in-built method =================
import math

# Function to print Pascal's Triangle using math.factorial
def print_pascals_triangle(n):
    for row in range(n):
        # Print leading spaces for alignment
        print(" " * (n - row - 1), end="")

        # Calculate each element in the row using factorials
        for col in range(row + 1):
            element = math.factorial(row) // (math.factorial(col) * math.factorial(row - col))
            print(element, end=" ")

        print()  # Move to the next line

# Input number of rows
n = int(input("Enter the number of rows: "))
print_pascals_triangle(n)

