#python enumerate() function practice
names = ["Vikram", "Ravi", "Sai"]

for name in enumerate(names):
    print("Without Unpacking: ",name)

for name in enumerate(names):
    index, value = name
    print("With Unpacking: ",index, value)

for index, value in enumerate(names):
    print("With Unpacking in Loop: ",index, value)

for index, value in enumerate(names, start=1):
    print("With Unpacking in Loop and Start=1: ",index, value)

for index, value in enumerate(names, start=1):
    print(f"With Unpacking in Loop and Start=1: {index} {value}")

for index, value in enumerate(names, start=1):
    print(f"With Unpacking in Loop and Start=1: {index} {value.upper()}")

#Student Numbering
students = ["Rahul", "Anil", "Kiran", "Teja"]

for index, value in enumerate(students, start=1):
    print(f"Student {index}: {value}")

#Even Position Elements
numbers = [10,20,30,40,50,60]

for index, value in enumerate(numbers):
    if index % 2 == 0:
        print(f"Even Position Element {index}: {value}")


# Odd Position Elements
for index, value in enumerate(numbers):
    if index % 2 != 0:
        print(f"Odd Position Element {index}: {value}")

#Find Specific Value Position
cities = ["Hyderabad","Chennai","Bangalore","Delhi"]
for index, value in enumerate(cities):
    if value == "Bangalore":
        print(f"Bangalore is at position {index}")

#Duplicate Detection
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com"
]
for index, value in enumerate(emails):
    if emails.count(value) > 1:
        print(f"Duplicate found for {value} at position {index}")

#API Response
users = [
    {"id":101,"name":"Vikram"},
    {"id":102,"name":"Ravi"},
    {"id":103,"name":"Sai"}
]
for index, user in enumerate(users):
    print(f"User {index}: ID={user['id']}, Name={user['name']}")

#Playwright Style
elements = [
    "Home",
    "Products",
    "Contact",
    "Logout"
]
for index, element in enumerate(elements):
    print(f"Element {index}: {element}")

#Enterprise Challenge
responses = [
    {"status":200},
    {"status":404},
    {"status":500},
    {"status":200},
    {"status":401}
]
for index, response in enumerate(responses):
    if response["status"] == 200:
        print(f"Success at index {index}")
    elif response["status"] == 404:
        print(f"Not Found at index {index}")
    elif response["status"] == 500:
        print(f"Server Error at index {index}")
    elif response["status"] == 401:
        print(f"Unauthorized at index {index}")

#employee Records
employees = [
    {"id": 1, "name": "Alice", "department": "Engineering"},
    {"id": 2, "name": "Bob", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "department": "Sales"}
]
for index, employee in enumerate(employees):
    print(f"Employee {index}: ID={employee['id']}, Name={employee['name']}, Department={employee['department']}")