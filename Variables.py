"""
Variables store data

Variable is nothing but a name given to a reserved memory location where the data is stored

We don't need to specify the Data Type for any variable

Storing different types of data into the variables

Variable Names: Must start with a letter or an underscore (_), followed by letters, digits, or underscores
valid_name = "John"
_another_valid_name = "Doe"
ASD12 = "Test"
invalid-name = "Error"  # This will raise a syntax error

Case Sensitivity:- Variables are case-sensitive.(it means, Age, age both are two different variables)

"snake_case" Snake case separates each word with an underscore character,
When using snake case, all letters need to be lowercase.

"camelCase" When using camel case, you start by making the first word lowercase.
Then, you capitalize the first letter of each word that follows.

So, a capital letter appears at the start of the second word and at each new subsequent word that follows it.

"PascalCase" pascal case requires the first letter of the first word to also be capitalized.  every word starts with an uppercase letter.

To know the variable what kind of data is contains use type() function
Ex:- print(type(A))
"""
a = 9  # integer
b = 1.25  # float
c = "Python"  # String
d = 'Pytest'  # String
e = True  # Boolean
A, B, C = 1, 2, 3  # in Single line
print(a, b, c)  # 9 1.25 Python
a = b = c = 10  # for all variables reference the one location in memory

my_first_name = "Testing"

# Global: Declared outside any function, accessible anywhere in the code.

global_var = "I am global"
def print_global():
    print(global_var)
print_global()  # Outputs: I am global

# Local: Declared inside a function, accessible only within that function.

def my_function():
    local_var = "I am local"
    print(local_var)
my_function()  # Outputs: I am local
print(local_var)  # Raises an error because local_var is not accessible here