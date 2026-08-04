#ListComprehensionwithifFiltering.py

# new_list = [expression for variable in iterable if condition]

"""
A List Comprehension with an if condition contains an expression, a for loop, and a condition. First, the for loop iterates through the iterable and assigns each value to the loop variable. Next, the if condition checks the current value. If the condition is True, the current value is passed to the expression, the expression is executed, and its result is added to the new list. If the condition is False, the expression is not executed, and that value is skipped. Only the values that satisfy the condition are included in the new list.
"""

# Syntax
#[expression for variable in iterable if condition]


# ---------------- Numbers ----------------
numbers = [10, 20, 30, 40, 50, 55]

[num for num in numbers if num % 2 == 0]              # Even numbers
[num for num in numbers if num % 2 != 0]              # Odd numbers
[num for num in numbers if num > 50]                  # Greater than 50
[num for num in numbers if num < 50]                  # Less than 50
[num for num in numbers if num >= 35]                 # Greater than or equal to 35
[num for num in numbers if num <= 35]                 # Less than or equal to 35
[num for num in numbers if num == 100]                # Equal to 100
[num for num in numbers if num != 100]                # Not equal to 100


# ---------------- Strings ----------------
names = ["Alice", "Bob", "Charlie", "TEST", "test", "Test"]

[name for name in names if len(name) > 5]             # Length greater than 5
[name for name in names if len(name) <= 5]            # Length less than or equal to 5
[name for name in names if name.startswith("A")]      # Starts with 'A'
[name for name in names if name.endswith("n")]        # Ends with 'n'
print([name for name in names if "a" in name.lower()])       # Contains letter 'a'
print([name for name in names if name.isupper()])            # Fully uppercase strings
print([name for name in names if name.islower()])            # Fully lowercase strings

# ---------------- Dictionary ----------------
users = [{"id": 1, "name": "Alice", "age": 25, "status": "Active", "role":"User",                "email":"alice@example.com", "verified": True}, 
{"id": 2, "name": "Bob", "age": 30, "status": "Inactive", "role": "User", 
 "email": "bob@example.com", "verified": False}, 
{"id": 3, "name": "Charlie", "age": 35, "status": "Active", "role": "Admin", 
 "email": "charlie@example.com", "verified": True}, 
{"id": 4, "name": "David", "age": 40, "status": "Inactive", "role": "User", 
 "email": "david@example.com", "verified": False}, 
{"id": 5, "name": "Eve", "age": 45, "status": "Active", "role": "Admin", 
 "email": "eve@example.com", "verified": True}]

print([user for user in users if user["age"] >= 18])         # Age >= 18
print([user for user in users if user["status"] == "Active"])    # Active users
print([user["id"] for user in users if user["status"] == "Active"])    # Active user IDs
print([user["name"] for user in users if user["role"] == "Admin"])     # Admin names
print([user["email"] for user in users if user["verified"]])           # Verified user emails


# ---------------- Automation Testing ----------------
tests = [{"name": "test_login", "status": "PASS"},
         {"name": "test_logout", "status": "FAIL"}, 
         {"name": "test_signup", "status": "PASS"}]

print([test for test in tests if test["status"] == "PASS"])          # Passed test cases
print([test for test in tests if test["status"] == "FAIL"])          # Failed test cases

#====================responses====================
responses = [{"status_code": 200, "body": "Success"}, 
             {"status_code": 404, "body": "Not Found"}, 
             {"status_code": 500, "body": "Server Error"}]

print("response:", [response for response in responses if response["status_code"] == 200])    # Success API responses

#====================elements====================
elements = [{"name": "button1", "visible": True}, 
            {"name": "button2", "visible": False}, 
            {"name": "button3", "visible": True}]

print([element for element in elements if element["visible"]]) 
#[element for element in elements if element.is_visible()]      # Visible elements (Playwright)

#====================files====================
files = ["data.json", 
         "report.csv", 
         "config.json", 
         "log.txt"]

print([file for file in files if file.endswith(".json")])             # JSON files only

print([file for file in files if file.endswith(".csv")])              # CSV files only

#====================logs====================
logs = ["INFO: Application started", 
        "ERROR: Failed to connect to database", 
        "INFO: User logged in", 
        "ERROR: Invalid input"]

print([log for log in logs if "ERROR" in log])                        # Error logs only

#====================emails====================
emails = ["alice@example.com", "bob@example.com", "", "charlie@example.com"]
print([email for email in emails if "bob" in email])                        # Remove empty email values