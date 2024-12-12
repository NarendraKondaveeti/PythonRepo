# =========without function==============

input_string = "madam"
reversed_string = ""

# Reverse the string manually
for char in input_string:
    reversed_string = char + reversed_string

# Check if the original string is the same as the reversed string
if input_string == reversed_string:
    print(f"'{input_string}' is a Palindrome")
else:
    print(f"'{input_string}' is not a Palindrome")

# =============Without using any in-built methods (Raw Program)===============

def is_palindrome_manual(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return input_string == reversed_string

# Example
input_string = "madam"
if is_palindrome_manual(input_string):
    print(f"'{input_string}' is a Palindrome")
else:
    print(f"'{input_string}' is not a Palindrome")

# ============ Using in-built methods============

# Using slicing to reverse
input_string = "madam"
if input_string == input_string[::-1]:  # Slicing reverses the string
    print(f"'{input_string}' is a Palindrome")
else:
    print(f"'{input_string}' is not a Palindrome")
