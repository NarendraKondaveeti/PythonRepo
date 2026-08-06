numbers = [10, 20, 30]

result = zip(numbers)

print(list(result))

names = ["Vikram", "Rahul", "Ravi", "Sai"]
ages = [25, 30]
id = [101, 102, 103]

for name, age, i in zip(names, ages, id):
    print(f"Name: {name}, Age: {age}, ID: {i}")