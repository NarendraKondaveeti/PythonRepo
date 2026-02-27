# ====Raw method(it means no ib-built function or methonds)=====

# Function to find the missing number in an array
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = 0
    for num in arr:  # Calculate the sum of elements in the array
        actual_sum += num
    return total_sum - actual_sum  # Missing number is the difference

# Input array
n = int(input("Enter the size of the array (including the missing number): "))
arr = list(map(int, input(f"Enter {n-1} numbers from 1 to {n}, separated by space: ").split()))

missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")

# ====with in-built method =================

# Function to find the missing number in an array using sum()
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum of array elements using sum()
    return total_sum - actual_sum  # Missing number is the difference

# Input array
n = int(input("Enter the size of the array (including the missing number): "))
arr = list(map(int, input(f"Enter {n-1} numbers from 1 to {n}, separated by space: ").split()))

missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")
