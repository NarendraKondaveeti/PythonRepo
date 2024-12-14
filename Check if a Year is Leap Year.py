# ====Raw method(it means no ib-built function or methonds)=====

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# ====with in-built method =================
import calendar

# Function to check if a year is a leap year using calendar.isleap()
def is_leap_year(year):
    return calendar.isleap(year)  # Use the built-in isleap() method

# Input year
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

