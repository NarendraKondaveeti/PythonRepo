# ====Raw method(it means no ib-built function or methonds)=====

# Function to remove all whitespaces from a string
def remove_whitespaces(s):
    result = ""
    for char in s:  # Loop through each character in the string
        if char != " ":  # If the character is not a whitespace, add it to the result
            result += char
    return result

# Input string
string = input("Enter a string: ")

result = remove_whitespaces(string)
print(f"The string without whitespaces is: '{result}'")

# ====with in-built method =================
# Function to remove all whitespaces from a string using replace()
def remove_whitespaces(s):
    return s.replace(" ", "")  # Use the built-in replace() method to remove all whitespaces

# Input string
string = input("Enter a string: ")

result = remove_whitespaces(string)
print(f"The string without whitespaces is: '{result}'")

