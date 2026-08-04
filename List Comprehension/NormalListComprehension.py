# new_list = [expression for variable in iterable]
names = ["Alice", "Bob", "Charlie"]
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
numbers = [10, 20, 30]

print([num*2 for num in numbers])
print([num for num in numbers])              # Same value
print([num * 2 for num in numbers])          # Multiply
print([num + 10 for num in numbers])         # Addition
print([num ** 2 for num in numbers])         # Square
print([len(name) for name in names])         # Length
print([name.upper() for name in names])      # Uppercase
print([user["id"] for user in users])        # Dictionary value

"""
A normal List Comprehension contains an expression and a for loop. First, the for loop iterates through the iterable and assigns each value to the loop variable. Then, the expression uses that current value and returns the result. Every returned result is automatically added to a new list. This process continues until all elements in the iterable are processed.

"""