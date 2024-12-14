# ====Raw method(it means no ib-built function or methonds)=====

# Function to implement a simple login system
def login_system():
    # Predefined username and password
    username = "user1"
    password = "password123"

    # User input for username and password
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    # Checking username and password
    if input_username == username and input_password == password:
        return "Login successful!"
    else:
        return "Invalid username or password."

# Call the login system function
result = login_system()
print(result)

# ====with in-built method =================
import getpass

# Function to implement a simple login system
def login_system():
    # Predefined username and password
    username = "user1"
    password = "password123"

    # User input for username and password using getpass to hide the password
    input_username = input("Enter username: ")
    input_password = getpass.getpass("Enter password: ")

    # Checking username and password
    if input_username == username and input_password == password:
        return "Login successful!"
    else:
        return "Invalid username or password."

# Call the login system function
result = login_system()
print(result)

