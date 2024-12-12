# Initial assignment
a = 5
print("a:", a)  # Outputs: a: 5
print(id(a))

# Reassignment
a = 10
print("a:", a)  # Outputs: a: 10
print(id(a))
# Multiple variables pointing to the same value
b = a
print("a:", a)  # Outputs: a: 10
print("b:", b)  # Outputs: b: 10
print(id(a))
print(id(b))

# Changing the value of a
a = 15
print("a:", a)  # Outputs: a: 15
print("b:", b)  # Outputs: b: 10
print(id(a))
print(id(b))


"""
Memory allocation for variables occurs at runtime when the code is executed by the Python interpreter.

Reference Counting: 
Python uses reference counting to keep track of how many references point to each object. 
When the reference count drops to zero, the memory can be reclaimed by the garbage collector.

Garbage Collection: 
Python's garbage collector reclaims memory that is no longer in use, 
ensuring efficient memory management.
"""
