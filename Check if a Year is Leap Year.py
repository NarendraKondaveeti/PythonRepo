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


"""
4 – Base Rule:
Earth ki sun ni round chese time ≈ 365.25 days

So every 4 years ki 1 day add cheyyali (0.25 × 4 = 1)

That’s why every 4 years we call it leap year

👉 100 – Correction Rule:
Kaani 0.25 kaadu actual ga 0.2422 days

So prathi 100 years ki 0.03 × 100 = 3 days ekkuva avutundi

So every 100 years ki leap year ni skip cheyyali

👉 400 – Balance Rule:
Kaani 100 years ki skip chesthe, konchem takkuva ayipotundi

So every 400 years ki malli Leap Year add cheyyali


"""

