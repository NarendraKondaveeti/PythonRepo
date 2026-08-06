# ============================================================
# upper()
# ============================================================

text = "hello world"

result = text.upper()

print("Original :", text) # hello world
print("Result   :", result) # HELLO WORLD   


# ============================================================
# lower()
# ============================================================

text = "HELLO WORLD"

result = text.lower()

print("Original :", text) # HELLO WORLD
print("Result   :", result) # hello world


# ============================================================
# title()
# ============================================================

text = "hello world python"

result = text.title()

print("Original :", text) # hello world python
print("Result   :", result) # Hello World Python


# ============================================================
# capitalize()
# ============================================================

text = "hello WORLD"

result = text.capitalize()

print("Original :", text) # hello WORLD
print("Result   :", result) # Hello world


# ============================================================
# swapcase()
# ============================================================

text = "Hello World"

result = text.swapcase()

print("Original :", text) # Hello World
print("Result   :", result) # hELLO wORLD


# ============================================================
# strip()
# ============================================================

text = "   Hello    World   "

result = text.strip()

print("Original :", text) #   Hello World   
print("Result   :", result) # Hello    World


# ============================================================
# strip(chars)
# ============================================================

text = "***Hel**lo***"

result = text.strip("*")

print("Original :", text) # ***Hello***
print("Result   :", result) # Hel**lo

# ============================================================
# replace(old, new)
# ============================================================

text = "I like Java"

result = text.replace("Java", "Python")

print("Original :", text) # I like Java
print("Result   :", result) # I like Python


# ============================================================
# replace(old, new, count)
# ============================================================

text = "apple apple apple"

result = text.replace("apple", "mango", 2)

print("Original :", text) # apple apple apple
print("Result   :", result) # mango mango apple


# ============================================================
# split()
# ============================================================

text = "Python Java C++"

result = text.split()

print("Original :", text) # Python Java C++
print("Result   :", result) # ['Python', 'Java', 'C++']


# ============================================================
# split(separator)
# ============================================================

text = "Apple,Mango,Grapes"

result = text.split(",")

print("Original :", text) # Apple,Mango,Grapes
print("Result   :", result) # ['Apple', 'Mango', 'Grapes']

# ============================================================
# split(separator, maxsplit)
# ============================================================

text = "A-B-C-D-E"

result = text.split("-",2)

print("Original :", text) # A-B-C-D-E
print("Result   :", result) # ['A', 'B', 'C-D-E']

# ============================================================
# find(value)
# ============================================================

text = "Hello Python"

result = text.find("Python")

print("Original :", text) # Hello Python
print("Result   :", result) # 6


# ============================================================
# find(value, start)
# ============================================================

text = "Python Java Python"

result = text.find("Python", 7)

print("Original :", text) # Python Java Python
print("Result   :", result) # 13


# ============================================================
# find(value, start, end)
# ============================================================

text = "Python Java Python"

result = text.find("Python", 0, 10)

print("Original :", text) # Python Java Python
print("Result   :", result) # 0


# ============================================================
# startswith(prefix)
# ============================================================

text = "Python Programming"

print("Original :", text) # Python Programming
print("Result   :", text.startswith("Python")) # True


# ============================================================
# startswith(prefix, start)
# ============================================================

text = "Hello Python"

print("Original :", text) # Hello Python
print("Result   :", text.startswith("Python", 6)) # True
print("Result   :", text.startswith("Hello", 0)) # False

# ============================================================
# startswith(prefix, start, end)
# ============================================================

text = "Hello Python"

print("Original :", text) # Hello Python
print("Result   :", text.startswith("Python", 0, 12)) # True

# ============================================================
# replace(old, new)
# ============================================================

text = "I like Java"

result = text.replace("Java", "Python")

print("Original String :", text) # I like Java
print("Updated String  :", result) # I like Python


# ============================================================
# replace(old, new, count)
# ============================================================

text = "apple apple apple apple"

result = text.replace("apple", "mango", 2)

print("Original String :", text) # apple apple apple apple
print("Updated String  :", result) # mango mango apple apple

# Output:
# Original String : apple apple apple apple
# Updated String  : mango mango apple apple

# ============================================================
# split()
# ============================================================

text = "Python Java C++"

result = text.split()

print(result)

# Output:
# ['Python', 'Java', 'C++']


# ============================================================
# split(separator)
# ============================================================

text = "Apple,Mango,Grapes"

result = text.split(",")

print(result)

# Output:
# ['Apple', 'Mango', 'Grapes']


# ============================================================
# split(separator, maxsplit)
# ============================================================

text = "A-B-C-D-E"

result = text.split("-", 2)

print(result)

# Output:
# ['A', 'B', 'C-D-E']

# ============================================================
# rsplit()
# ============================================================

text = "A-B-C-D-E"

result = text.rsplit("-", 2)

print(result)

# Output:
# ['A-B-C', 'D', 'E']

# ============================================================
# join()
# ============================================================

