# ====Raw method(it means no ib-built function or methonds)=====

# Function to check if a string contains another string
def contains_string(main_string, sub_string):
    for i in range(len(main_string) - len(sub_string) + 1):  # Loop through the main string
        if main_string[i:i+len(sub_string)] == sub_string:  # Check if the substring matches
            return True
    return False

# Input strings
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check: ")

# Check if the main string contains the substring
if contains_string(main_string, sub_string):
    print(f"'{sub_string}' is found in '{main_string}'.")
else:
    print(f"'{sub_string}' is not found in '{main_string}'.")

# ====with in-built method =================

# Function to check if a string contains another string
def contains_string(main_string, sub_string):
    return sub_string in main_string  # Use the 'in' operator to check for substring

# Input strings
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check: ")

# Check if the main string contains the substring
if contains_string(main_string, sub_string):
    print(f"'{sub_string}' is found in '{main_string}'.")
else:
    print(f"'{sub_string}' is not found in '{main_string}'.")
