# ====Raw method(it means no ib-built function or methonds)=====

# Function to check if a string is empty
def is_empty(s):
    if s == "":  # Check if the string is empty
        return True
    return False

# Input string
string = input("Enter a string: ")

if is_empty(string):
    print("The string is empty.")
else:
    print("The string is not empty.")

# ====with in-built method =================

# Function to check if a string is empty using len()
def is_empty(s):
    return len(s) == 0  # Return True if the length is 0, meaning the string is empty

# Input string
string = input("Enter a string: ")

if is_empty(string):
    print("The string is empty.")
else:
    print("The string is not empty.")