fruits = ["Apple", "Mango", "Orange"]

result = ",".join(fruits)

print(result)

# Output:
# Apple,Mango,Orange


# ============================================================
# join() with Space
# ============================================================

words = ["I", "Love", "Python"]

result = " ".join(words)

print(result)

# Output:
# I Love Python

# ============================================================
# find(value)
# ============================================================

text = "Hello Python"

print(text.find("Python"))

# Output:
# 6


# ============================================================
# find(value, start)
# ============================================================

text = "Python Java Python"

print(text.find("Python", 7))

# Output:
# 12


# ============================================================
# find(value, start, end)
# ============================================================

text = "Python Java Python"

print(text.find("Python", 0, 10))

# Output:
# 0

# ============================================================
# rfind()
# ============================================================

text = "Python Java Python"

print(text.rfind("Python"))

# Output:
# 12

# ============================================================
# index()
# ============================================================

text = "Hello Python"

print(text.index("Python"))

# Output:
# 6

# ============================================================
# rindex()
# ============================================================

text = "Python Java Python"

print(text.rindex("Python"))

# Output:
# 12

# ============================================================
# rindex()
# ============================================================

text = "Python Java Python"

print(text.rindex("Python"))

# Output:
# 12

# ============================================================
# count(value)
# ============================================================

text = "apple apple mango apple"

print(text.count("apple"))

# Output:
# 3


# ============================================================
# count(value, start)
# ============================================================

text = "apple apple mango apple"

print(text.count("apple", 6))

# Output:
# 2


# ============================================================
# count(value, start, end)
# ============================================================

text = "apple apple mango apple"

print(text.count("apple", 0, 15))

# Output:
# 2

# ============================================================
# endswith(suffix)
# ============================================================

text = "Python Programming"

result = text.endswith("Programming")

print(result)

# Output:
# True


# ============================================================
# endswith(suffix, start)
# ============================================================

text = "Hello Python"

result = text.endswith("Python", 0)

print(result)

# Output:
# True


# ============================================================
# endswith(suffix, start, end)
# ============================================================

text = "Hello Python"

result = text.endswith("Hello", 0, 5)

print(result)

# Output:
# True

# ============================================================
# isalpha()
# ============================================================

text = "Python"

print(text.isalpha())

# Output:
# True


# ============================================================
# isalpha()
# ============================================================

text = "Python123"

print(text.isalpha())

# Output:
# False


# ============================================================
# isalpha()
# ============================================================

text = "Python Language"

print(text.isalpha())

# Output:
# False

# ============================================================
# isdigit()
# ============================================================

text = "12345"

print(text.isdigit())

# Output:
# True


# ============================================================
# isdigit()
# ============================================================

text = "123abc"

print(text.isdigit())

# Output:
# False


# ============================================================
# isdigit()
# ============================================================

text = "12.5"

print(text.isdigit())

# Output:
# False

# ============================================================
# isalnum()
# ============================================================

text = "Python123"

print(text.isalnum())

# Output:
# True


# ============================================================
# isalnum()
# ============================================================

text = "Python 123"

print(text.isalnum())

# Output:
# False


# ============================================================
# isalnum()
# ============================================================

text = "Python@123"

print(text.isalnum())

# Output:
# False

# ============================================================
# isalnum()
# ============================================================

text = "Python123"

print(text.isalnum())

# Output:
# True


# ============================================================
# isalnum()
# ============================================================

text = "Python 123"

print(text.isalnum())

# Output:
# False


# ============================================================
# isalnum()
# ============================================================

text = "Python@123"

print(text.isalnum())

# Output:
# False

# ============================================================
# isspace()
# ============================================================

text = "   "

result = text.isspace()

print(result)

# Output:
# True


# ============================================================
# isspace()
# ============================================================

text = "\t\n"

result = text.isspace()

print(result)

# Output:
# True


# ============================================================
# isspace()
# ============================================================

text = " Hello "

result = text.isspace()

print(result)

# Output:
# False


# ============================================================
# isspace()
# ============================================================

text = ""

result = text.isspace()

print(result)

# Output:
# False

# ============================================================
# isupper()
# ============================================================

text = "PYTHON"

print(text.isupper())

# Output:
# True


# ============================================================
# isupper()
# ============================================================

text = "PYTHON123"

print(text.isupper())

# Output:
# True


# ============================================================
# isupper()
# ============================================================

text = "Python"

print(text.isupper())

# Output:
# False

# ============================================================
# istitle()
# ============================================================

text = "Hello World"

print(text.istitle())

# Output:
# True


# ============================================================
# istitle()
# ============================================================

text = "Python Programming Language"

print(text.istitle())

# Output:
# True


# ============================================================
# istitle()
# ============================================================

text = "hello World"

print(text.istitle())

# Output:
# False


# ============================================================
# istitle()
# ============================================================

text = "HELLO WORLD"

print(text.istitle())

# Output:
# False

