# ====Raw method(it means no ib-built function or methonds)=====

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        result = -result
    return result

# Function for division
def divide(a, b):
    if b == 0:
        return "Division by zero is undefined"
    result = 0
    is_negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)
    while a >= b:
        a -= b
        result += 1
    return -result if is_negative else result

# Simple calculator implementation
def calculator():
    print("Simple Calculator")
    print("Options: + (add), - (subtract), * (multiply), / (divide)")
    num1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = int(input("Enter second number: "))

    if operator == "+":
        print(f"Result: {add(num1, num2)}")
    elif operator == "-":
        print(f"Result: {subtract(num1, num2)}")
    elif operator == "*":
        print(f"Result: {multiply(num1, num2)}")
    elif operator == "/":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operator!")

calculator()

# ====with in-built method =================
# Simple calculator implementation using in-built operators
def calculator():
    print("Simple Calculator")
    print("Options: + (add), - (subtract), * (multiply), / (divide)")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(f"Result: {num1 + num2}")
    elif operator == "-":
        print(f"Result: {num1 - num2}")
    elif operator == "*":
        print(f"Result: {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Division by zero is undefined")
    else:
        print("Invalid operator!")

calculator()

