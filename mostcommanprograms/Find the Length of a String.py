# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the length of a string
def string_length(s):
    length = 0
    for char in s:  # Loop through each character in the string
        length += 1  # Increment the length for each character
    return length

# Input string
string = input("Enter a string: ")

result = string_length(string)
print(f"The length of the string '{string}' is: {result}")


# ====with in-built method =================

# Function to find the length of a string using len()
def string_length(s):
    return len(s)  # Use Python's built-in len() function

# Input string
string = input("Enter a string: ")

result = string_length(string)
print(f"The length of the string '{string}' is: {result}")
