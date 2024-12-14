# ====Raw method(it means no ib-built function or methonds)=====

# Function to find the maximum occurring character in a string
def max_occuring_char(s):
    max_count = 0
    max_char = ''
    
    # Loop through each character in the string
    for char in s:
        count = 0
        # Count occurrences of the character
        for ch in s:
            if ch == char:
                count += 1
        # If the current character count is greater than the previous maximum
        if count > max_count:
            max_count = count
            max_char = char
    
    return max_char

# Input string
s = input("Enter a string: ")

result = max_occuring_char(s)
print(f"The maximum occurring character is: {result}")

# ====with in-built method =================

from collections import Counter

# Function to find the maximum occurring character using Counter
def max_occuring_char(s):
    # Using Counter to get the frequency of each character
    count = Counter(s)
    # Finding the character with the maximum count
    return max(count, key=count.get)

# Input string
s = input("Enter a string: ")

result = max_occuring_char(s)
print(f"The maximum occurring character is: {result}")
