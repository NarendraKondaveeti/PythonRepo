# ====Raw method(it means no ib-built function or methonds)=====
# Function to find the second largest element in an array
def second_largest(arr):
    largest = second = float('-inf')  # Initialize both largest and second to negative infinity
    for num in arr:
        if num > largest:
            second = largest  # Update second largest
            largest = num  # Update largest
        elif num > second and num != largest:
            second = num  # Update second largest when a new number is found that is smaller than largest
    return second

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

second_largest_element = second_largest(arr)
print(f"The second largest element in the array is: {second_largest_element}")


# ====with in-built method =================
# Function to find the second largest element using in-built methods
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates using set
    arr.sort()  # Sort the array
    return arr[-2]  # The second largest element will be the second to last in the sorted array

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

second_largest_element = second_largest(arr)
print(f"The second largest element in the array is: {second_largest_element}")

