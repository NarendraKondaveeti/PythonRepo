#ListComprehensionwithifelse.py
#new_list = [value_if_true if condition else value_if_false for variable in iterable]

numbers = [10, 15, 20]

new_list = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(new_list)

"""
A List Comprehension with if...else contains an expression and a for loop. In this case, the expression itself contains the if...else statement. First, the for loop iterates through the iterable and assigns each value to the loop variable. Then, the if condition inside the expression is evaluated. If the condition is True, the value before the if keyword is returned. If the condition is False, the value after the else keyword is returned. Unlike the previous case, every iteration always returns a value, so every element in the iterable produces one output in the new list.
"""