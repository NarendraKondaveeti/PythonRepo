"""
An Armstrong number is a number where, if you take each digit of the number, raise it to the power of the total number of digits,
and then add them together, the sum will be equal to the original number.

Example:
153:
Number of digits = 3
Split digits: 1, 5, 3
Calculate:
1**3 + 5**3 + 3**3 = 1+125+27 = 153
Since the sum equals the original number, 153 is an Armstrong number.

Simple Formula:
For a number, if you add each of its digits raised to the power of the total number of digits, and the result is equal to the number itself, 
it's an Armstrong number
"""

# Raw Python Program (without in-built methods):
# Function to check if a number is Armstrong
def is_armstrong(number):
    num_str = str(number)  # Convert the number to string to count digits
    num_digits = len(num_str)  # Number of digits in the number
    sum_of_powers = 0
    
    # Loop through each digit and calculate the sum of digits raised to the power of num_digits
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    return sum_of_powers == number  # Return True if the sum is equal to the number, else False

# Input number
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

# Python Program with In-built Method (Using map() and pow()):
# Function to check if a number is Armstrong using in-built methods
def is_armstrong(number):
    num_str = str(number)  # Convert the number to string to count digits
    num_digits = len(num_str)  # Number of digits in the number
    sum_of_powers = sum(map(lambda digit: int(digit) ** num_digits, num_str))  # Calculate the sum of digits raised to the power of num_digits
    
    return sum_of_powers == number  # Return True if the sum is equal to the number, else False

# Input number
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
