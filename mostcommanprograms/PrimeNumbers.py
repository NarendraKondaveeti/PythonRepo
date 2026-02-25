# ===1. Raw Method (Without In-Built Functions)

num = int(input("Enter a Number = "))

for n in range(2, num):  #
    for i in range(2, n):
        if n % i ==0:
            break
    else:
        print(n, end=" ")


# ===2. other Way
for num in range(2, 21):  # 2 nunchi 20 varaku
    count = 0
    for i in range(1, num + 1):  # 1 nunchi num varaku anni check cheyyali
        if num % i == 0:
            count += 1  # remainder 0 ante divisor, count penchadam
    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is NOT a prime number")



"""# Libraries for Prime Numbers in Python
SymPy Library:
Python's sympy library lo isprime() function untundi.
Ee function oka number prime kaadu ani direct ga cheptundi.
"""

from sympy import isprime

n = int(input("Enter a Number = "))
primes = [num for num in range(2, n + 1) if isprime(num)]
print("Prime numbers:", primes)
