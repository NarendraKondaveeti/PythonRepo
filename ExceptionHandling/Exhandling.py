response = {
    "user": "test"
}

try:
    print("Reading user details...")

    user_name = response["user"]

    print("User Name:", user_name)

except TypeError as e:
    print("User data is not available.")
    print("Exception:", e)

print("Continue test execution...")