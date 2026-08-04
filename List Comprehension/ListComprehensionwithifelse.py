#ListComprehensionwithifelse.py
#new_list = [value_if_true if condition else value_if_false for variable in iterable]

"""
A List Comprehension with if...else contains an expression and a for loop. In this case, the expression itself contains the if...else statement. First, the for loop iterates through the iterable and assigns each value to the loop variable. Then, the if condition inside the expression is evaluated. If the condition is True, the value before the if keyword is returned. If the condition is False, the value after the else keyword is returned. Unlike the previous case, every iteration always returns a value, so every element in the iterable produces one output in the new list.
"""

# Syntax
#[value_if_true if condition else value_if_false for variable in iterable]

# ---------------- Numbers ----------------
numbers = [10, 20, 30, 40, 50, 55, -10, -20, -30]

["Even" if num % 2 == 0 else "Odd" for num in numbers]  # Even / Odd
print([num if num >= 0 else "Negative Value" for num in numbers])         # Negative numbers ni 0 ga marchadam

marks = [75, 45, 30, 80, 20]
["Pass" if mark >= 35 else "Fail" for mark in marks]       # Pass / Fail
["Positive" if num > 0 else "Negative" for num in numbers] # Positive / Negative
["Big" if num > 100 else "Small" for num in numbers]       # Big / Small
[num * 2 if num % 2 == 0 else num for num in numbers]      # Even numbers matrame multiply by 2
[num if num % 2 == 0 else num * 10 for num in numbers]     # Odd numbers matrame multiply by 10

# ---------------- Strings ----------------
names = ["Alice", "Bob", "Charlie","test", "TEST", "Test",""]

print([name.upper() if len(name) > 5 else name.lower() for name in names]) # Length batti Upper / Lower
print(["Valid" if name else "Empty" for name in names])                    # Empty string check
print([name if name.startswith("A") else "Unknown" for name in names])     # Starts with 'A'
print([name.upper() if name.islower() else name for name in names])   # Lowercase ni Uppercase cheyyadam
print([len(name) if name else 0 for name in names])                   # Empty ayithe 0, lekapothe length

# ---------------- Dictionary ----------------
users = [{"id": 1, "name": "Alice", "age": 25, "status": "Active", "role":"User",                "email":"alice@example.com", "verified": True},
         {"id": 2, "name": "Bob", "age": 17, "status": "Inactive", "role":"User",              "email":"bob@example.com", "verified": False},
         {"id": 3, "name": "Charlie", "age": 30, "status": "Active", "role":"Admin",            "email":"charlie@example.com", "verified": True}]

print(["Adult" if user["age"] >= 18 else "Minor" for user in users])   # Adult / Minor
print([user["name"] if user["status"] == "Active" else "Inactive User" for user in users])#Active user name
print(["Verified" if user["verified"] else "Not Verified" for user in users])  # Verification status
print([user["email"] if user["email"] else "No Email" for user in users])      # Default email text

# ---------------- Automation Testing ----------------
tests = [{"test_name": "Login Test", "status": "PASS"},
         {"test_name": "Signup Test", "status": "FAIL"},
        {"test_name": "Checkout Test", "status": "PASS"}]

print([test if test["status"] == "PASS" else "FAIL" for test in tests])      # Test result

#---------------- API Responses ----------------
responses = [{"status_code": 200, "message": "OK"},
            {"status_code": 404, "message": "Not Found"},
            {"status_code": 500, "message": "Internal Server Error"}]
["Success" if response["status_code"] == 200 else "Failed" for response in responses]  # API response status

#---------------- Web Elements ----------------
elements = [{"name": "button1", "visible": True},
            {"name": "button2", "visible": False},
            {"name": "button3", "visible": True}]

["Visible" if element["visible"] else "Hidden" for element in elements]    # Playwright element status

#---------------- Files ----------------
files = ["data.json", "report.csv", "config.json", "log.txt"]

[file if file.endswith(".json") else "Invalid File" for file in files]      # JSON file validation

#---------------- Logs ----------------
logs = ["INFO: Application started", "ERROR: Failed to connect to database", "INFO: User logged in", "ERROR: Invalid input"]
["Error" if "ERROR" in log else "Info" for log in logs]                     # Log classification

#---------------- Emails ----------------
emails = ["alice@example.com", "bob@example.com", "", "charlie@example.com"]
[email if email else "No Email" for email in emails]                        # Empty email replacement