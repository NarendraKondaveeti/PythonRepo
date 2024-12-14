# Raw Method (No In-Built Functions or Methods)
n = 10  # Number of terms
a = 0  # First term
b = 1  # Second term
count = 0  # Counter to track terms

# Generate Fibonacci series
while count < n:
    print(a, end=" ")  # Print the current term
    next_term = a + b  # Calculate the next term
    a = b  # Update a to the next term
    b = next_term  # Update b to the next term
    count += 1  # Increment the counter

# Without Function but Using In-Built Methods
n = 10  # Number of terms
series = [0, 1]  # Starting terms

# Generate Fibonacci series
for _ in range(2, n):
    series.append(series[-1] + series[-2])  # Add the last two terms

print("Fibonacci Series:", series)

# With Function but Without In-Built Methods
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

# With Function and In-Built Methods (Input Value at Runtime)
def fibonacci_series(n):
    series = [0, 1]  # Start with the first two terms
    for _ in range(2, n):
        series.append(series[-1] + series[-2])  # Add the last two terms
    return series

# Input runtime value
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_series(n))
