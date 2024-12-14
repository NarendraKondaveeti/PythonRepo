# ====Raw method(it means no ib-built function or methonds)=====
# Function to count the number of digits in a number
def count_digits(number):
    count = 0
    while number != 0:
        number = number // 10  # Remove the last digit by integer division
        count += 1  # Increment the count for each digit
    return count

# Input number
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"Number of digits: {digit_count}")


# ====with in-built method =================

# Function to count the number of digits using in-built methods
def count_digits(number):
    return len(str(abs(number)))  # Convert the number to a string and count the length

# Input number
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"Number of digits: {digit_count}")
