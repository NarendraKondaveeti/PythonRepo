# ====Raw method(it means no ib-built function or methonds)=====
# Function to count the number of digits in a number
def count_digits(number):
    count = 0
    while number != 0:
        number = number // 10  # Remove the last digit by integer division
        count += 1  # Increment the count for each digit count = count + 1
    return count

# Input number
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"Number of digits: {digit_count}")


# ====with in-built method =================

# Function to count the number of digits using in-built methods
def count_digits(number):
    return len(str(abs(number)))  # Convert the number to a string and count the length

# Input number
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"Number of digits: {digit_count}")

#================
def my_fun(num):
    if num >= 0:
        return len(str(num))
    else:
        return len(str(num))-1

num = int(input("Enter a number: "))
dig_nos = my_fun(num)
print(f'{num} digits = {dig_nos}')

#================
def my_fun(num):
    if num.startswith("-"):
        return len(num) - 1  # Remove minus sign from count
    else:
        return len(num)

num = input("Enter a number: ")
dig_nos = my_fun(num)
print(f'{num} digits = {dig_nos}')