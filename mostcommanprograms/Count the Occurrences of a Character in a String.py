# ====Raw method(it means no ib-built function or methonds)=====

# Function to count the occurrences of a character in a string
def count_occurrences(s, char):
    count = 0
    for c in s:  # Loop through each character in the string
        if c == char:  # If the character matches, increment the count
            count += 1
    return count

# Input string and character
string = input("Enter a string: ")
char = input("Enter the character to count: ")

result = count_occurrences(string, char)
print(f"The character '{char}' appears {result} times in the string '{string}'.")

# ====with in-built method =================

# Function to count the occurrences of a character in a string using count()
def count_occurrences(s, char):
    return s.count(char)  # Use the built-in count() method to count occurrences

# Input string and character
string = input("Enter a string: ")
char = input("Enter the character to count: ")

result = count_occurrences(string, char)
print(f"The character '{char}' appears {result} times in the string '{string}'.")
