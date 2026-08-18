from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        page.goto("https://example.com")

        page.locator("#username").fill("admin")

        print("Username field found")

    except Exception as e:
        print("Test failed")
        print("Error:", e)

    finally:
        browser.close()
        print("Browser closed")


#=======================

# Exercise 1: Handle missing API response data

response_data = {
    "name": "Vikram",
    "email": "vikram@test.com"
}

try:
    print("Reading user ID...")
    user_id = response_data["user_id"]
    print("User ID:", user_id)

except KeyError:
    print("user_id is missing in the API response.")

print("Continue with remaining test execution...")


#=======================

# Exercise 2: Handle missing test data file

file_name = "test_data.txt"

try:
    print("Opening test data file...")

    file = open(file_name, "r")
    data = file.read()

    print("Test data:")
    print(data)

    file.close()

except FileNotFoundError:
    print("Test data file was not found.")

print("Continue test execution...")

#=======================

# Exercise 3: API response processing

status_code = 200

try:
    print("Sending API request...")

    if status_code != 200:
        raise Exception("API request failed")

    print("API request completed successfully.")

except Exception as e:
    print("API request failed:", e)

else:
    print("No exception occurred.")
    print("Now validate API response.")
    print("Validate status code = 200")

print("Continue remaining tests...")

#=======================

# Exercise 4: Browser cleanup using finally

browser = None

try:
    print("Starting browser...")

    browser = "Chrome Browser"
    print("Browser started.")

    print("Executing login test...")

    # Simulating test execution
    username = "admin"
    password = "wrong"

    if password != "admin123":
        raise Exception("Invalid password")

    print("Login successful.")

except Exception as e:
    print("Test failed:", e)

finally:
    print("Closing browser...")
    browser = None
    print("Browser closed.")

print("Test execution completed.")

#=======================

# Exercise 5: Raise an exception intentionally

username = "admin"
password = "12345"

try:
    print("Validating login details...")

    if username != "admin":
        raise ValueError("Invalid username")

    if password != "admin123":
        raise ValueError("Invalid password")

    print("Login validation successful.")

except ValueError as e:
    print("Validation failed:", e)

print("Continue test execution...")


#=======================

# Exercise 6: Raise exception when API status is unexpected

response_status = 500

try:
    print("Checking API response...")

    if response_status != 200:
        raise AssertionError(
            f"Expected status code 200, but received {response_status}"
        )

    print("API response is valid.")

except AssertionError as e:
    print("API validation failed:", e)

print("Continue remaining test execution...")

#=======================

# Exercise 7: Complete login test flow

browser = None

try:
    print("Starting browser...")

    browser = "Chrome"
    print("Browser started.")

    print("Opening application...")
    print("Entering username...")
    print("Entering password...")

    username = "admin"
    password = "admin123"

    if username != "admin":
        raise ValueError("Invalid username")

    if password != "admin123":
        raise ValueError("Invalid password")

except ValueError as e:
    print("Login failed:", e)

else:
    print("Login successful.")
    print("User is logged into the application.")

finally:
    print("Closing browser...")
    browser = None
    print("Browser closed.")

print("Test execution completed.")

#=======================

# Exercise 8: API validation using exception handling

response = {
    "status_code": 200,
    "user_id": 101,
    "name": "Vikram"
}

try:
    print("Validating API response...")

    status_code = response["status_code"]

    if status_code != 200:
        raise AssertionError(
            f"Expected 200, but received {status_code}"
        )

    user_id = response["user_id"]
    name = response["name"]

except KeyError as e:
    print("Required field is missing:", e)

except AssertionError as e:
    print("API validation failed:", e)

else:
    print("API response validation successful.")
    print("User ID:", user_id)
    print("Name:", name)

finally:
    print("API validation process completed.")

print("Continue remaining test cases...")


#=======================

number = 10

try:
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful.")
    print("Result:", result)

finally:
    print("Execution completed.")

#===Null/None Exception====================

response = {
    "user": None
}

try:
    print("Reading user details...")

    user_name = response["user"]["name"]

    print("User Name:", user_name)

except TypeError as e:
    print("User data is not available.")
    print("Exception:", e)

print("Continue test execution...")

######

user_name = None

try:
    print("Checking user name...")

    if user_name is None:
        raise ValueError("User name is not available.")

    print("User Name:", user_name.upper())

except ValueError as e:
    print("Validation failed:", e)

print("Continue execution...")