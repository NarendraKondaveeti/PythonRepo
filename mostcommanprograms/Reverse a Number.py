# ====Raw method(it means no ib-built function or methonds)=====

# Function to reverse a number
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add the digit to the reversed number
        number = number // 10  # Remove the last digit from the number
    return reversed_num

# Input number
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"Reversed Number: {reversed_number}")


# ====with in-built method =================

# Function to reverse a number using in-built methods
def reverse_number(number):
    return int(str(number)[::-1])  # Convert number to string, reverse it, and convert it back to an integer

# Input number
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"Reversed Number: {reversed_number}")
