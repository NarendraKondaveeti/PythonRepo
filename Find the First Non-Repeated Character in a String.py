# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the first non-repeated character in a string
def first_non_repeated_char(s):
    for char in s:  # Loop through each character in the string
        if s.count(char) == 1:  # Check if the character appears only once
            return char
    return None  # Return None if no non-repeated character is found

# Input string
string = input("Enter a string: ")

result = first_non_repeated_char(string)
if result:
    print(f"The first non-repeated character is: {result}")
else:
    print("No non-repeated character found.")


# ====with in-built method =================

from collections import Counter

# Function to find the first non-repeated character using collections.Counter
def first_non_repeated_char(s):
    count = Counter(s)  # Count the occurrences of each character
    for char in s:
        if count[char] == 1:  # If the character appears only once
            return char
    return None  # Return None if no non-repeated character is found

# Input string
string = input("Enter a string: ")

result = first_non_repeated_char(string)
if result:
    print(f"The first non-repeated character is: {result}")
else:
    print("No non-repeated character found.")
