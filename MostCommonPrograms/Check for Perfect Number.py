
"""If a number (n) is divided by all smaller numbers (from 1 to n-1), and the numbers that give a remainder of 0 are added together, 
and their sum equals the original number (n), then it is called a perfect number

Example Input and Output:-
Input: 6
Divisors: 1, 2, 3
Sum: 1 + 2 + 3 = 6
Output: 6 is a Perfect Number

Input: 10
Divisors: 1, 2, 5
Sum: 1 + 2 + 5 = 8
Output: 10 is not a Perfect Number

Input: 28
Divisors: 1, 2, 4, 7, 14
Sum: 1 + 2 + 4 + 7 + 14 = 28
Output: 28 is a Perfect Number

"""

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

#===
def is_perfect(n):
    sum = 0
    for i in range(1, n//2 + 1): # Optimization: no need to go till n-1
        if n % i == 0:
            sum += i
    return sum == n
