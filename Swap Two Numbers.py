# ====Raw method(it means no ib-built function or methonds)=====
# Function to swap two numbers
def swap_numbers(a, b):
    # Using a temporary variable to swap the values
    temp = a
    a = b
    b = temp
    return a, b

# Input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = swap_numbers(a, b)
print(f"After swapping: First number = {a}, Second number = {b}")


# ====with in-built method =================

# Function to swap two numbers using tuple unpacking
def swap_numbers(a, b):
    a, b = b, a  # Swap using tuple unpacking
    return a, b

# Input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = swap_numbers(a, b)
print(f"After swapping: First number = {a}, Second number = {b}")
