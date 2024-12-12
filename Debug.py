n = 10  # Fibonacci Series terms
a = 0  # First number
b = 1  # Second number
count = 0  # Counter

while count < n:
    print("count, n= ",count, n)
    print("a, end= ", a, end='')  # Print current term
    next_term = a + b  # Calculate next term
    print("next_term = a + b=",next_term, a, b)
    a = b  # Update a to next
    print("a=", a)
    b = next_term  # Update b to next
    print("b=", b)
    count += 1  # Increment counter
    print("count =", count)
