# ====Raw method(it means no ib-built function or methonds)=====

# Function to generate a random number between a given range
import time

def generate_random(min_num, max_num):
    # Generate a random number based on current time
    time_seed = int((time.time() * 1000) % (max_num - min_num + 1)) + min_num
    return time_seed

# Input range
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

result = generate_random(min_num, max_num)
print(f"The random number between {min_num} and {max_num} is: {result}")

# ====with in-built method =================
import random

# Function to generate a random number between a given range
def generate_random(min_num, max_num):
    return random.randint(min_num, max_num)  # Use randint() from random module

# Input range
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

result = generate_random(min_num, max_num)
print(f"The random number between {min_num} and {max_num} is: {result}")

