# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit to the total
        n = n // 10  # Remove the last digit from the number
    return total

# Input number
number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")


# ====with in-built method =================

# Function to find the sum of digits of a number using str()
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))  # Convert number to string and sum each digit

# Input number
number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")
