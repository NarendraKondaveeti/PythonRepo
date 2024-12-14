######### without in-built methods
# Function to count vowels and consonants in a string by 
def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    
    # Loop through each character in the string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
                
    return vowels_count, consonants_count

# Input string
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)

############# with In-built Methods:
# Function to count vowels and consonants in a string using in-built methods
def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    
    # Filter out vowels and consonants using list comprehension
    vowels_count = len([char for char in input_string if char in vowels])
    consonants_count = len([char for char in input_string if char.isalpha() and char not in vowels])
    
    return vowels_count, consonants_count

# Input string
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)
