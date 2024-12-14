# ====Raw method(it means no ib-built function or methonds)=====

# Function to find the factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Input number
num = int(input("Enter a number: "))

result = factorial(num)
print(f"The factorial of {num} is: {result}")

