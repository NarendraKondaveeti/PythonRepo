
# Syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Without Separator
print("apple", "banana", "cherry")  # apple banana cherry

# With Separator
print("apple", "banana", "cherry", sep=" - ")  # apple - banana - cherry

# With Default End Line
print("apple")
print("banana")
print("cherry")

# With Default End Line
print("apple", end=", ")
print("banana", end=", ")
print("cherry")

name = "Alice"
favorite_number = 7

# Using commas
print("My name is", name, "and my favorite number is", favorite_number)

# f-strings are the most modern and readable way to format strings.
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

pi = 3.14159
print(f"Pi rounded to two decimal places: {pi:.2f}")

# The format method is flexible and works in all versions of Python 3.
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

pi = 3.14159
print("Pi rounded to two decimal places: {:.2f}".format(pi))

# The round function rounds a number to a specified number of decimal places.
pi = 3.14159
rounded_pi = round(pi, 2)
print("Pi rounded to two decimal places:", rounded_pi)

# You can use % to format strings. This is an older method but still useful.
pi = 3.14159
print("Pi rounded to two decimal places: %.2f" % pi)

# Basic print with Concatenation
name = "Alice"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")