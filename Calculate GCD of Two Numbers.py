# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the GCD of two numbers using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Swap a and b, and replace b with the remainder of a divided by b
    return a

# Input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd_result = gcd(a, b)
print(f"GCD of {a} and {b} is: {gcd_result}")



# ====with in-built method =================
import math

# Function to find the GCD using the math library
def gcd(a, b):
    return math.gcd(a, b)  # Using the in-built gcd function from the math module

# Input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd_result = gcd(a, b)
print(f"GCD of {a} and {b} is: {gcd_result}")
