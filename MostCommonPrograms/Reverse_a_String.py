# Without using any in-built methods (Raw Program)

def reverse_string_manual(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string  # Adding characters in reverse order
    return reversed_string

# Example
input_str = "Hello"
output = reverse_string_manual(input_str)
print("Reversed String (Manual):", output)

#============= Using in-built methods============
def reverse_string_builtin(input_string):
    return input_string[::-1]  # Using slicing to reverse

# Example
input_str = "Hello"
output = reverse_string_builtin(input_str)
print("Reversed String (In-built):", output)

# =========without function==============
# Input string
input_string = "Hello"

# Initialize an empty string to store the reversed string
reversed_string = ""

# Loop through each character in the string
for char in input_string:
    reversed_string = char + reversed_string  # Add the character to the front of reversed_string

# Print the reversed string
print("Reversed String:", reversed_string)


