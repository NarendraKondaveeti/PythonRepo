# Factorial for a value Example Factorial for 5
# 5 * 4 * 3 * 2 * 1 = 120, so 120 is the Factorial value for 5

# ====Raw Method (No In-Built Functions)====
n = 5  # Input number
factorial = 1  # Initialize result

for i in range(1, n + 1):  # Loop from 1 to n
    factorial = factorial * i  # Multiply with current number

print(f"The factorial of {n} is {factorial}")

# === 2. Without Function but Using In-Built Method

import math  # Import math module
n = int(input("Enter n value"))
print(f"Factorial value for {n}", math.factorial(n))
 