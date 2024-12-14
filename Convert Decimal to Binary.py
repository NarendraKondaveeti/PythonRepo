# ====Raw method(it means no ib-built function or methonds)=====
# Function to convert decimal to binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2  # Find the remainder when divided by 2
        binary = str(remainder) + binary  # Append remainder at the front
        n = n // 2  # Update n to n divided by 2 (integer division)
    return binary if binary else "0"  # Handle the case when n is 0

# Input decimal number
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")


# ====with in-built method =================

# Function to convert decimal to binary using bin()
def decimal_to_binary(n):
    return bin(n)[2:]  # Remove the '0b' prefix from the binary representation

# Input decimal number
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")
