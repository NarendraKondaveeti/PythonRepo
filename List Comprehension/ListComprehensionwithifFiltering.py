#ListComprehensionwithifFiltering.py

# new_list = [expression for variable in iterable if condition]

numbers = [10, 15, 20, 25]

new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

"""
A List Comprehension with an if condition contains an expression, a for loop, and a condition. First, the for loop iterates through the iterable and assigns each value to the loop variable. Next, the if condition checks the current value. If the condition is True, the current value is passed to the expression, the expression is executed, and its result is added to the new list. If the condition is False, the expression is not executed, and that value is skipped. Only the values that satisfy the condition are included in the new list.
"""