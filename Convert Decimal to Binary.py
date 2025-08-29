# ====Raw method(it means no ib-built function or methonds)=====
# Function to convert decimal to binary
def decimal_to_binary(n):
    binary = ""  #10 = 1010
    while n > 0: # 10, 5, 2, 1
        remainder = n % 2  # Find the remainder when divided by 2, % is Modulus Operator it's returns Remainder
        binary = str(remainder) + binary  # Append remainder at the front
        n = n // 2  # Update n to n divided by 2 (integer division), // is Floor Division Operator it's returns Quotient (int)
        # / is Normal Division Operator it's returns Quotient (float)s
    return binary if binary else "0"  # Handle the case when n is 0
    # if binary else "0" return binary

# Input decimal number
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")

# ====with in-built method =================

# Function to convert decimal to binary using bin()
def decimal_to_binary(n):
    return bin(n)[2:]  # Remove the '0b' prefix from the binary representation 0b1010

# Input decimal number
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")