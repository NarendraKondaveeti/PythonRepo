# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the sum of first N natural numbers
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):  # Loop through numbers from 1 to N
        sum += i  # Add each number to the sum
    return sum

# Input N
n = int(input("Enter a number: "))

result = sum_of_natural_numbers(n)
print(f"The sum of first {n} natural numbers is: {result}")


# ====with in-built method =================
# Function to find the sum of first N natural numbers using the formula
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2  # Formula for the sum of first N natural numbers

# Input N
n = int(input("Enter a number: "))

result = sum_of_natural_numbers(n)
print(f"The sum of first {n} natural numbers is: {result}")

