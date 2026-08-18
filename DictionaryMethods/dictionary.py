# ============================================================
# Python Dictionary Methods - Complete Examples with Expected Output
# ============================================================

# get(key)
student = {"id": 101, "name": "Vikram", "age": 25}

print(student.get("name"))
# Output:
# Vikram

print("-" * 50)

# get(key, default)
student = {"id": 101, "name": "Vikram"}

print(student.get("city", "Hyderabad"))
# Output:
# Hyderabad

print("-" * 50)

# keys()
student = {"id": 101, "name": "Vikram", "age": 25}

print(student.keys())
# Output:
# dict_keys(['id', 'name', 'age'])

print("-" * 50)

# values()
student = {"id": 101, "name": "Vikram", "age": 25}

print(student.values())
# Output:
# dict_values([101, 'Vikram', 25])

print("-" * 50)

# items()
student = {"id": 101, "name": "Vikram", "age": 25}

print(student.items())
# Output:
# dict_items([('id', 101), ('name', 'Vikram'), ('age', 25)])

print("-" * 50)

# update(other_dict)
student = {"id": 101, "name": "Vikram"}
student.update({"age": 25, "city": "Hyderabad"})
print(student)
# Output:
# {'id': 101, 'name': 'Vikram', 'age': 25, 'city': 'Hyderabad'}

print("-" * 50)

# update(key=value)
student = {"id": 101, "name": "Vikram"}
student.update(age=25, city="Hyderabad")
print(student)
# Output:
# {'id': 101, 'name': 'Vikram', 'age': 25, 'city': 'Hyderabad'}

print("-" * 50)

# pop(key)
student = {"id": 101, "name": "Vikram", "age": 25}
removed = student.pop("age")
print("Removed:", removed)
print(student)
# Output:
# Removed: 25
# {'id': 101, 'name': 'Vikram'}

print("-" * 50)

# pop(key, default)
student = {"id": 101, "name": "Vikram"}
removed = student.pop("city", "Not Found")
print(removed)
print(student)
# Output:
# Not Found
# {'id': 101, 'name': 'Vikram'}

print("-" * 50)

# popitem()
student = {"id": 101, "name": "Vikram", "age": 25}
removed = student.popitem()
print("Removed:", removed)
print(student)
# Output:
# Removed: ('age', 25)
# {'id': 101, 'name': 'Vikram'}

print("-" * 50)

# clear()
student = {"id": 101, "name": "Vikram"}
student.clear()
print(student)
# Output:
# {}

print("-" * 50)

# copy()
student = {"id": 101, "name": "Vikram"}
new_student = student.copy()
print(new_student)
# Output:
# {'id': 101, 'name': 'Vikram'}

print("-" * 50)

# setdefault(key)
student = {"id": 101, "name": "Vikram"}
value = student.setdefault("age")
print(value)
print(student)
# Output:
# None
# {'id': 101, 'name': 'Vikram', 'age': None}

print("-" * 50)

# setdefault(key, default)
student = {"id": 101, "name": "Vikram"}
value = student.setdefault("city", "Hyderabad")
print(value)
print(student)
# Output:
# Hyderabad
# {'id': 101, 'name': 'Vikram', 'city': 'Hyderabad'}

print("-" * 50)

# fromkeys(iterable)
keys = ["id", "name", "age"]
result = dict.fromkeys(keys)
print(result)
# Output:
# {'id': None, 'name': None, 'age': None}

print("-" * 50)

# fromkeys(iterable, value)
keys = ["id", "name", "age"]
result = dict.fromkeys(keys, "Not Available")
print(result)
# Output:
# {'id': 'Not Available', 'name': 'Not Available', 'age': 'Not Available'}