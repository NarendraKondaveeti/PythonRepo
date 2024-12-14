# ===1. Raw Method (Without In-Built Functions)

n = 20  # Check prime numbers up to this number

for num in range(2, n + 1):  # Loop through numbers from 2 to n
    is_prime = True  # Assume each number is prime
    for i in range(2, num):  # Check divisibility
        if num % i == 0:
            is_prime = False  # Not a prime number
            break
    if is_prime:
        print(f"{num} is a prime number")


"""# Libraries for Prime Numbers in Python
SymPy Library:
Python's sympy library lo isprime() function untundi.
Ee function oka number prime kaadu ani direct ga cheptundi.
"""

from sympy import isprime

n = 20
primes = [num for num in range(2, n + 1) if isprime(num)]
print("Prime numbers:", primes)
