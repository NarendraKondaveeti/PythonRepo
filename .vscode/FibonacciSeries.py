# ====Raw method(it means no ib-built function or methonds)=====

n = 10  # Fibonacci Series terms
a = 0  # First number
b = 1  # Second number
count = 0  # Counter

while count <= n:
    print(a, end=" ")  # Print current term
    next_term = a + b  # Calculate next term
    a = b  # Update a to next
    b = next_term  # Update b to next
    count += 1  # Increment counter

# ====without fuction but with in-built method =================

n = 10  # Number of terms
series = [0, 1]  # Starting terms

# Generate Fibonacci series
for _ in range(2, n):
    series.append(series[-1] + series[-2])  # Add the last two terms

print("Fibonacci Series:", series)

# ====with function and without in-built method/functions ======

def fibonacci_manual(n):
    a, b = 0, 1  # First two terms
    result = []  # List to store the series
    for _ in range(n):
        result.append(a)  # Add the current term
        a, b = b, a + b  # Update terms
    return result

# Example
n = 10
print("Fibonacci Series:", fibonacci_manual(n))

# ====with function and in-built methond and the input value should as at runtime ====

def fibonacci_series(n):
    series = [0, 1]  # Start with the first two terms
    for _ in range(2, n):
        series.append(series[-1] + series[-2])  # Add the last two terms
    return series

# Input runtime value
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_series(n))

