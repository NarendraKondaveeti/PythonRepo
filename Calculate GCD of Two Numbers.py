# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the GCD of two numbers using Euclidean algorithm
GCD (Greatest Common Divisor) ante rendu numbers ki common ga unna biggest factor (divisor).
Idi HCF (Highest Common Factor) ani kuda antaru.

📌 Mathematical Definition
👉 GCD(m, n) = Two numbers ki common ga vache biggest number.
🔹 GCD(12, 18) Calculation
✅ 12 divisors → 1, 2, 3, 4, 6, 12
✅ 18 divisors → 1, 2, 3, 6, 9, 18
✅ Common divisors → 1, 2, 3, 6
✅ Biggest common divisor → 6

a % b ni recursive ga calculate chesthu b = 0 ayye varaku loop run avuthundi.
Final ga a value GCD avutundi.

👉 So, GCD(12, 18) = 6

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
