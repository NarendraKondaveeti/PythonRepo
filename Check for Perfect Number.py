# ====Raw method(it means no ib-built function or methonds)=====
# Function to check if a number is a perfect number
def is_perfect_number(n):
    if n <= 0:
        return False  # Perfect numbers are positive

    sum_of_divisors = 0
    for i in range(1, n):  # Loop through numbers less than n
        if n % i == 0:  # Check if i is a divisor
            sum_of_divisors += i

    return sum_of_divisors == n  # A perfect number equals the sum of its divisors

# Input number
number = int(input("Enter a number: "))

if is_perfect_number(number):
    print(f"{number} is a Perfect Number")
else:
    print(f"{number} is not a Perfect Number")


# ====with in-built method =================

# Function to check if a number is a perfect number using sum()
def is_perfect_number(n):
    if n <= 0:
        return False  # Perfect numbers are positive

    # Calculate the sum of proper divisors using a list comprehension
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors == n  # A perfect number equals the sum of its divisors

# Input number
number = int(input("Enter a number: "))

if is_perfect_number(number):
    print(f"{number} is a Perfect Number")
else:
    print(f"{number} is not a Perfect Number")
