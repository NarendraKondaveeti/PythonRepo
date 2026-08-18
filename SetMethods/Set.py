# ============================================================
# Python Set Methods - Complete Examples with Expected Output
# ============================================================

# add(item)
numbers = {10, 20, 30}
numbers.add(40)
print("add():", numbers)
# Output: {10, 20, 30, 40}

print("-" * 50)

# update(iterable)
numbers = {10, 20}
numbers.update([30, 40, 50])
print("update():", numbers)
# Output: {10, 20, 30, 40, 50}

print("-" * 50)

# remove(item)
numbers = {10, 20, 30}
numbers.remove(20)
print("remove():", numbers)
# Output: {10, 30}

print("-" * 50)

# discard(item)
numbers = {10, 20, 30}
numbers.discard(100)
print("discard():", numbers)
# Output: {10, 20, 30}

print("-" * 50)

# pop()
numbers = {10, 20, 30}
removed = numbers.pop()
print("pop() removed:", removed)
print("Remaining:", numbers)
# Output: Removed item may vary because set is unordered.

print("-" * 50)

# clear()
numbers = {10, 20, 30}
numbers.clear()
print("clear():", numbers)
# Output: set()

print("-" * 50)

# copy()
numbers = {10, 20, 30}
new_numbers = numbers.copy()
print("copy():", new_numbers)
# Output: {10, 20, 30}

print("-" * 50)

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print("union():", result)
# Output: {1, 2, 3, 4, 5}

print("-" * 50)

# intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print("intersection():", result)
# Output: {2, 3}

print("-" * 50)

# difference()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print("difference():", result)
# Output: {1}

print("-" * 50)

# symmetric_difference()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print("symmetric_difference():", result)
# Output: {1, 4}

print("-" * 50)

# intersection_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print("intersection_update():", set1)
# Output: {2, 3}

print("-" * 50)

# difference_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print("difference_update():", set1)
# Output: {1}

print("-" * 50)

# symmetric_difference_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update():", set1)
# Output: {1, 4}

print("-" * 50)

# isdisjoint()
set1 = {1, 2}
set2 = {3, 4}
print("isdisjoint():", set1.isdisjoint(set2))
# Output: True

print("-" * 50)

# issubset()
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("issubset():", set1.issubset(set2))
# Output: True

print("-" * 50)

# issuperset()
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print("issuperset():", set1.issuperset(set2))
# Output: True