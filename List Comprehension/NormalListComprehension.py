# new_list = [expression for variable in iterable]

numbers = [10, 20, 30]
new_list = [num for num in numbers]

print(new_list)

"""
A normal List Comprehension contains an expression and a for loop. First, the for loop iterates through the iterable and assigns each value to the loop variable. Then, the expression uses that current value and returns the result. Every returned result is automatically added to a new list. This process continues until all elements in the iterable are processed.

"""